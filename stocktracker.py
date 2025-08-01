portfolio = {}  # Global dictionary to hold all purchases
stocks = {
    "AAPL": 211.18,
    "TSLA": 329.65,
    "GOOGL": 185.06,
    "MSFT": 510.05,
    "AMZN": 226.13,
    "NVDA": 172.41,
    "META": 704.28,
    "BRK.B": 473.80,
    "JPM": 291.27,
    "UNH": 282.65
}

def total_investment(stockP_name, price_per_share, shares_purchased):
    if stockP_name in portfolio:
        portfolio[stockP_name]["Shares Purchased"] += shares_purchased
        portfolio[stockP_name]["Total Investment"] += price_per_share * shares_purchased
    else:
        portfolio[stockP_name] = {
            "Price Per Share": price_per_share,
            "Shares Purchased": shares_purchased,
            "Total Investment": price_per_share * shares_purchased
        }

def display_portfolio():
    print("\nYour portfolio:")
    if not portfolio:
        print("No stocks purchased yet.")
    else:
        net_total = 0
        for stock, details in portfolio.items():
            print(f"{stock}: {details}")
            net_total += details["Total Investment"]
        print(f"\nNet Total Investment: {net_total}")

def save_portfolio_to_file(filename="portfolio.txt"):
    with open(filename, "w") as file:
        file.write("Your portfolio:\n")
        net_total = 0
        for stock, details in portfolio.items():
            file.write(f"{stock}: {details}\n")
            net_total += details["Total Investment"]
        file.write(f"\nNet Total Investment: {net_total}\n")
    print(f"\nPortfolio saved to {filename}")

def purchase_stocks():
    while True:
        print("\nAvailable stocks:")
        for symbol, price in stocks.items():
            print(f"{symbol}: {price}")

        stockP_name = input("\nEnter the name of the stock: ").upper()
        if stockP_name not in stocks:
            print("Stock not found.")
        else:
            try:
                shares_purchased = int(input("Enter the number of shares you would like to purchase: "))
                total_investment(stockP_name, stocks[stockP_name], shares_purchased)
                print(f"Your total investment in {stockP_name} for {shares_purchased} shares is {shares_purchased * stocks[stockP_name]}")
            except ValueError:
                print("Invalid number of shares. Please enter an integer.")
                continue

            check = input("Would you like to view your portfolio? (yes/no): ").strip().lower()
            if check == "yes":
                display_portfolio()

            receipt_check = input("Would you like to print a receipt of your portfolio? (yes/no): ").strip().lower()
            if receipt_check == "yes":
                save_portfolio_to_file()

        counter = input("Type 'yes' to continue purchasing stocks or 'no' to stop: ").strip().lower()
        if counter == "no":
            break

def main():
    purchase_stocks()
    print("\nFinal Portfolio:")
    display_portfolio()

main()
