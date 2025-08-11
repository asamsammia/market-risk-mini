import numpy as np

def var(series, alpha=0.05):
    return np.percentile(series, 100*alpha)

def es(series, alpha=0.05):
    v = var(series, alpha)
    return series[series <= v].mean()

def scenario_shift(series, shift):
    return series + shift
