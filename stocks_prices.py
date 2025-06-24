import yfinance as yf

def get_stock_values(stocks_and_shares):
    """
    Calculates the current value of a stock portfolio and the daily change for each stock.

    Args:
        stocks_and_shares (dict): A dictionary where keys are stock tickers (str)
                                 and values are the number of shares held (float).
    """
    total_portfolio_value_today = 0
    total_portfolio_value_yesterday = 0 # Initialize for yesterday's total value
    print("--- Stock Portfolio Value Analysis ---")
    print("--------------------------------------\n")

    for ticker, shares in stocks_and_shares.items():
        try:
            # Convert ticker to uppercase to ensure compatibility with yfinance
            upper_ticker = ticker.upper()

            # Fetch historical data for the last two trading days.
            # 'period="2d"' retrieves data for the last 2 days.
            stock = yf.Ticker(upper_ticker)
            hist = stock.history(period="2d")

            # Check if sufficient historical data was retrieved
            if hist.empty or len(hist) < 2:
                print(f"Warning: Not enough historical data found for {upper_ticker}. Skipping analysis for this stock.")
                print("-" * 40 + "\n")
                continue

            # Get today's closing price (the most recent available)
            today_price = hist['Close'].iloc[-1]
            # Get yesterday's closing price (the second most recent available)
            yesterday_price = hist['Close'].iloc[-2]

            # Calculate the current value of the shares for this stock
            current_value = today_price * shares
            # Calculate the value of the shares based on yesterday's closing price
            previous_day_value = yesterday_price * shares
            # Calculate the change in value from yesterday to today
            value_change = current_value - previous_day_value

            # Add the current stock's value to the total portfolio value
            total_portfolio_value_today += current_value
            total_portfolio_value_yesterday += previous_day_value # Accumulate yesterday's total

            # Print the detailed information for the current stock
            print(f"Stock: {upper_ticker}")
            print(f"  Shares Held: {shares}")
            print(f"  Today's Closing Price: ${today_price:.2f}")
            print(f"  Current Value of Holdings: ${current_value:.2f}")
            print(f"  Last Trading Day's Closing Price: ${yesterday_price:.2f}")
            print(f"  Value Change (compared to last trading day): ${value_change:+.2f}") # Use + for positive changes
            print("-" * 40 + "\n")

        except Exception as e:
            # Handle any errors that occur during fetching or calculation for a specific stock
            print(f"Error processing {ticker.upper()}: {e}")
            print("Please ensure the ticker symbol is correct and valid.\n")
            print("-" * 40 + "\n")

    # Calculate net gain/loss for the entire portfolio
    net_gain_loss = total_portfolio_value_today - total_portfolio_value_yesterday

    # Print the total portfolio value for today, yesterday, and the net gain/loss
    print(f"--------------------------------------")
    print(f"Total Portfolio Value Yesterday: ${total_portfolio_value_yesterday:.2f}")
    print(f"Total Portfolio Value Today: ${total_portfolio_value_today:.2f}")
    print(f"Net Gain/Loss Today vs. Yesterday: ${net_gain_loss:+.2f}") # Display with sign
    print(f"--------------------------------------")

# Your provided list of stock tickers and shares
# Note: Dictionary keys are case-insensitive when passed to yfinance,
# but it's good practice to keep them consistent (e.g., all uppercase).
stocks_and_shares_c = {
    "META": 0.6706,
    "NVDA": 3.0156,
    "PLTR": 2,
    "COST": 0.1012,
    "SRAD": 2,
    "GRAB": 1,
    "SPY":0.1659430436
    }
stocks_and_shares_a= {
    "META": 0.6347,
    "NVDA": 2.2623,
    "PLTR": 2,
    "MRVL": 3,
    "SPY":0.1659430436
}
stocks_and_shares_z= {
    "PLTR": 5,
    "SRAD": 6,
    "GRAB": 30,
    "CMG": 0.0312,
    "SPY":0.15336695342
}
# Call the function to get and print the stock values
get_stock_values(stocks_and_shares_c)
get_stock_values(stocks_and_shares_a)
get_stock_values(stocks_and_shares_z)
# Example usage: