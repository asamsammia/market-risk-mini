import argparse
import numpy as np
import pandas as pd

def hist_var(returns: pd.Series, alpha=0.95):
    q = 1 - alpha
    return -np.quantile(returns.dropna(), q)

def hist_es(returns: pd.Series, alpha=0.95):
    q = 1 - alpha
    tail = returns[returns <= np.quantile(returns.dropna(), q)]
    return -tail.mean()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.demo:
        rng = np.random.default_rng(42)
        r = pd.Series(rng.normal(0.0005, 0.01, 252))
        print("VaR(95%):", round(hist_var(r), 5))
        print("ES(95%):", round(hist_es(r), 5))