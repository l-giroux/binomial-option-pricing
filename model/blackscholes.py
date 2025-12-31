import numpy as np
from scipy import stats
from model.config import BinomialOptionConfig

def black_scholes(std: float, config: BinomialOptionConfig):

    S0 = config.S0
    K = config.K
    t = config.T
    r = config.r
    q = config.dividend_yield
    option_type = config.option_type
    option_style = config.option_style

    if option_style == "fx":
        q = config.rf

    if option_style == "future":
        q = r

    mu = r - q

    d1 = (np.log(S0/K) + (mu + std ** 2 /2) * t) / (std * np.sqrt(t))
    d2 = d1 - std * np.sqrt(t)

    disc_strike = K * np.exp(-r * t)

    if option_type == "call":
        call = stats.norm.cdf(d1) * S0 * np.exp(-q * t) - stats.norm.cdf(d2) * disc_strike
        return call
    
    if option_type == "put":
        put = disc_strike * stats.norm.cdf(-d2) - S0 * np.exp(-q * t) * stats.norm.cdf(-d1)
        return put