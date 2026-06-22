"""
Intent enum for the AI Brain India brain layer.

The brain classifies incoming user requests into one of these intents,
then routes to the matching agent. Patterned after Brain's
brain_brain.py 7-shape classifier (TASK/PROJECT/PERSON/etc).

PROVENANCE: STUB — v0.2+ will add Ollama-based classification.
v0.1 uses rule-based keyword matching (see classifier.py).
"""

from enum import Enum


class Intent(Enum):
    """User request intents for the legal-practice domain."""

    MATTER_UPDATE = "matter_update"  # new hearing, order received, status change
    CITATION_LOOKUP = "citation_lookup"  # parse / validate / look up a citation
    COURT_QUERY = "court_query"  # court info, jurisdiction question
    DRAFTING_NEED = "drafting_need"  # needs drafting help (Wolfgang_rush plugins)
    DEADLINE_CHECK = "deadline_check"  # limitation / hearing-date question
    CLIENT_COMM = "client_comm"  # client communication question or update
    COMPLIANCE_FLAG = "compliance_flag"  # Rule 36 / DPDP / ethics concern
    UNKNOWN = "unknown"  # fallback


# Routing table: intent → agent module name
AGENT_FOR_INTENT: dict[Intent, str] = {
    Intent.MATTER_UPDATE: "matter_agent",
    Intent.CITATION_LOOKUP: "citation_agent",
    Intent.COURT_QUERY: "court_agent",
    Intent.DRAFTING_NEED: "drafting_agent",
    Intent.DEADLINE_CHECK: "deadline_agent",
    Intent.CLIENT_COMM: "matter_agent",  # v0.1: client comm rolls into matter; split in v0.2+
    Intent.COMPLIANCE_FLAG: "compliance_agent",
    Intent.UNKNOWN: "matter_agent",  # safe default
}
