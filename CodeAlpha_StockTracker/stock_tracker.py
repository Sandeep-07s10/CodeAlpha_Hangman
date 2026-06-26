# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 140,
    "MSFT": 300
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:

    stock = input("Enter Stock Name (or done): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:

        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock] * quantity

        total += investment

        print("Investment Value =", investment)

    else:
        print("Stock Not Found")

print("\nTotal Investment =", total)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment = " + str(total))

print("Result saved to portfolio.txt")