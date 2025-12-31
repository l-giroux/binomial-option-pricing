import numpy as np
from model.config import BinomialOptionConfig

def parameters(std, config: BinomialOptionConfig, up_arr, down_arr):

    r = config.r
    q = config.dividend_yield
    t = config.T
    steps = config.steps
    option_style = config.option_style

    if option_style == "fx":
        q = config.rf

    mu = r - q
    if option_style == "future":
        mu = 0

    u = np.exp(std * np.sqrt(t/steps))
    d = 1/u

    disc = np.exp(-r * t / steps)

    p = (np.exp(mu * t / steps) - d)/(u - d)
    p1 = 1 - p

    up = u ** up_arr
    down = d ** down_arr

    return p, p1, disc, up, down