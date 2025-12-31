from model.main import main
from model.config import BinomialOptionConfig

config = BinomialOptionConfig(
    S0=60,
    K=65,
    T=1.4,
    r=0.058,
    rf=None,
    dividend_yield=0.03,
    dividend_cash=[],
    option_type="call",
    option_style="european",
    steps=100
)

main(0.35, config)