# -*- coding: utf-8 -*-
"""
Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# National Bank of Canada: 327
# Toronto-Dominion Bank: 302
# Royal Bank of Canada: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# Canadian Imperial Bank of Commerce: 83
# TD Bank: 108
# Bank of Montreal: 67
# Capital One: 47
# FNB Corporation: 4
# Laurentian Bank of Canada: 3
# Ally Financial: 12
# Montreal Trust Company: 145
# Canadian Western Bank: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)
banks = {
    "National Bank of Canada": 327,
    "Toronto-Dominion Bank": 302,
    "Royal Bank of Canada": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "Canadian Imperial Bank of Commerce": 83,
    "TD Bank": 108,
    "Bank of Montreal": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "Laurentian Bank of Canada": 3,
    "Ally Financial": 12,
    "Montreal Trust Company": 145,
    "Canadian Western Bank": .97
}
# @TODO: Change the market cap for 'Royal Bank of Canada'
banks['Royal Bank of Canada'] = 170

# @TODO: Add a new bank and market cap pair
banks['Scotiabank'] = 33

# @TODO: Remove a bank from the dictionary
del banks['Montreal Trust Company']

# @TODO: Initialize metric variables
total_market_capitalization = 0
banks_count = 0
banks_average = 0

# @TODO: Initialize minimum key-value pair
minimum_key = ""
minimum_value = 0

# @TODO: Initialize maximum key-value pair
maximum_key = ""
maximum_value = 0

# Mega Cap: Firms with a market capitalization over $300 billion.
# Large Cap: Firms with a market capitalization over 10 billion. ...
# Mid Cap: A market capitalization between $2 and $10 billion.
# Small Cap: A market capitalization between $300 million and $2 billion.

# @TODO: Initialize market cap lists
mega_cap = []
large_cap = []
mid_cap = []
small_cap = []

# @TODO: Iterate over key-value pairs of the dictionary
for bank_name, market_cap in banks.items():
   
    # @TODO: Calculate sum of market caps and number of banks in the dictionary
    total_market_capitalization += market_cap
    banks_count += 1

    # @TODO: Logic to determine min value and associated key
    if minimum_value > market_cap:
        minimum_value = market_cap
        minimum_key = bank_name
        
    # @TODO: Logic to determine max value and associated key
    if maximum_value < market_cap:
        maximum_value = market_cap
        maximum_key = bank_name

    # @TODO: Group banks by categories of market caps
    if market_cap >= 300:
        mega_cap.append(bank_name)
    elif market_cap >= 10 and market_cap < 300:
        large_cap.append(bank_name)
    elif market_cap >= 2 and market_cap < 10:
        mid_cap.append(bank_name)
    elif market_cap < 2:
        small_cap.append(bank_name)

# @TODO: Calculate average market cap of banks in the dictionary
banks_average = total_market_capitalization / banks_count

# @TODO: Print the metrics
print(f"Total Market Capitalization: {int(total_market_capitalization)}")
print(f"Total Number of Banks: {banks_count}")
print(f"Average Market Capitalization: {banks_average:.2f}")
print(f"Largest Bank: {maximum_key}")
print(f"Smallest Bank: {minimum_key}")
print("-------------------------------------------")
print(f"Mega Cap Banks: {mega_cap}")
print(f"Large Cap Banks: {large_cap}")
print(f"Mid Cap Banks: {mid_cap}")
print(f"Small Cap Banks: {small_cap}")