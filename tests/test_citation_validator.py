"""Tests for india_citation_validator MCP tool — v0.1."""

from ailawfirm_india.mcp_tools.citation_validator import india_citation_validator


# Valid AIR
def test_air_supreme_court_valid():
    r = india_citation_validator("AIR 1973 SC 1461")
    assert r["valid"] is True
    assert r["format"] == "AIR"
    assert r["year"] == 1973
    assert r["court_or_reporter"] == "SC"
    assert r["page_or_serial"] == 1461


def test_air_bombay_high_court_valid():
    r = india_citation_validator("AIR 2020 Bom 234")
    assert r["valid"] is True
    assert r["format"] == "AIR"
    assert r["year"] == 2020
    assert r["court_or_reporter"] == "Bom"


# Valid SCC
def test_scc_valid():
    r = india_citation_validator("(2023) 4 SCC 121")
    assert r["valid"] is True
    assert r["format"] == "SCC"
    assert r["year"] == 2023
    assert r["volume_or_number"] == 4
    assert r["page_or_serial"] == 121


# Valid SCC OnLine
def test_scc_online_bombay_valid():
    r = india_citation_validator("2024 SCC OnLine Bom 891")
    assert r["valid"] is True
    assert r["format"] == "SCC_ONLINE"
    assert r["year"] == 2024
    assert r["court_or_reporter"] == "Bom"
    assert r["page_or_serial"] == 891


def test_scc_online_delhi_valid():
    r = india_citation_validator("2025 SCC OnLine Del 1024")
    assert r["valid"] is True
    assert r["court_or_reporter"] == "Del"


# Invalid / unknown
def test_unknown_format_invalid():
    r = india_citation_validator("Foo Bar 2023 Baz")
    assert r["valid"] is False
    assert r["format"] == "UNKNOWN"


def test_empty_string_invalid():
    r = india_citation_validator("")
    assert r["valid"] is False


def test_non_string_input_invalid():
    r = india_citation_validator(12345)
    assert r["valid"] is False
    assert "not a string" in r["parse_notes"]


def test_air_missing_court_invalid():
    r = india_citation_validator("AIR 1973 1461")
    assert r["valid"] is False


def test_scc_missing_parens_invalid():
    r = india_citation_validator("2023 4 SCC 121")
    assert r["valid"] is False
