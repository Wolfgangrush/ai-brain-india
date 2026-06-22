# KNOWLEDGE_PROVENANCE — AI Brain · India · Solo · v0.1

This file maps every domain claim in the codebase to its source. The purpose is to prevent the silent introduction of hallucinated legal facts.

## Provenance categories

- **TRAINED** — the model's training corpus. Reliable for high-frequency well-documented facts (e.g. "Supreme Court of India sits in New Delhi"); UNRELIABLE for low-frequency niche facts (recent statutes, recent amendments, specific judge dispositions). Flag with `# PROVENANCE: TRAINED` in code.
- **CITED** — backed by a specific source document in `docs/sources/` that the verifier can inspect. Flag with `# PROVENANCE: CITED:<filename>:<page>` in code.
- **STUB** — placeholder for v0.2+ where real content lands. Flag with `# PROVENANCE: STUB — fill in v0.2`.

## v0.1 claim ledger

### Court hierarchy (in `ailawfirm_india/ontology.py` — `IndianCourt` enum)

| Claim | Provenance |
|---|---|
| Supreme Court of India exists | TRAINED (high-frequency) |
| High Courts of 25 states/UTs exist | TRAINED — count may be stale post-2024 reorganizations · NEEDS PUBLISHER VERIFY |
| Bombay HC has benches at Mumbai · your city · Aurangabad · Panaji | TRAINED — the publisher practices at your city bench, can verify |
| Pecuniary limits per court tier | STUB — NOT included in v0.1 · v0.2+ requires citation |
| Subject-matter jurisdiction rules | STUB — NOT included in v0.1 |

### Statute registry (in `ailawfirm_india/ontology.py` — `IndianStatute` enum)

| Statute | Provenance |
|---|---|
| DPDP Act 2023 | TRAINED + publisher-studied — text not embedded in v0.1 |
| IT Act 2000 | TRAINED — text not embedded in v0.1 |
| CPC 1908 | TRAINED — text not embedded in v0.1 |
| CrPC 1973 / BNSS 2023 | TRAINED — BNSS is recent · NEEDS PUBLISHER VERIFY which is in force when |
| IPC 1860 / BNS 2023 | TRAINED — BNS is recent · NEEDS PUBLISHER VERIFY |
| Contract Act 1872 | TRAINED |
| Evidence Act 1872 / BSA 2023 | TRAINED — BSA is recent · NEEDS PUBLISHER VERIFY |
| BCI Rules 1975 (Rule 36) | TRAINED + publisher-cited multiple times in palace · high-confidence |

### Citation formats (in `ailawfirm_india/mcp_tools/citation_validator.py`)

| Format | Provenance |
|---|---|
| AIR (All India Reporter) — `AIR YYYY SC NNNN` / `AIR YYYY <HC> NNNN` | TRAINED — high-frequency, low-risk |
| SCC (Supreme Court Cases) — `(YYYY) N SCC NNN` | TRAINED — high-frequency |
| SCC OnLine — `YYYY SCC OnLine <Court> NNNN` | TRAINED — high-frequency |

## Verification protocol

Before any v0.1 → v0.2 transition, the publisher reviews this file. Items flagged `NEEDS PUBLISHER VERIFY` are checked against authoritative sources (Bare Acts, India Code, official court websites). Items flagged `STUB` get filled with `CITED` content.

## What this file is NOT

- Not a comprehensive legal database — that's a downstream goal.
- Not a substitute for a lawyer's own statutory research — this codebase MUST NOT be presented to end users as a source of legal advice. Bar Council Rule 36 firewall.
- Not a fixed document — every change in domain content must update this file in the same commit.
