# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "MSFT": 300,
    "INFY": 1450
}

def main():
    total_investment = 0
    investment_details = []

    print("📈 Simple Stock Tracker")
    print("Enter stock names and quantities (type 'done' to finish):\n")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found in price list. Try again.")
            continue
        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            price = stock_prices[stock]
            investment = price * qty
            investment_details.append((stock, qty, price, investment))
            total_investment += investment
        except ValueError:
            print("❌ Invalid quantity. Enter a number.")
    
    print("\n📊 Investment Summary:")
    for stock, qty, price, investment in investment_details:
        print(f"{stock}: {qty} shares @ ₹{price} = ₹{investment}")

    print(f"\n💰 Total Investment: ₹{total_investment}")

    # Optional: Save to file
    save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
    if save == "yes":
        with open("investment_report.csv", "w") as f:
            f.write("Stock,Quantity,Price,Investment\n")
            for stock, qty, price, investment in investment_details:
                f.write(f"{stock},{qty},{price},{investment}\n")
            f.write(f"\nTotal,,,{total_investment}")
        print("✅ Saved to investment_report.csv")

if __name__ == "__main__":
    main()
