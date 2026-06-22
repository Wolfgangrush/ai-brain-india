"""
india_court_lookup MCP tool — v0.1.

Resolves a court name (fuzzy) to a structured court info dict.
v0.1 covers 5 court stubs. Pecuniary limits and subject-matter rules
are STUBs (PROVENANCE: STUB — v0.2+ with citations).

PROVENANCE: TRAINED for court existence + locations (high-frequency facts).
"""

from typing import Optional
from ailawfirm_india.core.ontology import IndianCourt


# v0.1 stub data. v0.2+ replaces with CITED content.
_COURT_INFO: dict[IndianCourt, dict] = {
    IndianCourt.SC_INDIA: {
        "name": "Supreme Court of India",
        "location": "New Delhi",
        "tier": "apex",
        "jurisdiction_class": "original + appellate + writ + advisory",
        "procedural_code": "Supreme Court Rules 2013",
        "pecuniary_limit": None,  # PROVENANCE: STUB
    },
    IndianCourt.HC_BOMBAY_MUMBAI: {
        "name": "Bombay High Court (Principal Seat)",
        "location": "Mumbai",
        "tier": "high_court",
        "jurisdiction_class": "original + appellate + writ + supervisory",
        "procedural_code": "Bombay High Court (Appellate Side) Rules 1960",
        "pecuniary_limit": None,  # PROVENANCE: STUB
    },
    IndianCourt.HC_BOMBAY_AURANGABAD: {
        "name": "Bombay High Court Aurangabad Bench",
        "location": "Aurangabad, Maharashtra",
        "tier": "high_court_bench",
        "jurisdiction_class": "appellate + writ + supervisory (Vidarbha region)",
        "procedural_code": "Bombay High Court (Appellate Side) Rules 1960",
        "pecuniary_limit": None,  # PROVENANCE: STUB
    },
    IndianCourt.DISTRICT_AURANGABAD: {
        "name": "District Court Aurangabad",
        "location": "Aurangabad, Maharashtra",
        "tier": "district",
        "jurisdiction_class": "original civil + criminal sessions",
        "procedural_code": "CPC 1908 + CrPC/BNSS",
        "pecuniary_limit": None,  # PROVENANCE: STUB
    },
    IndianCourt.DRT_AURANGABAD: {
        "name": "Debt Recovery Tribunal Aurangabad",
        "location": "Aurangabad, Maharashtra",
        "tier": "tribunal",
        "jurisdiction_class": "DRT Act 1993 — bank debt recovery > ₹20 lakh",
        "procedural_code": "DRT Procedure Rules 1993",
        "pecuniary_limit": "₹20 lakh and above",
    },
}


def _fuzzy_match_court(query: str) -> Optional[IndianCourt]:
    """Case-insensitive match on court enum values and names.
    Checks for full query substring, then for all individual words.
    Returns the first match or None."""
    q = query.lower().strip()
    if not q:
        return None
    q_words = q.split()
    for court in IndianCourt:
        text = (court.value + " " + court.name).lower()
        if q in text:
            return court
        if q_words and all(w in text for w in q_words):
            return court
    return None


def india_court_lookup(court_name: str) -> dict:
    """Resolve a court name (fuzzy) to structured court info.

    Args:
        court_name: free-text court name (e.g. "Bombay HC Aurangabad", "supreme court")

    Returns:
        dict with keys: name, location, tier, jurisdiction_class,
        procedural_code, pecuniary_limit, matched_enum (str), found (bool).
        If no match: {"found": False, "query": <input>}.
    """
    if not isinstance(court_name, str):
        return {"found": False, "error": "court_name must be a string"}

    matched = _fuzzy_match_court(court_name)
    if matched is None or matched not in _COURT_INFO:
        return {"found": False, "query": court_name}

    info = dict(_COURT_INFO[matched])
    info["matched_enum"] = matched.name
    info["found"] = True
    return info
