from model.main import main
from model.config import BinomialOptionConfig

config = BinomialOptionConfig(
    S0= 50,
    K= 60,
    T=2.5,
    r=0.07,
    rf = 0.03,
    dividend_yield=0,
    dividend_cash=[],
    option_type="call",
    option_style="fx",
    steps=100
)

main(0.4, config)