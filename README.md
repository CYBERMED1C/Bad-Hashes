# Bad Hashes

A curated SHA-256 malware blocklist for defensive detection. The repository
provides a historical dataset and a latest daily delta, with provenance and
verification evidence for every published entry.

## Downloads

- [`hashblock.csv`](hashblock.csv) — cumulative database with malware family,
  source, evidence, and status.
- [`hashes_sha256_all.txt`](hashes_sha256_all.txt) — all active hashes,
  one per line.
- [`hashes_sha256_all_comma.txt`](hashes_sha256_all_comma.txt) — all active
  hashes in comma-separated SIEM copy/paste format.
- [`daily_hashes.csv`](daily_hashes.csv) — hashes added in the latest review,
  with provenance and evidence.
- [`daily_hashes_sha256.txt`](daily_hashes_sha256.txt) — latest daily delta,
  one hash per line.
- [`daily_hashes_sha256_comma.txt`](daily_hashes_sha256_comma.txt) — latest
  daily delta in comma-separated format.
- [`feed_status.json`](feed_status.json) — current review status and counts.

## Documentation

- [`AGENT_POLICY.md`](AGENT_POLICY.md) — evidence, inclusion, and maintenance
  rules.
- [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) — source attribution and
  licensing notices.

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
