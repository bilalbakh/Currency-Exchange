import sys
## Notes:
# Functions:
# input_information
# calculate_exchanged_currency
# output_currency

# Global variables
EXCHANGE_RATES = {
    "EUR": 1.3,
    "USD": 1.5,
    "JPY": 0.6,
    "CHF": 1.9,
    "AUD": 3,
    "CAD": 2,
}

def input_information():
    '''Gets input from the user and returns the amount of money they have and the currency they want'''
    amount_of_money = input("How much money do you have? ")#
    currencies = list(EXCHANGE_RATES.keys())
    print("We offer the following currencies: " + str(currencies))
    desired_currency = input("What currency would you like? ")

    # Validate the input based on our preconditions
    money_integer = int(amount_of_money)
    try:
        money_integer = int(amount_of_money)
    except ValueError:
        sys.exit("Sorry, you must enter a number.")
    if money_integer > 100000 or money_integer < 10:
        sys.exit("Sorry, your amount must be more than £10 or less than ")
def calculate_exchanged_currency():
    pass

def output_currency():
    pass





input_information()