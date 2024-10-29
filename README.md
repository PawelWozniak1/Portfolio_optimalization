# Investment Portfolio Optimization

## Project Overview

This project applies portfolio optimization principles to construct an investment portfolio using stocks from the American stock exchange. The portfolio optimization is based on Harry Markowitz's Modern Portfolio Theory, focusing on diversification to balance risk and return.

### Objective

The goal is to construct two optimized portfolios under different conditions:
1. **Variant 1**: Achieve an expected return of at least 5% with the lowest possible risk.
2. **Variant 2**: Maximize the expected return while ensuring the portfolio variance does not exceed half of the highest individual stock variance.

---

## Table of Contents

- [Installation](#installation)
- [Data Collection](#data-collection)
- [Optimization](#optimization)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)

---

## Installation

To run this project, ensure the following packages are installed:

```bash
pip install yfinance pandas numpy scipy
```

---

## Data Collection

We retrieve stock data from Yahoo Finance for the selected companies on the American stock exchange.

Example ticker list:

Apple (AAPL)
Microsoft (MSFT)
Google (GOOGL)
Amazon (AMZN)
Tesla (TSLA)
Meta (META)
NVIDIA (NVDA)
JPMorgan Chase (JPM)
Johnson & Johnson (JNJ)
Visa (V)
Procter & Gamble (PG)
Code for Data Import and Preprocessing
Historical stock data is fetched, and daily returns are calculated. The average returns and covariance matrix for these stocks are used to model portfolio risk and returns.