#!/usr/bin/env python3
"""Build the small, provenance-rich Bad-Hashes feed from approved sources."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


@dataclass(frozen=True)
class Record:
    sha256: str
    malware_family: str
    source: str
    source_reference: str
    source_commit: str
    published_utc: str
    confidence: str


def git_file_metadata(repository: Path, relative_path: str) -> tuple[str, datetime]:
    command = [
        "git",
        "-c",
        f"safe.directory={repository.resolve()}",
        "-C",
        str(repository),
        "log",
        "-1",
        "--format=%H|%cI",
        "--",
        relative_path,
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    value = result.stdout.strip()
    if not value or "|" not in value:
        raise ValueError(f"No Git history found for {relative_path}")
    commit, published = value.split("|", 1)
    published_at = datetime.fromisoformat(published).astimezone(timezone.utc)
    return commit, published_at


def read_hashes(path: Path) -> list[str]:
    hashes: list[str] = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        value = raw_line.strip().lower()
        if not value or value.startswith("#"):
            continue
        if not SHA256_RE.fullmatch(value):
            raise ValueError(f"Invalid SHA-256 in {path} on line {line_number}: {value}")
        hashes.append(value)
    if not hashes:
        raise ValueError(f"Approved source file contains no hashes: {path}")
    return hashes


def render_csv(records: list[Record]) -> str:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(
        [
            "sha256",
            "malware_family",
            "source",
            "source_reference",
            "source_commit",
            "published_utc",
            "confidence",
        ]
    )
    for record in records:
        writer.writerow(
            [
                record.sha256,
                record.malware_family,
                record.source,
                record.source_reference,
                record.source_commit,
                record.published_utc,
                record.confidence,
            ]
        )
    return output.getvalue()


def write_if_changed(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def build(config_path: Path, source_root: Path, output_dir: Path, now: datetime) -> int:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    max_hashes = int(config["max_hashes"])
    max_source_age_days = int(config["max_source_age_days"])
    if not 1 <= max_hashes <= 100:
        raise ValueError("max_hashes must be between 1 and 100")

    records_by_hash: dict[str, Record] = {}
    for source in config["sources"]:
        source_path = source_root / source["local_path"]
        if not source_path.is_file():
            raise FileNotFoundError(f"Approved source file is missing: {source_path}")

        commit, published_at = git_file_metadata(source_root, source["local_path"])
        age_days = (now - published_at).total_seconds() / 86400
        if age_days < -1:
            raise ValueError(f"Source publication date is in the future: {source_path}")
        if age_days > max_source_age_days:
            raise ValueError(
                f"Approved source is {age_days:.0f} days old; maximum is "
                f"{max_source_age_days}: {source_path}"
            )

        published_utc = published_at.isoformat().replace("+00:00", "Z")
        for sha256 in read_hashes(source_path):
            records_by_hash[sha256] = Record(
                sha256=sha256,
                malware_family=source["malware_family"],
                source=source["provider"],
                source_reference=source["reference"],
                source_commit=commit,
                published_utc=published_utc,
                confidence=source["confidence"],
            )

    records = sorted(
        records_by_hash.values(),
        key=lambda item: (item.published_utc, item.sha256),
        reverse=True,
    )[:max_hashes]
    if not records:
        raise ValueError("No hashes passed the approved-source policy")

    output_dir.mkdir(parents=True, exist_ok=True)
    write_if_changed(output_dir / "hashblock.csv", render_csv(records))
    write_if_changed(
        output_dir / "hashes_sha256.txt",
        "\n".join(record.sha256 for record in records) + "\n",
    )
    write_if_changed(
        output_dir / "hashes_sha256_comma.txt",
        ",".join(record.sha256 for record in records) + "\n",
    )
    print(f"Published {len(records)} high-confidence SHA-256 hashes")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path("config/sources.json"))
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("."))
    parser.add_argument(
        "--now",
        help="Optional ISO-8601 UTC time used for deterministic validation",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = (
        datetime.fromisoformat(args.now.replace("Z", "+00:00")).astimezone(timezone.utc)
        if args.now
        else datetime.now(timezone.utc)
    )
    try:
        return build(args.config, args.source_root, args.output_dir, now)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"Update failed safely: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
