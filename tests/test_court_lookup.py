"""Tests for india_court_lookup MCP tool — v0.1."""

from ailawfirm_india.mcp_tools.court_lookup import india_court_lookup


def test_lookup_supreme_court_exact():
    r = india_court_lookup("Supreme Court of India")
    assert r["found"] is True
    assert r["location"] == "New Delhi"
    assert r["tier"] == "apex"


def test_lookup_supreme_court_fuzzy():
    r = india_court_lookup("supreme court")
    assert r["found"] is True
    assert r["matched_enum"] == "SC_INDIA"


def test_lookup_bombay_hc_aurangabad():
    r = india_court_lookup("Aurangabad Bench")
    assert r["found"] is True
    assert "Vidarbha" in r["jurisdiction_class"]


def test_lookup_drt_aurangabad():
    r = india_court_lookup("DRT Aurangabad")
    assert r["found"] is True
    assert r["tier"] == "tribunal"
    assert r["pecuniary_limit"] == "₹20 lakh and above"


def test_lookup_unknown_returns_not_found():
    r = india_court_lookup("Mars Family Court")
    assert r["found"] is False
    assert r["query"] == "Mars Family Court"


def test_lookup_empty_string():
    r = india_court_lookup("")
    assert r["found"] is False


def test_lookup_non_string_input():
    r = india_court_lookup(12345)
    assert r["found"] is False
    assert "error" in r
