import pandas as pd
import statsmodels.api as sm

def factor_betas(asset: pd.Series, factors: pd.DataFrame):
    df = pd.concat([asset, factors], axis=1).dropna()
    y = df.iloc[:, 0]
    X = sm.add_constant(df.iloc[:, 1:])
    model = sm.OLS(y, X).fit()
    return model.params, model.rsquared