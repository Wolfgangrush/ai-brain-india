# SCOPE — AI Brain · India · Solo · v0.1

## In scope (v0.1 must-haves)

- [x] Forked from brain-3.0.0 (MIT)
- [x] Package renamed to `ailawfirm_india`
- [x] pyproject.toml v0.1.0 with India Solo metadata
- [x] README positioned for Indian solo advocates, the local memory layer credited
- [x] SCOPE.md (this file)
- [x] KNOWLEDGE_PROVENANCE.md (hallucination firewall skeleton)
- [x] `ontology.py` — Indian matter types, court hierarchy enums, statute registry slots
- [x] MCP tool 1: `india_court_lookup` (5 court stubs)
- [x] MCP tool 2: `india_citation_validator` (3 citation formats)
- [x] Test suite covering ontology + both MCP tools
- [x] MCP server wired with the 2 new tools
- [x] All tests passing
- [x] Local commits clean

## Explicitly out of scope (NOT v0.1)

- [ ] Firm mode (multi-advocate, roles, billing) — v0.2+
- [ ] Real statute text (DPDP Act, IT Act, CPC, etc.) — needs source PDFs · v0.2+
- [ ] Drafting templates — these live in the Wolfgang_rush plugin family · separate repo
- [ ] Citation lookup against actual databases (Manupatra, SCC Online, IndianKanoon) — v0.3+
- [ ] Matter calendar / deadline tracker — v0.2+
- [ ] Client billing module — v0.2+
- [ ] GitHub publish — requires publisher verification + decision · post-v0.1
- [ ] Production deployment — requires hardening · post-v0.1
- [ ] UI (terminal or web) — beyond CLI stubs · post-v0.1
- [ ] Internationalization (Marathi/Hindi UI strings) — post-v0.1
- [ ] Cloud sync — explicitly anti-goal · local-first by design
- [ ] AI generation of legal advice — Bar Council Rule 36 firewall · forbidden permanently

## Verification path

v0.1 is verified by the publisher (Rushikesh R. Mahajan) before any GitHub publish.

## Falsification

If v0.1 cannot achieve all "in scope" items in a single DeepSeek build session of < 90 minutes, the scope or the plan is wrong. Halt and report — do not pad the scope to declare victory.
