"""Smoke test: MCP server module imports and the 2 new tools are reachable."""


def test_court_lookup_importable():
    from ailawfirm_india.mcp_tools.court_lookup import india_court_lookup

    assert callable(india_court_lookup)


def test_citation_validator_importable():
    from ailawfirm_india.mcp_tools.citation_validator import india_citation_validator

    assert callable(india_citation_validator)


def test_mcp_server_module_importable():
    """mcp_server.py should at minimum be importable without crashing."""
    import ailawfirm_india.mcp_server  # noqa: F401
