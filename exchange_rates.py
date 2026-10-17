
'''
FINE 3300 - Assignment 1, Part 1
Currency Exchange Rate Calculator
'''

class ExchangeRates:
    def __init__(self, filename):
        # Open and read the exchange rate file
        with open(filename, 'r', encoding='utf-8-sig') as file:
            data = file.read()

        # Separate the data into rows
        rows = data.split('\n')

        # Remove the empty last row if there is one
        if rows[-1] == '':
            rows.pop()

        # Separate each row into columns
        rows = [row.split(',') for row in rows]

        # Find the USD/CAD column
        column = rows[0].index('FXAUSDCAD')

        # Get the exchange rate from the last row
        self.__rate = float(rows[-1][column])

    def convert(self, amount, from_currency, to_currency):
        if from_currency == 'USD' and to_currency == 'CAD':
            result = amount * self.__rate
        elif from_currency == 'CAD' and to_currency == 'USD':
            result = amount / self.__rate
        else:
            result = amount

        return result


if __name__ == '__main__':
    exchange = ExchangeRates('BankOfCanadaExchangeRate.2026.csv')

    amount = float(input('Enter the amount: '))
    from_currency = input('Convert FROM (USD or CAD): ').upper()
    to_currency = input('Convert TO (USD or CAD): ').upper()

    converted_amount = exchange.convert(amount, from_currency, to_currency)

    print('${:,.2f} {} = ${:,.2f} {}'.format(
        amount, from_currency, converted_amount, to_currency))
