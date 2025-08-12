# Market Risk Mini

Lightweight **stress** and **exposure** analytics on synthetic portfolios to illustrate scenario analysis.

## Why
Provide fast portfolio-level scans to spot sensitivities and concentration risk.

## Tech
- Python 3.10+, pandas, numpy
- Optional: matplotlib/plotly for charts

## Data
Sample input format:
```
position_id, instrument, qty, price, beta, sector
```
Edit `data/sample_positions.csv` or load your own.

## How to Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # or pip install pandas numpy
python src/run_scenarios.py --positions data/sample_positions.csv --scenario shocks/base.yaml
```
- See `scenarios/` for simple shock files (e.g., equity -10%, sector +5 vol).

## Outputs
- Exposure tables by sector/instrument
- Scenario P&L deltas
- Optional charts in `outputs/`

## Key Results (placeholders)
- Ran N scenarios in < T seconds on laptop hardware.
- Identified top 3 risk concentrations with simple heuristics.

## Notes
- Replace N/T with your measurements.
- Add real scenarios/greeks if you extend the model.
