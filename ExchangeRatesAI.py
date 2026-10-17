
import csv

class ExchangeRates:
    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.rate = float(row["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate
        else:
            return amount


# Read the exchange rate from the CSV file
exchange = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

# Ask the user for the amount and currencies
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency to convert from (USD or CAD): ").upper()
to_currency = input("Enter the currency to convert to (USD or CAD): ").upper()

# Convert the amount
converted_amount = exchange.convert(amount, from_currency, to_currency)

# Display the result
print(f"${amount:,.2f} {from_currency} = ${converted_amount:,.2f} {to_currency}")
