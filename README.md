# Market Risk Mini-Stack

Quick-start toolkit for VaR/ES, scenario analysis, and factor exposures.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/var.py --demo
```
## Modules
- `src/var.py` – Historical/Parametric VaR & Expected Shortfall
- `src/factors.py` – Factor exposure via OLS
- `notebooks/risk_walkthrough.ipynb` – step-by-step demo
