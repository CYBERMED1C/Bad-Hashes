# Bad Hashes

> **Repository health**
> - **Last push (UTC): 2026-09-25 16:01
> - **Overall health:** **PARTIAL** — published data is valid; the daily batch is below target because no additional hashes met the evidence standard.
> - **Validation:** **PASS** — 14 cumulative hashes and 14 daily hashes; CSV, line-separated, and comma-separated formats are synchronized.
> - **Latest archive:** [2026/09/25](2026/09/25)

A curated SHA-256 malware blocklist for defensive detection. The repository
provides a historical dataset and dated daily archives, with provenance and
verification evidence for every published entry.

## Downloads

- [`hashblock.csv`](hashblock.csv) — cumulative database with malware family,
  source, evidence, and status.
- [`hashes_sha256_all.txt`](hashes_sha256_all.txt) — all active hashes,
  one per line.
- [`hashes_sha256_all_comma.txt`](hashes_sha256_all_comma.txt) — all active
  hashes in comma-separated SIEM copy/paste format.
- [`2026/09/25/daily_hashes.csv`](2026/09/25/daily_hashes.csv) — daily
  archive with provenance and evidence.
- [`2026/09/25/daily_hashes_sha256.txt`](2026/09/25/daily_hashes_sha256.txt)
  — daily archive, one hash per line.
- [`2026/09/25/daily_hashes_sha256_comma.txt`](2026/09/25/daily_hashes_sha256_comma.txt)
  — daily archive in comma-separated SIEM format.
- [`feed_status.json`](feed_status.json) — current review status and counts.

## Archive structure

Each review date gets its own day folder inside the year and month:

```
2026/
└── 09/
    ├── 24/
    ├── 25/
    ├── 26/
    └── ...
```

The full pattern is `YYYY/MM/DD/`.

## Inclusion policy

- Exact SHA-256 file hashes only.
- Daily target: 30–50 new hashes when that many meet the evidence standard.
- No artificial cap on the cumulative database.
- Every row must name the malware family, source, source reference, and
  confirmation evidence.
- PUPs, adware, hacktools, keygens, miners, dual-use administration tools,
  filenames, fuzzy hashes, IPs, domains, and URLs are excluded.
- If fewer than 30 hashes meet the evidence standard, the daily file contains
  fewer rather than weak or unverified indicators.

## Important limitation

An exact hash blocks one exact file. Malware operators frequently rebuild files,
which creates new hashes. This list is a focused defensive supplement, not a
replacement for antivirus, EDR, behavioral detection, or threat hunting.
