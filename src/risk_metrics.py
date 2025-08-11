import numpy as np
import pandas as pd


def drawdown(returns: pd.Series) -> pd.Series:
    """Compute percentage drawdown from cumulative returns."""
    cum = (1 + returns.fillna(0)).cumprod()
    peak = cum.cummax()
    dd = (cum / peak) - 1
    return dd


def max_drawdown(returns: pd.Series) -> float:
    """Maximum drawdown (as a negative number)."""
    return drawdown(returns).min()


def sharpe_ratio(returns: pd.Series, rf: float = 0.0, periods: int = 252) -> float:
    """Annualized Sharpe ratio."""
    excess = returns - (rf / periods)
    mu = excess.mean() * periods
    sigma = excess.std(ddof=1) * np.sqrt(periods)
    return mu / sigma if sigma != 0 else np.nan
