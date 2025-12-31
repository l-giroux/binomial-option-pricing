import numpy as np
from tqdm import tqdm
from model.parameters import parameters
from model.config import BinomialOptionConfig


def american(std: float, config: BinomialOptionConfig):

    K = config.K
    S0 = config.S0
    t = config.T
    D = config.dividend_cash
    option_type = config.option_type
    steps = config.steps

    rows = np.arange(steps + 1)[:, None] - np.arange(steps + 1)

    up_arr = rows[rows >= 0]

    down_rows = rows[:, ::-1]
    down_arr = down_rows[down_rows >= 0]

    p, p1, disc, up, down = parameters(std, config, up_arr, down_arr)

    total_S = up * down * S0

    # \\ cash dividend calculation
    if D:
        arr = np.repeat(np.arange(steps+1), np.arange(1, steps+2))
        arr = arr / steps * t
        for i in tqdm(range(len(D)), desc="Calculating cash dividends ... "):
            mask = D[i][0] < arr
            total_S -= (mask.astype(int)) * D[i][0]
    # \\

    S_t = total_S

    if option_type == "call":
        initial_val = np.maximum(0, total_S[-(steps+1):] - K)

        option_price = initial_val

        for i in tqdm(range(steps, 0, -1), desc="Estimating ... "):
            S_t = S_t[:-(i+1)]
            option_price = (option_price[:-1] * p + option_price[1:] * p1) * disc
            option_price = np.maximum(option_price, S_t[-i:] - K)

    if option_type == "put":
        initial_val = np.maximum(0, K - total_S[-(steps+1):])

        option_price = initial_val

        for i in tqdm(range(steps, 0, -1), desc="Estimating ... "):
            S_t = S_t[:-(i+1)]
            option_price = (option_price[:-1] * p + option_price[1:] * p1) * disc
            option_price = np.maximum(option_price, K - S_t[-i:])

    return option_price.item()