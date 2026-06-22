"""Tests for ontology module — v0.1."""

from ailawfirm_india.core.ontology import (
    MatterType,
    IndianCourt,
    IndianStatute,
    BarCouncilRule,
    Matter,
    Citation,
)


def test_matter_type_has_pil():
    assert MatterType.PIL.value == "Public Interest Litigation"


def test_indian_court_has_bombay_hc_aurangabad():
    assert IndianCourt.HC_BOMBAY_AURANGABAD.value == "Bombay High Court Aurangabad Bench"


def test_indian_statute_includes_dpdp():
    assert IndianStatute.DPDP_2023.value == "Digital Personal Data Protection Act 2023"


def test_bci_rule_36_present():
    assert "Rule 36" in BarCouncilRule.RULE_36.value
    assert "soliciting" in BarCouncilRule.RULE_36.value.lower()


def test_no_duplicate_matter_type_values():
    values = [m.value for m in MatterType]
    assert len(values) == len(set(values)), "Duplicate MatterType values"


def test_no_duplicate_court_values():
    values = [c.value for c in IndianCourt]
    assert len(values) == len(set(values)), "Duplicate IndianCourt values"


def test_no_duplicate_statute_values():
    values = [s.value for s in IndianStatute]
    assert len(values) == len(set(values)), "Duplicate IndianStatute values"


def test_matter_dataclass_minimal():
    m = Matter(
        matter_id="WP-AURANGABAD-2026-001",
        matter_type=MatterType.WP,
        court=IndianCourt.HC_BOMBAY_AURANGABAD,
        short_title="Test v. State of Maharashtra",
    )
    assert m.matter_id == "WP-AURANGABAD-2026-001"
    assert m.matter_type == MatterType.WP
    assert m.court == IndianCourt.HC_BOMBAY_AURANGABAD
    assert m.parties_petitioner == []
    assert m.statutes_invoked == []


def test_citation_dataclass_minimal():
    c = Citation(raw="AIR 1973 SC 1461", format="AIR")
    assert c.raw == "AIR 1973 SC 1461"
    assert c.format == "AIR"
    assert c.valid is False  # default
