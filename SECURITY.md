# SECURITY — AI Brain · India

## Reporting a vulnerability

If you discover a security vulnerability in AI Brain — India, please report it via one of:

1. **GitHub Security Advisories** (preferred) at: https://github.com/Wolfgangrush/ai-law-firm-india/security/advisories/new

2. **Private email** to: advrushikeshravindramahajan@gmail.com

Please do NOT post vulnerabilities to public GitHub Issues.

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact (severity assessment)
- Any suggested mitigation
- Whether you wish to be publicly credited

We aim to acknowledge reports within 72 hours and provide an initial assessment within 7 days.

## Scope

### Vulnerabilities in scope

- Code-execution vulnerabilities (path traversal · command injection · pickle deserialization · YAML/JSON unsafe loading · etc.)
- Sensitive-data exposure (config-file world-readable · credentials in logs · cached API keys in version-control · etc.)
- Local privilege escalation via tool usage
- Cryptographic weaknesses in any signing or encryption layer
- Dependency-injection vulnerabilities that affect the Software's behaviour
- Authentication or authorization bypass (where applicable)
- Insecure default configurations

### Out of scope

- Vulnerabilities in upstream dependencies — report to those projects directly (we will track + patch)
- Vulnerabilities in cloud AI vendors (Anthropic · OpenAI · Google · DeepSeek · etc.) — report to those vendors directly
- Social-engineering attacks against users
- Physical access attacks against the user's device
- Issues that require the user to have already lost root or admin access

## Disclosure policy

We follow **coordinated disclosure**:

- We will not disclose the vulnerability publicly until a fix is released or 90 days pass, whichever is sooner
- We will credit the reporter in the CHANGELOG and security advisory (unless they prefer anonymity)
- For confirmed vulnerabilities meeting NIST CVSS criteria, we will request a CVE through GitHub's CVE Numbering Authority
- We do NOT offer monetary bug bounties at this time (we are an open-source project with no revenue)

## Security hygiene practices

The Software's published codebase follows these practices:

- Dependencies pinned in `requirements.txt`
- Quarterly `pip-audit` review (publisher-side)
- No `eval` · no `exec` · no unsafe pickle / YAML / JSON deserialization
- All user input filtered before crossing tool/OS boundary
- File paths normalized to prevent path traversal (`os.path.normpath` + boundary checks)
- Subprocess calls audited and use explicit argument lists (never `shell=True` with user input)
- Configuration files written with restrictive permissions (file mode 0600 for sensitive configs)
- No hardcoded credentials, API keys, or secrets in the codebase

## User-side security recommendations

While the Software's local-first architecture closes many vectors at the design layer, users should also:

1. **Encrypt your device** — FileVault (macOS), BitLocker (Windows), LUKS (Linux). The Software stores matter data and configuration on disk; device encryption is the first defense.
2. **Strong device authentication** — biometric or strong passphrase.
3. **Backup discipline** — regular encrypted backups to a separate drive or service.
4. **Cloud API key management** — if you opt into cloud mode, treat API keys as confidential credentials. Do not commit them to version control. Use environment variables or a password manager.
5. **Audit your dependencies** — periodically run `pip list --outdated` and update vulnerable libraries.
6. **Network awareness** — if you handle particularly sensitive client matters, consider an air-gapped workstation for those matters.

## Past advisories

(None as of v0.1)

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §3.V11 (Security Vulnerability). Playbook version: v0.1.*
