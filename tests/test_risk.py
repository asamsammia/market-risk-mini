import numpy as np
from src.risk_metrics import var, es

def test_var_es():
    data = np.random.normal(0, 1, 1000)
    assert isinstance(var(data), float)
    assert isinstance(es(data), float)
