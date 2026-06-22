# NO_PII_NO_DATA — Zero-Collection Architecture (India)

**This document explains, in detail, why AI Brain — India collects no personal data from the user, and what that means under the Digital Personal Data Protection Act 2023.**

---

## TL;DR

The publisher (Wolfgang_rush) operates **zero infrastructure** that touches user data. There is no server. There is no telemetry. There is no analytics. There is no "anonymous usage statistics." The Software runs entirely on the user's device.

---

## The architectural guarantee

AI Brain — India is **local-first** software. Specifically:

**(1) The codebase contains zero telemetry.** Verify this independently:
```bash
grep -rE "telemetry|analytics|tracking|posthog|mixpanel|segment|amplitude|google-analytics|datadog|sentry|requests.post|urlopen" ailawfirm_india/
```
The above command will return only legitimate cloud-AI calls (user-initiated, routed direct to the user's chosen vendor).

**(2) The publisher operates no server.** There is no AI Brain India API. There is no AI Brain India cloud service. There is no AI Brain India database. The publisher's only infrastructure is the public GitHub repository.

**(3) Storage is on the user's device.** Matter data, citation cache, calendar entries, configuration, and all other persistent state live on the user's local filesystem under `~/.ailawfirm-india/`. The publisher has no access to this folder.

**(4) Network calls are limited to:**
- Package installation (PyPI download during `pip install`)
- User-initiated AI cloud calls (only if the user opts into cloud mode — direct to vendor, never through publisher)
- Optional update checks (v0.2+ if added — opt-in only, checks GitHub releases only)

---

## Cloud-mode (when the user opts in)

If the user chooses to use cloud AI processing (DeepSeek · Anthropic Claude · Google Gemini · OpenAI · Mistral · Cohere · Groq · etc.), the user's queries route **directly from the user's device to the AI vendor**.

The publisher is **not in the data path**. The publisher cannot see the user's queries. The publisher does not know what the user processes.

The contract for cloud-mode usage is between **the user** and the **AI vendor** under their respective terms of service. The publisher is not a party to that contract and is not a controller or processor of any data the user transmits to a cloud vendor.

**For client-confidential work, DPDP-sensitive data, and Bar Council Rule 17 confidentiality material, use the local-only mode.** Local-only mode = Ollama + Qwen3 or equivalent. See [MODEL_SETUP.md](MODEL_SETUP.md).

---

## Digital Personal Data Protection Act 2023 — Publisher's status

Under the **DPDP Act 2023** read with the DPDP Rules 2025 (as in force from time to time):

**The publisher is NOT a Data Fiduciary.** Section 2(i) defines "Data Fiduciary" as any person who alone or in conjunction with other persons determines the purpose and means of processing of personal data. The publisher determines neither — the user determines what to process; the user chooses where it gets processed.

**The publisher is NOT a Data Processor.** Section 2(k) defines "Data Processor" as any person who processes personal data on behalf of a Data Fiduciary. The publisher processes no personal data on anyone's behalf — the publisher operates no server.

**The publisher is NOT a Significant Data Fiduciary.** Section 10 SDF designation requires processing — which the publisher does not do.

**The publisher is NOT a Consent Manager.** Section 6(7)-(9) require a Consent Manager to be registered with the Data Protection Board and to handle consent records — none of which apply to a software publisher.

**The publisher IS a software publisher.** Publishing open-source software is not "processing of personal data" under Section 2(t) DPDP Act. It is publication activity governed by the Indian Copyright Act 1957 and the Information Technology Act 2000, not the DPDP Act.

---

## Your status as Data Fiduciary when using this Software

If the user uses this Software to process personal data of clients or any other Data Principal, **the user** is the Data Fiduciary for that processing.

The user's DPDP Act obligations include (non-exhaustive list — verify against current law):

- **Section 5** — Provide notice of processing to the Data Principal (item-wise notice content)
- **Section 6** — Obtain valid consent (free, specific, informed, unconditional, unambiguous, signified by clear affirmative action) where consent is the legal basis
- **Section 7** — Lawful processing for legitimate uses (alternative legal bases enumerated)
- **Section 8** — General obligations of a Data Fiduciary (accuracy · completeness · consistency · security safeguards · breach notification within 72 hours to the Data Protection Board and affected Data Principals · etc.)
- **Section 9** — Children's data — verifiable parental consent + processing restrictions
- **Section 10** — Significant Data Fiduciary specific obligations (DPO appointment · DPIA · audit · etc.) if so designated by Government
- **Section 11-14** — Rights of Data Principals (right to access · correction · erasure · grievance redressal · nominate)
- **Section 15** — Duties of Data Principals
- **Section 16** — Cross-border transfer restrictions (Section 16 read with rules to be notified)
- **Section 17** — Exemptions (carefully read — many exemptions are narrow)

The Software's local-only mode supports the user's Section 8 security obligation by keeping data on a device the user controls. Cloud-mode use requires careful Section 8 + Section 16 analysis by the user.

---

## Cross-border data transfer (Section 16 DPDP)

Section 16 of the DPDP Act restricts cross-border transfer of personal data based on Government notification of permitted/restricted countries.

The publisher transfers no personal data anywhere — Section 16 does not apply to the publisher's activity.

If the user opts into cloud mode and the cloud vendor processes data outside India (most do), the cross-border transfer is the **user's** action. The user's Section 16 obligations apply.

For sensitive matters — especially those involving identifiable Indian individuals, financial data, health data, or government-adjacent information — the user should default to local-only mode regardless of Section 16 status.

---

## Sectoral regulator interplay

The user's use of this Software may also be subject to:
- **RBI guidelines** — for matters involving banking/finance regulated entities
- **SEBI regulations** — for listed-company or securities matters
- **IRDAI directions** — for insurance matters
- **TRAI / DOT** — for telecommunications matters
- **MeitY / CERT-In** — for cybersecurity incidents involving Indian systems
- **Bar Council of India + State Bar Council rules** — for all client confidentiality, conflict, and professional-conduct obligations

The publisher does not provide guidance on these sectoral obligations. The user must independently verify compliance.

---

## Verification path — independent confirmation of zero-collection

The user can independently verify zero-collection at any time:

1. **Code grep:**
   ```bash
   grep -rE "telemetry|analytics|posthog|mixpanel|segment|amplitude|google-analytics|datadog|sentry" ailawfirm_india/
   ```
   Should return zero results.

2. **Dependency audit:**
   ```bash
   cat requirements.txt
   ```
   Should contain no analytics or telemetry libraries.

3. **Offline test:**
   Run the Software with the network disconnected (`pip install` from cache · disconnect WiFi · run any local command). Local features should work fully; cloud-AI calls will fail visibly. This proves there are no hidden network dependencies.

4. **Network inspection during use:**
   Use `nettop` (macOS) / `nethogs` (Linux) / Resource Monitor (Windows) to inspect outbound network traffic during Software use. With cloud-mode disabled, you should see NO outbound traffic from the Software process.

5. **Source-code review:**
   The Software is MIT-licensed open-source. Read the source. There is nothing hidden.

---

## If this changes

If a future version of the Software adds telemetry, opt-in update checks, or any cloud touchpoint involving publisher-controlled infrastructure, the change will be:
- **Announced** in CHANGELOG with the specific data category added
- **Default OFF** — user-opt-in only
- **Documented** in this file with the change date

This file always represents the current state. If it differs from the code, the code is the truth — please file an issue on GitHub.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §2(b) (Zero Data Collection pillar), §3.V4 (Data Protection — DPDP Act 2023), §3.V9 (Conduct-Rule Inducement — BCI Rule 17 confidentiality). Playbook version: v0.1.*
