"""
Ontology module — AI Brain · India · Solo · v0.1

Defines the core enums for Indian legal practice:
- MatterType: case file types
- IndianCourt: court hierarchy
- IndianStatute: statute registry slots
- BarCouncilRule: BCI rule references (Rule 36 firewall)

v0.1 = shape only (enums + empty containers). Real content (statute text,
court pecuniary limits, subject-matter rules) lands in v0.2+ with CITED
provenance in KNOWLEDGE_PROVENANCE.md.

PROVENANCE: TRAINED for enum values (high-frequency, low-risk).
PROVENANCE: STUB for any associated metadata in v0.1.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class MatterType(Enum):
    """Indian legal matter type codes — non-exhaustive v0.1 set."""

    # Original civil
    WP = "Writ Petition"  # constitutional, HC/SC
    PIL = "Public Interest Litigation"
    SLP = "Special Leave Petition"  # SC only, Art 136
    CRA = "Criminal Appeal"
    CRP = "Civil Revision Petition"
    MA = "Misc Application"
    CA = "Civil Appeal"
    OA = "Original Application"  # tribunals
    AB = "Anticipatory Bail"
    NBW = "Non-Bailable Warrant cancellation"
    EXE = "Execution Petition"
    SUIT = "Civil Suit"

    # Tribunal / specialised
    DRT_OA = "DRT Original Application"
    DRAT_APPEAL = "DRAT Appeal"
    NCLT_CP = "NCLT Company Petition"
    NCLAT_APPEAL = "NCLAT Appeal"

    # Other
    OTHER = "Other (specify in description)"


class IndianCourt(Enum):
    """Indian court hierarchy — v0.1 stubs only. PROVENANCE: TRAINED."""

    SC_INDIA = "Supreme Court of India (New Delhi)"
    HC_BOMBAY_MUMBAI = "Bombay High Court (Mumbai)"
    HC_BOMBAY_AURANGABAD = "Bombay High Court Aurangabad Bench"
    DISTRICT_AURANGABAD = "District Court Aurangabad"
    DRT_AURANGABAD = "Debt Recovery Tribunal Aurangabad"
    OTHER = "Other (specify)"


class IndianStatute(Enum):
    """Indian statute registry slots — v0.1 references only.
    PROVENANCE: TRAINED for names + years; STUB for text content (v0.2+)."""

    DPDP_2023 = "Digital Personal Data Protection Act 2023"
    IT_ACT_2000 = "Information Technology Act 2000"
    CPC_1908 = "Code of Civil Procedure 1908"
    CRPC_1973 = "Code of Criminal Procedure 1973"
    BNSS_2023 = "Bharatiya Nagarik Suraksha Sanhita 2023"
    IPC_1860 = "Indian Penal Code 1860"
    BNS_2023 = "Bharatiya Nyaya Sanhita 2023"
    CONTRACT_ACT_1872 = "Indian Contract Act 1872"
    EVIDENCE_ACT_1872 = "Indian Evidence Act 1872"
    BSA_2023 = "Bharatiya Sakshya Adhiniyam 2023"
    BCI_RULES_1975 = "Bar Council of India Rules 1975"
    NI_ACT_1881 = "Negotiable Instruments Act 1881"
    SARFAESI_2002 = "SARFAESI Act 2002"
    IBC_2016 = "Insolvency and Bankruptcy Code 2016"


class BarCouncilRule(Enum):
    """BCI rule references — Rule 36 firewall is load-bearing.
    PROVENANCE: TRAINED + publisher-cited in palace (high-confidence)."""

    RULE_36 = "BCI Rules 1975 Rule 36 — no soliciting work; no advertising"
    # Other BCI rules added as needed in v0.2+


@dataclass
class Matter:
    """A single matter (case file) — v0.1 shape only.

    PROVENANCE: STUB — full matter lifecycle (hearings, orders, drafts,
    deadlines, billing) lands in v0.2+ via separate modules.
    """

    matter_id: str
    matter_type: MatterType
    court: IndianCourt
    short_title: str
    parties_petitioner: list[str] = field(default_factory=list)
    parties_respondent: list[str] = field(default_factory=list)
    statutes_invoked: list[IndianStatute] = field(default_factory=list)
    filed_date: Optional[str] = None  # ISO YYYY-MM-DD; v0.2+ uses datetime
    status_note: Optional[str] = None  # free-text v0.1; v0.2+ enum


@dataclass
class Citation:
    """A parsed Indian legal citation — produced by citation_validator MCP tool."""

    raw: str
    format: str  # 'AIR' | 'SCC' | 'SCC_ONLINE' | 'UNKNOWN'
    year: Optional[int] = None
    court_or_reporter: Optional[str] = None
    volume_or_number: Optional[int] = None
    page_or_serial: Optional[int] = None
    valid: bool = False
    parse_notes: Optional[str] = None
