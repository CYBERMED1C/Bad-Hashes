# Codex agent policy

This repository is reviewed and maintained by a recurring Codex agent. The
agent must favor confidence over volume and must never add hashes merely to make
the list appear active.

## Daily process

1. Research malware activity reported during the preceding 30 days.
2. Use original publications from established security research organizations.
3. Confirm that redistribution is permitted by an explicit license or an
   equally clear publisher statement.
4. Prefer malware families with evidence of broad or repeated current use.
5. Add only exact SHA-256 file hashes explicitly identified as malicious.
6. Reject ambiguous, suspicious-only, PUP, adware, hacktool, keygen, miner,
   dual-use administration tool, filename-only, fuzzy-hash, and network IOCs.
7. Retain provenance for every published hash in `hashblock.csv`.
8. Keep no more than 20 active hashes across the entire repository.
9. Keep `hashblock.csv`, `hashes_sha256.txt`, and
   `hashes_sha256_comma.txt` identical in membership.
10. Update `feed_status.json` and push one daily review commit. If no hash
    qualifies, do not modify the hash files.

## Required evidence

Each hash must have:

- a named malware family or operation;
- a direct reference to the analyst's publication;
- the source repository commit or publication date;
- a high-confidence malicious classification; and
- a source whose reuse terms permit republication.

No automated community submission is sufficient by itself. A second source may
be used for corroboration, but matching entries within the same provider's
ecosystem do not count as independent confirmation.

## Failure behavior

When source access, licensing, provenance, or maliciousness is unclear, the
agent must make no hash-list change. It records the failed review in
`feed_status.json` only when doing so would not misrepresent the feed as
successfully validated.
