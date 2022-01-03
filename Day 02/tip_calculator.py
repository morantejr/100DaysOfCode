def tipCalc():
    bill = input("What was the total bill:\n $")

    FLOAT_BILL = float(bill)

    tip = input("What percentage tip would you like to give? 10, 12, 15?\n")

    FLOAT_TIP = float(tip) /100

    num_people = input("How many people are there to split?\n")

    INT_PEOPLE = int(num_people)

    bill_tip = FLOAT_BILL + (FLOAT_BILL * FLOAT_TIP)

    final = bill_tip / INT_PEOPLE

    print(f"Each person should pay: ${round(final,2)}")
tipCalc()
