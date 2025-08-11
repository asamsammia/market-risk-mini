import pandas as pd
import statsmodels.api as sm


def factor_betas(asset: pd.Series, factors: pd.DataFrame):
    """Estimate factor betas via OLS.

    Parameters
    ----------
    asset : pd.Series
        Asset excess returns aligned by date index.
    factors : pd.DataFrame
        Factor excess returns with matching index.

    Returns
    -------
    (params, r2) : (pd.Series, float)
        Regression coefficients (with constant) and R-squared.
    """
    df = pd.concat([asset.rename("asset") , factors], axis=1).dropna()
    y = df["asset"]
    X = sm.add_constant(df.drop(columns=["asset"]))
    model = sm.OLS(y, X).fit()
    return model.params, model.rsquared
