from dataclasses import dataclass
from typing import Literal
import numpy as np

@dataclass
class BinomialOptionConfig:
    S0: float # initial underlying asset price
    K: float #strike price
    T: float #time to maturity
    r: float #risk free rate
    rf: float #foreign exchange: foreign risk free rate
    dividend_yield: float #percent dividend payment
    dividend_cash: list[tuple[float, float]] #tuple: time of dividend payment, dividend cash amount
    option_type: Literal["call", "put"]
    option_style: Literal["american", "european", "fx", "future"]
    steps: int

    def validate(self) -> None:
        assert self.S0 > 0
        assert self.K > 0
        assert self.T > 0
        assert 1 >= self.r >= 0
        assert self.dividend_yield >= 0
        assert self.option_type in {"call", "put", None}
        assert self.option_style in {"american", "european", "fx", "future"}
        assert self.steps > 0

        if self.dividend_cash:
            D_t = np.array(self.dividend_cash)[:, 0]
            assert np.all((D_t > 0) & (D_t < self.T))
            assert np.all(np.array(self.dividend_cash)[:, 1] > 0)