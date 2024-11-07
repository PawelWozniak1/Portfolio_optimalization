# Portfolio Optimization Project

This project focuses on optimizing an investment portfolio by maximizing returns and minimizing risk. Using historical stock data, we explore various portfolios, calculate their risks and returns, and identify optimal portfolios along the efficient frontier.

## Project Overview

The goal of this analysis is to construct an optimal portfolio that aligns with specific investment objectives, such as maximizing the Sharpe ratio, minimizing risk, or achieving a target return. We use techniques from modern portfolio theory to determine the efficient frontier and identify the most efficient asset allocation.

### Key Objectives

- Calculate daily and logarithmic returns for selected assets.
- Compute the covariance and correlation matrices.
- Generate and visualize random portfolios.
- Plot the efficient frontier.
- Identify optimal portfolios based on:
  - Maximum Sharpe Ratio
  - Minimum Risk
  - Custom Target Returns (e.g., 25% and 35%)

## Dataset

The data used for this analysis includes daily closing prices for selected assets over approximately 10 years. The data is stored in `akcje.txt` and includes 2776 entries.

## Analysis Steps

1. **Data Preparation**
   - Load data and calculate daily price changes.
   - Compute daily and logarithmic returns.

2. **Statistical Analysis**
   - Generate covariance and correlation matrices for returns.
   - Visualize correlations using a heatmap.

3. **Portfolio Simulation**
   - Generate a large number of random portfolios with varied allocations.
   - Calculate portfolio risk, return, and Sharpe ratio for each simulated portfolio.

4. **Efficient Frontier**
   - Plot the efficient frontier based on portfolio risk-return combinations.
   - Highlight optimal portfolios:
     - **Max Sharpe Ratio Portfolio**
     - **Min Risk Portfolio**
     - Portfolios with target returns (e.g., 25%, 35%).

5. **Visualization**
   - Display the efficient frontier plot, showcasing the different portfolio strategies.

## Results

The analysis produces a comprehensive visualization of the efficient frontier with marked points for:
- **Max Sharpe Ratio Portfolio** (Highest risk-adjusted return)
- **Min Risk Portfolio** (Lowest possible risk)
- **Target Return Portfolios** (Portfolios meeting specific return goals)

The following plot illustrates the efficient frontier and optimal portfolio allocations:

![Efficient Frontier Plot](R:\Portfolio_optimalization\efficient_frontier.png)

## Getting Started

### Prerequisites

- Python (version 3.8+ recommended)
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`

### Running the Notebook

1. Clone this repository.
2. Ensure the dataset (`akcje.txt`) is in the same directory.
3. Run each section of the Jupyter Notebook to reproduce the analysis and visualizations.

## Conclusion

This project provides insights into optimal portfolio allocation, balancing returns and risk. The efficient frontier and calculated optimal portfolios serve as a guide for constructing diversified portfolios tailored to specific investment strategies.

## License

This project is licensed under the MIT License.

---

**Note:** Replace `R:\Portfolio_optimalization\efficient_frontier.png` with the actual path to your generated plot image.
