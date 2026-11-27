# Indian Tax Compliance Verification
**Using Propositional Logic and Truth-Table Model Checking**

An educational Artificial Intelligence micro-project that demonstrates symbolic knowledge representation, logical inference, and truth-table model checking ($KB \models REF$) using Python and an interactive web simulator.

## Academic Details
- **Student:** Rahul Shivaji Sankpal 
## Project Overview
This project models a simplified, hypothetical tax-refund verification workflow using three propositional symbols:
- **`ITR`**: Income Tax Return filed
- **`TDS`**: Excess Tax Deducted at Source
- **`REF`**: Tax Refund eligible

### Knowledge Base (KB) & Rules
- **Rule 1:** $ITR \rightarrow TDS$ (`not ITR or TDS`)
- **Rule 2:** $TDS \rightarrow REF$ (`not TDS or REF`)
- **Query:** $REF$

The model-checking engine enumerates all $2^3 = 8$ Boolean truth assignments and verifies whether $REF$ holds `True` in every model where the Knowledge Base is satisfied.

## Repository Contents
- `index.html` — Interactive web simulator with live truth-table generation and diagnostic explanations.
- `main.py` — Python implementation using `itertools.product()` for truth-table model checking.
- `Micro_Project_Report.pdf` — Complete academic micro-project report.

## How to Run
1. **Web Simulator:** Open `index.html` in any web browser (or visit the live GitHub Pages link in the About section).
2. **Python CLI:**
   ```bash
   python main.py
   ```

> 
