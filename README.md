# Bad Hashes

A cumulative SHA-256 blocklist maintained by a recurring Codex agent. It is
designed for two uses: a daily delta of newly verified hashes and a historical
database that can be imported years later.

## Download

- [`hashblock.csv`](hashblock.csv) - cumulative historical database with
  confirmation evidence and provenance.
- [`hashes_sha256_all.txt`](hashes_sha256_all.txt) - cumulative list, one hash
  per line.
- [`hashes_sha256_all_comma.txt`](hashes_sha256_all_comma.txt) - cumulative
  list in comma-separated SIEM copy/paste format.
- [`daily_hashes.csv`](daily_hashes.csv) - only hashes added in the latest
  daily review.
- [`daily_hashes_sha256.txt`](daily_hashes_sha256.txt) - latest daily delta,
  one hash per line.
- [`daily_hashes_sha256_comma.txt`](daily_hashes_sha256_comma.txt) - latest
  daily delta in comma-separated format.
- [`feed_status.json`](feed_status.json) - review status and counts.

## Inclusion policy

- SHA-256 file hashes only.
- Daily target: 30–50 new hashes when that many pass verification.
- No artificial cap on the cumulative database.
- Every row must name the malware family, source, source reference, and
  confirmation evidence.
- PUPs, adware, hacktools, keygens, miners, dual-use administration tools,
  filenames, fuzzy hashes, IPs, domains, and URLs are excluded.
- If fewer than 30 hashes meet the evidence standard, the agent publishes fewer
  rather than padding the daily file with weak indicators.

## Agent-maintained update schedule

A recurring Codex agent reviews the threat landscape every day at approximately
9:00 AM America/Los_Angeles time. It uses the MalwareBazaar recent SHA-256
export for intake, then checks individual sample records and analyst evidence
before publishing anything. ESET and PRODAFT research are used for
corroboration when available. Nothing is installed or scheduled on the
repository owner's computer.

The agent appends verified hashes to the cumulative files and replaces the daily
delta files. A failed or ambiguous review leaves the last known-good hash files
untouched. The complete decision policy is documented in
[`AGENT_POLICY.md`](AGENT_POLICY.md).

## Important limitation

An exact hash blocks one exact file. Malware operators frequently rebuild files,
which creates new hashes. This list is a focused defensive supplement, not a
replacement for antivirus, EDR, behavioral detection, or threat hunting.

If you believe a hash is a false positive, open an issue with the hash and the
reason it should be reviewed.
