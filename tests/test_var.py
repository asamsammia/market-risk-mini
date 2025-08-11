import pandas as pd
from src.var import hist_var, hist_es

def test_signs():
    r = pd.Series([-0.1, 0.0, 0.1])
    assert hist_var(r) >= 0
    assert hist_es(r) >= 0