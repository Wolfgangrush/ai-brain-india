# Changelog

## [0.1.3] — 2026-06-05 · Dual-mode disclosure refinement (with DPDP Section 8(5) + Section 5-7 cloud-mode clarification + BSA 2023 attorney-client privilege framing)

### Changed
- **README.md** — refined headline tagline, tier table rows (Local Ollama · DeepSeek · Claude/Gemini), and "Privacy posture (the honest version)" section to honestly disclose the dual-mode architecture (local-default · cloud-optional) and the role of the internalised Pseudonymisation Gateway as the structural privacy primitive when cloud mode is invoked.

  **DPDP Act 2023 is now framed dual-mode**:
  - Local Ollama tier: Section 8 not triggered (no transmission occurs)
  - Cloud tier: Section 8(5) reasonable-security-safeguards duty is supported by Gateway sanitisation (structural pseudonymisation = meaningful technical safeguard); Section 5-7 consent + lawful-basis duties remain practitioner's as Data Fiduciary — Gateway does NOT discharge them.
  - Section 8(5) + Section 17(2)(a) legal-proceeding exemption interaction acknowledged.

  **Attorney-client privilege** (Bharatiya Sakshya Adhiniyam 2023 Section 132 / Indian Evidence Act 1872 Section 126): pointed to Local Ollama tier as the safe default for privileged work; cloud mode is conditional on client engagement letter AI-disclosure + audit-log basis.

  **BCI Rule 36** (publicity/solicitation firewall): preserved as practitioner-responsibility independent of dual-mode privacy architecture.

  Prior wording overstated by treating local-only as architectural fact across all tiers; the architecture is in fact **local-default with cloud-optional + Gateway-sanitised cloud transmission**.

### Why this matters
An Indian solo advocate relying on the prior *"Your data stays on your laptop"* line who configured a cloud-LLM provider for client work would have been misled about the residual DPDP Section 5-7 Data Fiduciary obligations the Gateway supports but does NOT discharge. The refinement is honest disclosure; the Gateway as a privacy primitive is materially stronger than what most cloud-AI legal tools offer; the wedge for choosing this tool over commodity cloud AI is preserved.

### Unchanged
- All agents, drafting-plugin connector, tests, getting-started guides (11 Indian languages), and the Pseudonymisation Gateway itself are unchanged. This is a documentation + privacy-disclosure-honesty refinement, not a behavioural change.
