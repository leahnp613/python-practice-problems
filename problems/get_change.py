# Create a fxn named “get_change” that gets user input for a cash total. Calculate the total number of Quarters / Dimes / Nickels / Pennies for the change exchange. The fxn should return a print of those calculations. 
# Note: make this a “hungry” fxn that gets the largest number of large coins and smallest number of small coins. 
# Note: validate the input to ensure proper input from the user, cover all edge case entries, do not allow breaking errors

# Input: 1.49
# Output: 
# Total Cents: 149
# Total Quarters: 5
# Total Dimes: 2
# Total Nickels: 0
# Total Pennies: 4

def get_change():
    while True:
        try:
            cash_total = float(input("Enter the cash total: "))
            if cash_total < 0:
                raise ValueError("Cash total cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid cash total.")

    total_cents = int(cash_total * 100)
    total_quarters = total_cents // 25
    total_cents %= 25
    total_dimes = total_cents // 10
    total_cents %= 10
    total_nickels = total_cents // 5
    total_cents %= 5
    total_pennies = total_cents

    print("Total Cents:", total_cents)
    print("Total Quarters:", total_quarters)
    print("Total Dimes:", total_dimes)
    print("Total Nickels:", total_nickels)
    print("Total Pennies:", total_pennies)

get_change()


    
        