from model.american import american
from model.european import european
from model.blackscholes import black_scholes
from model.config import BinomialOptionConfig

def main(std: float, config: BinomialOptionConfig):
    config.validate()
    assert 0 <= std

    style = config.option_style

    if style == "american":
        if not config.dividend_cash and config.dividend_yield == 0:
            option_price = european(std, config)
        else:
            option_price = american(std, config)

    if style == "european" or style == "fx" or style == "future":
        option_price = european(std, config)

    out = {
    "Binomial Estimation": option_price,
    "Black-Scholes Model": black_scholes(std, config),
}

    for key, value in out.items():
        print(f"{key}: {value}")