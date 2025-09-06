# README.md

## ⚖️ AFCA Jurisdiction & Remedies Checker

This Streamlit app provides an **indicative assessment** of:

1. **Jurisdiction** — whether a complaint is likely to fall within AFCA’s rules (eligibility, time limits, monetary limits, exclusions).
2. **Remedies** — what outcomes AFCA can award under **Sections D.2–D.6** of the AFCA Rules, applying the **current monetary caps** (effective **1 Jan 2024**, per AFCA Rule changes v5.1).

---

### 🚀 Features
- **Jurisdiction Checker**
  - Checks eligibility (complainant type, member firm, product scope).
  - Applies time limits (B.4.2 NCC special cases, B.4.3 general 6-year/2-year rules).
  - Flags mandatory (C.1) and discretionary (C.2) exclusions.
  - Enforces **monetary restriction per claim ($1,263,000)** and relevant **D.4 claim-type caps**.

- **Remedies Checker**
  - Evaluates requested remedies against AFCA’s powers.
  - Applies **D.4 compensation caps** by claim type:
    - Income stream insurance — $16,900/month
    - General insurance broking — $316,000
    - Uninsured motor vehicle — $19,000
    - Credit (Small Business borrower) — $1,263,500 (facility ≤ $6,317,000)
    - Credit (Primary Producer borrower) — $2,526,500 (facility ≤ $6,317,000)
    - Credit (Other borrower) — $631,500
    - All other claims — $631,500
    - Indirect financial loss — $6,300
    - Non-financial loss — $6,300
  - Recognises **permitted remedies** (e.g. pay claim, repair/replace, refund, vary/rectify, debt relief, interest, apology) and flags **prohibited remedies** (e.g. punitive damages).

- **Report Export**
  - Generates a structured Markdown report with case inputs, jurisdiction findings, and remedy availability.

---

### 📦 Requirements
- Python 3.9+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

`requirements.txt` should include:
```txt
streamlit
pandas
```

---

### ▶️ Running the App

```bash
streamlit run app.py
```

- Open the local Streamlit URL in your browser.
- Enter case details and (optionally) requested remedies.
- View jurisdiction + remedies analysis in the browser.
- Download a Markdown report for your AFCA file.

---

### ⚙️ Configuration
- Upload a **JSON config** via the sidebar to override default caps, thresholds, or remedy catalog.
- Default config aligns to **AFCA Rules v5.1 (effective 1 July 2024)** with **D.4 tables (1 Jan 2024 monetary limits)**.
- For production/legal use, always cross-check against the official [AFCA Rules](https://www.afca.org.au/about-afca/rules-and-guidelines/rules) and [Operational Guidelines](https://www.afca.org.au/about-afca/rules-and-guidelines/afcas-operational-guidelines).

---

### 📖 Sources
- AFCA Rules v5.1 (effective 1 July 2024)
- AFCA Operational Guidelines (2024)
- AFCA News — Compensation caps and monetary limits adjusted 1 Jan 2024

---

### ⚠️ Disclaimer
This tool is for **indicative purposes only**. It does **not substitute** for AFCA’s Rules, Operational Guidelines, or legal advice. Always confirm findings against the official AFCA materials.
