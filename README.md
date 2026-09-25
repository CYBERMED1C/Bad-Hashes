# Bad Hashes

A small, conservative SHA-256 blocklist built from analyst-confirmed malware
research. This project intentionally favors confidence over volume.

## Download

- [`hashblock.csv`](hashblock.csv) - hashes with malware family, provenance,
  publication date, and source commit.
- [`hashes_sha256.txt`](hashes_sha256.txt) - one SHA-256 hash per line.
- [`hashes_sha256_comma.txt`](hashes_sha256_comma.txt) - the same hashes in a
  comma-separated copy/paste format.

## Inclusion policy

A hash is eligible only when all of the following are true:

- It is a full SHA-256 file hash.
- It comes from an explicitly licensed, named security research source.
- The source identifies the file as malware, not merely suspicious software.
- It is associated with an approved active malware family or operation.
- It is no more than 180 days old when admitted.
- The complete published list contains no more than 20 hashes.

Potentially unwanted applications, adware, hacktools, keygens, generic remote
administration tools, filenames, fuzzy hashes, IP addresses, domains, and URLs
are excluded.

SHA-256 is used instead of MD5 because it is the stronger and more portable
choice for modern blocklists.

## Update schedule

GitHub Actions checks the approved upstream source every day at approximately
9:17 AM America/Los_Angeles time. It creates a commit only when the resulting
hash list changes. A failed download or validation stops the update and leaves
the last known-good files untouched.

The initial feed contains ESET-confirmed Amadey and Stealc samples published as
part of Operation Endgame. See [`config/sources.json`](config/sources.json) for
the exact source and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for its
license.

## Important limitation

An exact hash blocks one exact file. Malware operators frequently rebuild their
files, which creates new hashes. This list is a focused defensive supplement,
not a replacement for antivirus, EDR, behavioral detection, or threat hunting.

If you believe a hash is a false positive, open an issue with the hash and the
reason it should be reviewed.
