from model.main import main
from model.config import BinomialOptionConfig

config = BinomialOptionConfig(
    S0=60,
    K=62,
    T=2,
    r=0.06,
    rf= None,
    dividend_yield=0,
    dividend_cash=[(0.5, 3), (0.8, 5), (1.2, 2.5)],
    option_type="put",
    option_style="american",
    steps=100
)

main(0.2, config)