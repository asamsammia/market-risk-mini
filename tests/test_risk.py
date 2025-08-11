import numpy as np
import pandas as pd
from src.risk_metrics import max_drawdown, sharpe_ratio


def test_basic_metrics():
    rng = np.random.default_rng(0)
    r = pd.Series(rng.normal(0.0005, 0.01, 100))
    mdd = max_drawdown(r)
    sr = sharpe_ratio(r)
    assert mdd <= 0
    assert np.isfinite(sr) or np.isnan(sr)
