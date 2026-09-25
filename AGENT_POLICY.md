# Codex agent policy

This repository is reviewed and maintained by a recurring Codex agent. The
agent must favor confidence over volume and must never add hashes merely to make
the list appear active.

## Daily process

1. Start with the MalwareBazaar recent SHA-256 export, then inspect candidate
   sample records individually.
2. Use original publications from established security research organizations
   for family and campaign context.
3. Confirm that redistribution is permitted by the source's current terms.
4. Prefer malware families with evidence of broad, repeated, or currently
   active use.
5. Add only exact SHA-256 file hashes explicitly identified as malicious.
6. Require a named malware family plus at least one concrete confirmation signal
   such as a vendor/sandbox verdict, named analyst detection, YARA/ClamAV
   detection, or a linked research report.
7. Reject ambiguous, suspicious-only, PUP/adware, hacktool, keygen, miner,
   dual-use administration tool, filename-only, fuzzy-hash, and network IOCs.
8. Retain provenance and confirmation evidence for every published hash in
   `hashblock.csv`.
9. Add 30–50 new hashes to the daily delta when that many pass. Never pad the
   daily file with weak or unverified indicators.
10. Append verified hashes to the cumulative files; do not remove historical
    entries except through an explicit `revoked` status with a reason.
11. Keep `hashblock.csv`, `hashes_sha256_all.txt`, and
    `hashes_sha256_all_comma.txt` identical in cumulative membership. Keep the
    three daily files identical in daily membership.
12. Update `feed_status.json` and push one daily review commit.

## Required evidence

Each hash must have:

- a named malware family or operation;
- a direct reference to the analyst's publication;
- the source repository commit or publication date;
- a high-confidence malicious classification;
- a specific confirmation signal beyond mere presence in a community feed; and
- a source whose reuse terms permit republication.

No automated community submission is sufficient by itself. A second source may
be used for corroboration, but matching entries within the same provider's
ecosystem do not count as independent confirmation.

## Failure behavior

When source access, licensing, provenance, or maliciousness is unclear, the
agent must make no hash-list change. It records the failed review in
`feed_status.json` only when doing so would not misrepresent the feed as
successfully validated.
