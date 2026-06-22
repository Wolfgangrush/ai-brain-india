"""
india_citation_validator MCP tool — v0.1.

Validates and parses Indian legal citations against 3 well-known formats:
- AIR (All India Reporter): e.g. "AIR 1973 SC 1461"
- SCC (Supreme Court Cases): e.g. "(2023) 4 SCC 121"
- SCC OnLine: e.g. "2024 SCC OnLine Bom 891"

v0.1: format validation + parsing only. v0.3+ adds lookup against
external databases.

PROVENANCE: TRAINED for citation formats (high-frequency, well-documented).
"""

import re
from ailawfirm_india.core.ontology import Citation


# Regex patterns — PROVENANCE: TRAINED
_AIR_PATTERN = re.compile(r"^AIR\s+(?P<year>\d{4})\s+(?P<court>[A-Z][A-Za-z]*)\s+(?P<page>\d+)$")
_SCC_PATTERN = re.compile(r"^\((?P<year>\d{4})\)\s+(?P<volume>\d+)\s+SCC\s+(?P<page>\d+)$")
_SCC_ONLINE_PATTERN = re.compile(
    r"^(?P<year>\d{4})\s+SCC\s+OnLine\s+(?P<court>[A-Z][A-Za-z]*)\s+(?P<serial>\d+)$"
)


def india_citation_validator(citation_string: str) -> dict:
    """Parse and validate an Indian legal citation.

    Args:
        citation_string: e.g. "AIR 1973 SC 1461" or "(2023) 4 SCC 121"

    Returns:
        dict serialization of Citation dataclass with:
        - raw: input string
        - format: 'AIR' | 'SCC' | 'SCC_ONLINE' | 'UNKNOWN'
        - year, court_or_reporter, volume_or_number, page_or_serial
        - valid: True if recognized format
        - parse_notes: optional diagnostic
    """
    if not isinstance(citation_string, str):
        return {
            "raw": str(citation_string),
            "format": "UNKNOWN",
            "valid": False,
            "parse_notes": "input was not a string",
        }

    s = citation_string.strip()

    # Try AIR
    m = _AIR_PATTERN.match(s)
    if m:
        c = Citation(
            raw=s,
            format="AIR",
            year=int(m.group("year")),
            court_or_reporter=m.group("court"),
            page_or_serial=int(m.group("page")),
            valid=True,
        )
        return _citation_to_dict(c)

    # Try SCC
    m = _SCC_PATTERN.match(s)
    if m:
        c = Citation(
            raw=s,
            format="SCC",
            year=int(m.group("year")),
            volume_or_number=int(m.group("volume")),
            page_or_serial=int(m.group("page")),
            court_or_reporter="SC",
            valid=True,
        )
        return _citation_to_dict(c)

    # Try SCC OnLine
    m = _SCC_ONLINE_PATTERN.match(s)
    if m:
        c = Citation(
            raw=s,
            format="SCC_ONLINE",
            year=int(m.group("year")),
            court_or_reporter=m.group("court"),
            page_or_serial=int(m.group("serial")),
            valid=True,
        )
        return _citation_to_dict(c)

    # No format matched
    return _citation_to_dict(
        Citation(
            raw=s,
            format="UNKNOWN",
            valid=False,
            parse_notes="did not match AIR, SCC, or SCC OnLine patterns",
        )
    )


def _citation_to_dict(c: Citation) -> dict:
    return {
        "raw": c.raw,
        "format": c.format,
        "year": c.year,
        "court_or_reporter": c.court_or_reporter,
        "volume_or_number": c.volume_or_number,
        "page_or_serial": c.page_or_serial,
        "valid": c.valid,
        "parse_notes": c.parse_notes,
    }
