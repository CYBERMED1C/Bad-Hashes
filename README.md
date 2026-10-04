# Bad Hashes

## Live status

🟢 Operational

**Last push:** 2026-10-04 16:07 UTC  
**Overall health:** Healthy

A curated SHA-256 malware blocklist for defensive detection. The repository
provides a historical dataset and dated daily archives, with provenance and
verification evidence for every published entry.

## Downloads

Current cumulative weekly bucket:

- [`2026/cumulative-hashes/10/week-1/hashblock.csv`](2026/cumulative-hashes/10/week-1/hashblock.csv) — CSV records added during October week 1, with malware family, source, evidence, and status.
- [`2026/cumulative-hashes/10/week-1/hashes_sha256.txt`](2026/cumulative-hashes/10/week-1/hashes_sha256.txt) — active hashes from October week 1, one per line.
- [`2026/cumulative-hashes/10/week-1/hashes_sha256_comma.txt`](2026/cumulative-hashes/10/week-1/hashes_sha256_comma.txt) — active October week 1 hashes in comma-separated SIEM copy/paste format.

Latest daily archive:

- [`2026/10/04/daily_hashes.csv`](2026/10/04/daily_hashes.csv) — daily archive with provenance and evidence.
- [`2026/10/04/daily_hashes_sha256.txt`](2026/10/04/daily_hashes_sha256.txt) — daily archive, one hash per line.
- [`2026/10/04/daily_hashes_sha256_comma.txt`](2026/10/04/daily_hashes_sha256_comma.txt) — daily archive in comma-separated SIEM format.

## Cumulative weekly organization

Inside each year folder, the cumulative collection is divided into small weekly buckets instead of one continuously growing root file. Together, every weekly bucket forms the complete cumulative database.

```
2026/
├── cumulative-hashes/
│   ├── 09/
│   │   ├── week-4/
│   │   └── week-5/
│   └── 10/
│       └── week-1/
└── 10/
    └── 04/  (daily archive)
```

Each weekly folder contains a full CSV plus line-separated and comma-separated SHA-256 blocklists. Weeks are assigned by the UTC `added_utc` date:

- `week-1`: days 1–7
- `week-2`: days 8–14
- `week-3`: days 15–21
- `week-4`: days 22–28
- `week-5`: days 29 through the end of the month

For example, hashes added on October 3 go into `2026/cumulative-hashes/10/week-1/`, while hashes added on November 10 go into `2026/cumulative-hashes/11/week-2/`. Existing hashes never move between buckets.

## Daily archive structure

Each review date also keeps its own daily folder inside the year and month:

```
2026/
├── 09/
│   ├── 24/
│   ├── 25/
│   └── ...
└── 10/
    ├── 01/
    ├── 02/
    ├── 03/
    └── 04/
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
