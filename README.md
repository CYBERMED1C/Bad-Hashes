# Bad Hashes

A small, conservative SHA-256 blocklist built from analyst-confirmed malware
research. This project intentionally favors confidence over volume.

## Download

- [`hashblock.csv`](hashblock.csv) - hashes with malware family, provenance,
  publication date, and source commit.
- [`hashes_sha256.txt`](hashes_sha256.txt) - one SHA-256 hash per line.
- [`hashes_sha256_comma.txt`](hashes_sha256_comma.txt) - the same hashes in a
  comma-separated copy/paste format.
- [`feed_status.json`](feed_status.json) - last successful daily check, current
  hash count, and source commit recorded by the agent.

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

## Agent-maintained update schedule

A recurring Codex agent reviews the threat landscape every day at approximately
9:00 AM America/Los_Angeles time. The agent researches current malware activity,
checks the original analyst publication and reuse license, validates every hash,
updates the files, and pushes the result to GitHub. Nothing is installed or
scheduled on the repository owner's computer.

The agent updates `feed_status.json` after every successful review, even when no
new hash qualifies. A failed or ambiguous review leaves the last known-good hash
files untouched. The complete decision policy is documented in
[`AGENT_POLICY.md`](AGENT_POLICY.md).

The initial feed contains ESET-confirmed Amadey and Stealc samples published as
part of Operation Endgame. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)
for the source license.

## Important limitation

An exact hash blocks one exact file. Malware operators frequently rebuild their
files, which creates new hashes. This list is a focused defensive supplement,
not a replacement for antivirus, EDR, behavioral detection, or threat hunting.

If you believe a hash is a false positive, open an issue with the hash and the
reason it should be reviewed.
