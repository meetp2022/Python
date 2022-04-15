# Get the loan details 


money_owed = float(input("How much money do you owe, in rupees?\n")) #Rs.50,000
roi = float(input("What is the annual rate of interest?\n")) #3
payment = float(input("What will your monthy payment be, in rupees?\n")) #Rs.1000
months = int(input("How many months do you want to see the results for?\n")) #24

# Divide ROI by 100 to make it a percent, then divide by 12 to make monthly

monthly_rate = roi/100/12


for i in range(months):

    # Add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    # Make payment
    money_owed = money_owed - payment

    # Print the results after this month
    print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
    print("Now I owe", money_owed)