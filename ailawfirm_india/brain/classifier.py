"""
Brain classifier — rule-based intent detection (v0.1).

v0.1 strategy: simple keyword matching. Fast, deterministic, no LLM cost.
v0.2+ upgrade path: replace _RULES with an Ollama-based classifier
(small 7B model, ~5GB) following the brain_brain.py pattern.

PROVENANCE: TRAINED for keyword set (high-frequency legal terms).
"""

from ailawfirm_india.brain.intents import Intent


# Keyword-to-intent map. v0.1 is intentionally simple.
# Order matters — first match wins.
_RULES: list[tuple[list[str], Intent]] = [
    (
        ["citation", "air ", "scc ", "manupatra", "cite", "cited", "indiankanoon"],
        Intent.CITATION_LOOKUP,
    ),
    (
        [
            "court",
            "jurisdiction",
            "pecuniary",
            "bench",
            "tribunal",
            " hc ",
            " hc.",
            "high court",
            "supreme court",
            "district court",
            "drt",
            "nclt",
            "ncdrc",
            "nclat",
            "drat",
        ],
        Intent.COURT_QUERY,
    ),
    (
        [
            "draft",
            "drafting",
            "petition",
            "reply",
            "rejoinder",
            "affidavit",
            "plaint",
            "written statement",
        ],
        Intent.DRAFTING_NEED,
    ),
    (
        ["deadline", "limitation", "due date", "hearing date", "next date", "limitation period"],
        Intent.DEADLINE_CHECK,
    ),
    (
        ["client said", "client called", "client wants", "client emailed", "client confirmed"],
        Intent.CLIENT_COMM,
    ),
    (
        ["rule 36", "bci", "dpdp", "ethics", "compliance", "solicit", "advertis", "rule 35"],
        Intent.COMPLIANCE_FLAG,
    ),
    (["matter", "hearing", "order received", "argued", "filed"], Intent.MATTER_UPDATE),
]


def classify(text: str) -> Intent:
    """Classify the intent of a user request via keyword match.

    v0.1: rule-based. v0.2+: Ollama-classified.

    Args:
        text: free-text user request

    Returns:
        Intent enum value
    """
    if not isinstance(text, str) or not text.strip():
        return Intent.UNKNOWN

    t = text.lower()
    for keywords, intent in _RULES:
        if any(kw in t for kw in keywords):
            return intent
    return Intent.UNKNOWN
