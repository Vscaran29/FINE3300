principal=float(input("Input the starting principal for the mortgage: "))
rate=float(input("Input the annual rate in % for the mortgage: "))
amortization=float(input("Input the amortization period the mortgage in years: "))

# Create a single function that calculates the mortgage payment
def mortgage_payment(principal,rate,amortization):
    # Convert the % recieved as a input into a float number
    rate=rate/100

    
    # Calculate the number of payments for each different period
    monthly=amortization*12
    semi_monthly=amortization*24
    bi_weekly=amortization*26
    weekly=amortization*52

    # Get the rate for each scenario(using the formulas provided in the assignment sheet)
    monthly_rate=(((1+rate/2)**(2/12))-1)
    semi_monthly_rate=((1+rate/2)**(2/24))-1
    bi_weekly_rate=((1+rate/2)**(2/26))-1
    weekly_rate=((1+rate/2)**(2/52))-1

    # Begin to calculate the payments for different schedules
    monthly_payment=((((monthly_rate*(1+monthly_rate)**monthly))/(((1+monthly_rate)**monthly)-1)))*principal
    semi_monthly_payment=((((semi_monthly_rate*(1+semi_monthly_rate)**semi_monthly))/(((1+semi_monthly_rate)**semi_monthly)-1)))*principal
    bi_weekly_payment=((((bi_weekly_rate*(1+bi_weekly_rate)**bi_weekly))/(((1+bi_weekly_rate)**bi_weekly)-1)))*principal
    weekly_payment=((((weekly_rate*(1+weekly_rate)**weekly))/(((1+weekly_rate)**weekly)-1)))*principal
    
    # Can use the shortcut for the accelerated payments as the accelarated payments are a percentage of the monthly payment

    acel_bi_weekly_payment=monthly_payment/2
    acel_weekly=monthly_payment/4

    print("Based on the Parameters of the mortgage the following would be your different options for making payments:")

    print("Monthly Payment:$ ",round(monthly_payment,2))
    print("Semi Monthly Payment:$ ",round(semi_monthly_payment,2))
    print("Bi Weekly Payment:$ ",round(bi_weekly_payment,2))
    print("Weekly Payment:$ ",round(weekly_payment,2))
    print("Accelerated Bi Weekly Payment:$ ",round(acel_bi_weekly_payment,2))
    print("Accelerated Weekly Payment:$ ",round(acel_weekly,2))

# Execution of the variables for question b in the assingment based on the user input
mortgage_payment(principal,rate,amortization) 

