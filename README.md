## Binomial Option Pricing Model (CRR)

This project is an educational implementation of a CRR binomial tree option pricing model.

## Project Overview

This project uses the Cox-Ross-Rubinstein binomial trees to estimate option price. European and American style options, as well as forward, futures, and foreign exchange options are supported. Binomial trees and/or underlying asset value are adjusted based on the presence of dividends. Model option price is compared to values given by the Black-Scholes model for validation.


## Methodology

- Parameters are calculated based on inputs.
- Binomial tree is calculated based on parameters and option specifications
- Output is compared to the Black-Scholes option pricing model.

## Core Functions

**Parameters**
Risk-neutral probability and discount rate factor are calculated and returned based on inputs. Drift rate is adjusted in case of dividend yield, foreign risk-free rate, and future option pricing. The function also returns an up-down factor array for total movements along the binomial tree.

**European**
Underlying asset prices at maturity are explicitly calculated using the up-down factor array from the parameters function. Option value is calculated at each step of the tree until the spot option price is found. Option payoff structure is considered based on option type (call/put).
In case of discrete cash dividends, their present value is calculated and subtracted from spot underlying asset price.
This function is also used to price foreign exchange and future/forward options.

**American**
Underlying asset prices are calculated at each step of the binomial tree using the up-down factor array from the parameters function. Option value is compared to exercise payoff at each step until the spot option price is found. Option payoff structure is considered based on option type (call/put).
In case of discrete cash dividends, cash value is subtracted at each step subsequent to the dividend payment.

**Black-Scholes**
Prices options based on the Black-Scholes model. The model is adjusted in case of dividend yield, foreign risk-free rate, and future option pricing.

## Inputs

- Underlying asset spot price
- Option strike price
- Option time to maturity (years)
- Risk-free rate
- Foreign risk-free rate (fx estimation)
- Percent dividend yield
- Discrete cash dividends
- Option type (call, put)
- Option style (american, european, fx, future/forward)
- Steps
- Underlying asset standard deviation

*All rates should be expressed as decimals rather than percentages.*

## Outputs

- Option price, binomial estimation
- Option price, Black-Scholes model

**Example Output**

    Binomial Estimation: 9.138546174363187
    Black-Scholes Model: 9.126619039583064

## Assumptions
- No early exercise for european options.
- The underlying asset can only move to one of two values for each step (up or down).
- Inputs are constant over the option's life.
- Time is divided into discrete steps until the option expires.
- Dividends are either a constant yield or a discrete cash amount.
- No transaction costs are considered.

*Disclaimer: This implementation is intended for educational purposes only and does not constitute a production option pricing model.*