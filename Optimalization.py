import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Step 1: Define the tickers for American stocks and download historical data
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "BRK-B", "JNJ", "V", "UNH"]

# Fetch historical adjusted close prices for the specified period
data = yf.download(tickers, start="2000-01-01", end="2024-10-28")['Adj Close']

# Step 2: Calculate daily returns and compute mean returns & covariance matrix
returns = data.pct_change().dropna()
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Number of assets
num_assets = len(tickers)

# Step 3: Define optimization functions for portfolio variance and return
def portfolio_variance(weights, cov_matrix):
    return weights.T @ cov_matrix @ weights

def portfolio_return(weights, mean_returns):
    return weights.T @ mean_returns

# Constraints and bounds for weights (weights must sum to 1, between 0 and 1)
constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
bounds = tuple((0, 1) for _ in range(num_assets))

# Step 4: Optimize for Minimum Variance Portfolio (Variant 1)
initial_guess = np.ones(num_assets) / num_assets
result_variant_1 = minimize(portfolio_variance, initial_guess, args=(cov_matrix,),
                            method='SLSQP', bounds=bounds, constraints=constraints)
optimal_weights_variant_1 = result_variant_1.x

# Step 5: Optimize for Maximum Sharpe Ratio Portfolio (Variant 2)
risk_free_rate = 0.01

def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    port_return = portfolio_return(weights, mean_returns)
    port_variance = portfolio_variance(weights, cov_matrix)
    return -(port_return - risk_free_rate) / np.sqrt(port_variance)

result_variant_2 = minimize(neg_sharpe_ratio, initial_guess, args=(mean_returns, cov_matrix, risk_free_rate),
                            method='SLSQP', bounds=bounds, constraints=constraints)
optimal_weights_variant_2 = result_variant_2.x

# Step 6: Map asset names to optimal weights for each variant
variant_1_mapping = dict(zip(tickers, optimal_weights_variant_1))
variant_2_mapping = dict(zip(tickers, optimal_weights_variant_2))

# Display results
print("Optimal Weights for Variant 1 (Minimum Variance Portfolio):")
for asset, weight in variant_1_mapping.items():
    print(f"{asset}: {weight:.4f}")

print("\nOptimal Weights for Variant 2 (Maximum Sharpe Ratio Portfolio):")
for asset, weight in variant_2_mapping.items():
    print(f"{asset}: {weight:.4f}")

# Step 7: Plot the Optimal Weights for each variant
plt.figure(figsize=(12, 6))

# Plot for Minimum Variance Portfolio
plt.subplot(1, 2, 1)
plt.bar(variant_1_mapping.keys(), variant_1_mapping.values())
plt.title("Minimum Variance Portfolio Weights")
plt.xlabel("Assets")
plt.ylabel("Weights")
plt.xticks(rotation=45)

# Plot for Maximum Sharpe Ratio Portfolio
plt.subplot(1, 2, 2)
plt.bar(variant_2_mapping.keys(), variant_2_mapping.values(), color='orange')
plt.title("Maximum Sharpe Ratio Portfolio Weights")
plt.xlabel("Assets")
plt.ylabel("Weights")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Step 8: Generate Efficient Frontier for Visualization
port_returns = []
port_risks = []

for _ in range(5000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    
    ret = np.sum(weights * mean_returns)
    risk = np.sqrt(weights.T @ cov_matrix @ weights)
    
    port_returns.append(ret)
    port_risks.append(risk)

# Convert lists to numpy arrays for easy plotting
port_returns = np.array(port_returns)
port_risks = np.array(port_risks)

# Plot Efficient Frontier with Optimal Portfolios
plt.figure(figsize=(10, 6))
plt.scatter(port_risks, port_returns, c=port_returns / port_risks, cmap='viridis', marker='o')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Portfolio Risk')
plt.ylabel('Portfolio Return')
plt.title('Efficient Frontier with Optimal Portfolios')

# Mark optimal points for reference
plt.scatter(np.sqrt(portfolio_variance(optimal_weights_variant_1, cov_matrix)), 
            portfolio_return(optimal_weights_variant_1, mean_returns), color='red', label="Min Variance Portfolio")
plt.scatter(np.sqrt(portfolio_variance(optimal_weights_variant_2, cov_matrix)), 
            portfolio_return(optimal_weights_variant_2, mean_returns), color='blue', label="Max Sharpe Ratio Portfolio")
plt.legend(loc='best')
plt.show()
