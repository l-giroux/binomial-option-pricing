import numpy as np
from tqdm import tqdm
from model.parameters import parameters
from model.config import BinomialOptionConfig


def european(std: float, config: BinomialOptionConfig):

    K = config.K
    D = config.dividend_cash
    r = config.r
    S0 = config.S0
    option_type = config.option_type

    # \\ cash dividend calculation
    if D:
        PVD = []
        for i in range(len(D)):
            t = D[i][0]
            d = D[i][1]
            PVD.append(d * np.exp(-r * t))

        S0 -= sum(PVD)
    # \\
    
    arr = np.arange(config.steps + 1)

    p, p1, disc, up, down = parameters(std, config, arr, arr[::-1])

    S_array = up * down * S0

    if option_type == "call":
        initial_val = np.maximum(S_array - K, 0)
    if option_type == "put":
        initial_val = np.maximum(K - S_array, 0)

    option_price = initial_val

    for _ in tqdm(range(config.steps), desc="Estimating ... "):
        option_price = (option_price[:-1] * p1 + option_price[1:] * p) * disc

    return option_price.item()
