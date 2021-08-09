from art import logo
import os
print(logo)

response = "yes"
biders = {}
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


while response == 'yes':
    name = input("What is your Name ? : ")
    bid = input("What is your Bid ? : $")
    biders[name] = bid
    response = input("Are there any other bidders? Type 'yes' or no ? ")
    clearConsole()

win_key = max(biders, key=biders.get)
print(f"The Highest Bider is {win_key} with amount of ${biders[win_key]}.")