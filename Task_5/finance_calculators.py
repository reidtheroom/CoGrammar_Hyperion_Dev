import math

# choose investment or bond
while True:

    print(''' 
          investment - to calculate the amount of interest you'll earn on your investment
          bond - to calculate the amount you'll have to pay on a home loan
          ''')
    choice = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

    # if they choose investment
    if choice == "investment":
        deposit = round(float(input("How much money are you depositing? £")), 2)
        # input valid percentage for interest
        interest_rate = None
        while interest_rate is None:
            try:
                interest_rate = float(input("What is your interest rate? "))
                if interest_rate <= 0 or interest_rate > 100:
                    raise ValueError
            except ValueError:
                print("Please ensure you have entered a valid numeric value.")
                interest_rate = None
                

        years = int(input("How many years are you investing? "))

        interest_input = input("Do you want to calculate simple or compound interest? ")
        interest = interest_input.lower()
        # decimal mulitplier for interest percentage
        r = interest_rate / 100 

        # choosing simple interest
        if interest == "simple":
            calculate_simple_interest = deposit * ((1 + r) * years)
            simple_interest = round(calculate_simple_interest, 2)
            print(f"Your total investment is £{simple_interest}")

        # choosing compound interest
        elif interest == "compound":
            calculate_compound_interest = deposit * math.pow((1 + r), years)
            compound_interest = round(calculate_compound_interest, 2)
            print(f"Your total investment is £{compound_interest}")

        break

    # if they choose bond
    elif choice == "bond":

        present_value = round(float(input("What is the present value of the house? £")), 2)

        interest_rate = None
        while interest_rate is None:
            try:
                interest_rate = float(input("What is your interest rate? "))
                if interest_rate <= 0 or interest_rate > 100:
                    raise ValueError
            except ValueError:
                print("Please ensure you have entered a valid numeric value.")
                interest_rate = None
        
        months = int(input("How many months do you plan to take to repay the bond? "))
        # decimal multiplier per month
        monthly_interest_rate = (interest_rate / 100) / 12

        calculate_repayment = (monthly_interest_rate * present_value) / (1 - ((1 + monthly_interest_rate)**(-months)))
        repayment = round(calculate_repayment, 2)
        print(f"Your monthly repayment is £{repayment}.")

        break


    else:
        print("Invalid entry, try again.")

