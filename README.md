# Investment Portfolio Optimization

## Project Overview

This project applies portfolio optimization principles to construct an investment portfolio using stocks from the American stock exchange. The portfolio optimization is based on Harry Markowitz's Modern Portfolio Theory, focusing on diversification to balance risk and return.

### Objective

The goal is to construct two optimized portfolios under different conditions:
1. **Variant 1**: Achieve an expected return of at least 5% with the lowest possible risk.
2. **Variant 2**: Maximize the expected return while ensuring the portfolio variance does not exceed half of the highest individual stock variance.


## Table of Contents

- [Installation](#installation)
- [Data Collection](#data-collection)
- [Optimization](#optimization)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)


## Installation

To run this project, ensure the following packages are installed:

```bash
pip install yfinance pandas numpy scipy
```


## Data Collection

We retrieve stock data from Yahoo Finance for the selected companies on the American stock exchange.

Example ticker list:

- Apple (AAPL)
- Microsoft (MSFT)
- Google (GOOGL)
- Amazon (AMZN)
- Tesla (TSLA)
- Meta (META)
- NVIDIA (NVDA)
- JPMorgan Chase (JPM)
- Johnson & Johnson (JNJ)
- Visa (V)
- Procter & Gamble (PG)

# Code for Data Import and Preprocessing

Historical stock data is fetched, and daily returns are calculated. The average returns and covariance matrix for these stocks are used to model portfolio risk and returns.


## Optimization

Portfolio Optimization Functions

Two main optimization functions were defined:

1. Variant 1: Minimizes risk while achieving a target return of 5%.
2. Variant 2: Maximizes return with a capped portfolio variance.

These optimizations are carried out using the scipy.optimize.minimize method.


## Results

After running the optimization:

1. Variant 1 provided a portfolio composition with minimized risk for a 5% expected return.
2. Variant 2 yielded a portfolio with maximized returns while maintaining a capped risk level.

# ***Output Example***
> Optimal Weights for Variant 1: [0.10, 0.15, ..., 0.12]
> Optimal Weights for Variant 2: [0.20, 0.05, ..., 0.10]


## Conclusion

The optimized portfolios demonstrate effective diversification by balancing risk and return. Variant 1 allows for lower risk with a moderate return, while Variant 2 pursues higher returns within a limited risk framework. These approaches illustrate the benefits of Modern Portfolio Theory in real-world investment scenarios.


### References
- Harry Markowitz's Portfolio Theory (Nobel Prize, 1990)
- Yahoo Finance
- Scipy Documentation