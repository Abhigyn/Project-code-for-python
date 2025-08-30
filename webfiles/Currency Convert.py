import decimal
import requests  # (you had it, keeping it even if unused)

with open(r"i:\Study\Golu lession\Python      Projects\docs\Currency.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

CurrencyDict = {}
for line in lines:
    parsed = line.strip("\n").split("\t")
    CurrencyDict[parsed[0]] = decimal.Decimal(parsed[1])  # store as Decimal

amount = decimal.Decimal(input("Enter The Amount:\n"))
print("Enter The Amount you want to covert it;\n")
[print(item) for item in CurrencyDict.keys()]

currency = input("Please Enter One of These Values:\n")

# Multiply using Decimal instead of float
print(f"{amount} INR is equal to {amount * CurrencyDict[currency]} {currency}:\n")
