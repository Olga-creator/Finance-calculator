import math

# Program allows the user to access two different financial calculators: 
#  an investment calculator and a home loan repayment calculator. 

# Prompt user to choose calculator. Function lower() used to accept capitalised input
# Function strip() is used in order to remove any whitespaces in case if user input some
calculator_choice = input("""Choose either 'investment' or 'bond' from the menu below to proceed:
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
""")
calculator_choice = calculator_choice.lower().strip()
if calculator_choice == 'investment':
    # I assume that amount of money for deposit, etc will be entered as integer for simplification
    # Request user to enter deposit, rate and how many years they're planning on investing
    amount_money = int(input("What's the amount of money you're depositing? "))
    interest_rate = int(input("Please enter interest rate: "))
    years = int(input("Please enter the number of years you're planning on investing: "))
    interest = input("Please choose 'Simple' or 'Compound' interest: ") # I could add at the end of the sentance (simple or compaund) but not necessary
    interest = interest.lower().strip()
    if interest == 'simple':
        total_amount = amount_money * (1 + (interest_rate / 100) * years)
        print(f"The total amount of interest you'll earn on your investment when simple interest is applied is R{total_amount:.2f}.")
    elif interest == 'compound':
        # At the top of the file the line 'import math' is included in order to use math.pow to calculate total amount of interest
        # Total amount of interest is calculated based on the formula provided in the task
        total_amount = amount_money * math.pow((1 + (interest_rate / 100)), years)
        # The total amount is rounded to two dicimal points as no other instructions
        print(f"The total amount of interest you'll earn on your investment when compaund interest is applied is R{total_amount:.2f}.")
    else:
        # Comments will be displayed if the user doesn't chose an option from the menu
        print("You haven't chosen an option from the menu. Please contact clients service for further assistance.")
elif calculator_choice == 'bond':
    house_value = int(input("What's present value of the house? "))
    interest_rate = int(input("Please enter interest rate: "))
    months = int(input("Please enter the number of months over which the bond will be repaid: "))
    interest_rate = interest_rate/100/12
    # Total repayment amount calculated based on the formula provided in the task. I guessed that instead of '.' should be '*' in the formula in the task. 
    # Please check pdf. Formala is x = (i.P)/(1-(1+i)^(-n)) should be x = (i*P)/(1-(1+i)^(-n))?!?!
    # I have checked bond repayment calculator online and monthly amounts are the same as in my calculations
    # ref: line 40 formula correctness https://www.ooba.co.za/home-loan/bond-repayment-calculator/
    repayment = (interest_rate * house_value) / (1 - math.pow((1 + interest_rate), (-months)))
    print(f"The monthly repayment amount on a home loan is R{repayment:.2f}.")
else:
    print("You haven't chosen an option from the menu. Please contact clients service for further assistance.")
