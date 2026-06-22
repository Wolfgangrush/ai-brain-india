"""
drafting_agent — invokes Wolfgang_rush drafting plugins (v0.1 stub).

v0.1: returns a placeholder pointing to the Wolfgang_rush plugin family.
v0.2+: detects the matter type + invokes the matching plugin.

PROVENANCE: STUB — real Wolfgang_rush plugin integration in v0.2+.
"""


def handle(payload: str) -> dict:
    return {
        "agent": "drafting_agent",
        "status": "v0.1 stub",
        "payload_received": payload,
        "note": "drafting is provided by the Wolfgang_rush plugin family — "
        "integration lands in v0.2+",
    }
