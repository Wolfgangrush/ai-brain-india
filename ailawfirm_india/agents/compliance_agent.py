"""
compliance_agent — BCI Rule 36 firewall + DPDP compliance check (v0.1 skeleton).

v0.1: detects the Rule 36 / DPDP keyword class + returns a structured warning.
v0.2+: full compliance check pipeline.

PROVENANCE: TRAINED for keyword set; STUB for compliance logic itself.
"""

from ailawfirm_india.core.ontology import BarCouncilRule


def handle(payload: str) -> dict:
    p = payload.lower()
    flags = []
    if any(k in p for k in ["solicit", "advertis", "promot"]):
        flags.append(
            {
                "rule": BarCouncilRule.RULE_36.value,
                "concern": "potential Rule 36 violation (solicitation / advertising)",
            }
        )
    if "dpdp" in p or "personal data" in p or "data fiduciary" in p:
        flags.append(
            {
                "rule": "DPDP Act 2023",
                "concern": "DPDP compliance check needed (v0.2+ real logic)",
            }
        )
    return {
        "agent": "compliance_agent",
        "status": "v0.1 — keyword-flag firewall only",
        "flags": flags,
        "note": "full compliance pipeline lands in v0.2+",
    }
