from model.main import main
from model.config import BinomialOptionConfig

config = BinomialOptionConfig(
    S0=37,
    K=40,
    T=3,
    r=0.03,
    rf = None,
    dividend_yield=0,
    dividend_cash=[],
    option_type="put",
    option_style="future",
    steps=100
)

main(0.32, config)