# initialize global variables
annual_salary = None
annual_salary_question = "Enter your annual salary [default = 120000]: "
portion_saved = None
portion_saved_question = "Enter the percent of your salary to save, as a decimal [default = 0.1]: "
r = None
r_question = "Enter the expected annual rate of return [default = 0.04]: "
total_cost = None
total_cost_question = "Enter the total cost of your dream home [default = 1000000]: "
portion_down_payment = None
portion_down_payment_question = "Enter the portion required for down payment [default = 0.25]: "
resume = True

while resume:
    def request_info(value, question, default):
        while not isinstance(value, float):
            value = input(question) or default
            try:
                value = float(value)
            except:
                print("Invalid input. Please try again!")
                continue
        return value


    # collect user input about income and home statistics. Include defaults, check for invalid entry,
    # and convert to usable data types
    print("Welcome to the dream home down payment calculator! Please answer a few questions...")


    annual_salary = request_info(annual_salary, annual_salary_question, 120000)

    portion_saved = request_info(portion_saved, portion_saved_question, .1)

    r = request_info(r, r_question, .04)

    total_cost = request_info(total_cost, total_cost_question, 1000000)

    portion_down_payment = request_info(portion_down_payment, portion_down_payment_question, .25)

    down_payment = total_cost * portion_down_payment

    print(f"\n\nHere's what you entered:\n"
          f"Annual salary:" f"{int(annual_salary)}\n"
          f"Percentage of salary saved: {portion_saved * 100} %\n"
          f"Expected rate of return: {r * 100} %\n"
          f"Cost of your dream home: {int(total_cost)}\n"
          f"Down payment required: {portion_down_payment * 100} %\n")

    # Determine number of months required to meet down payment by looping through and adding previous month's return on
    # investment + monthly savings, then incrementing the number of months after each loop until savings >= down payment

    def calc_months():
        months = 0
        current_savings = 0

        while current_savings <= down_payment:
            current_savings += (current_savings * r / 12) + (annual_salary / 12 * portion_saved)
            months += 1
            # print(f"Month {months}: ${int(current_savings)}")
        return months

    total_months = calc_months()

    # print(f"Number of months: {total_months}\n")
    print(f"It will take {total_months} months to save {int(down_payment)} dollars for a down payment!\n")

    while True:
        resume_app = input("Would you like to run the program again? (y/n): ")
        if resume_app.lower() == "n":
            print("Thanks for using the dream_home_down_payment calculator! Try saying that three times fast. Bye now!")
            resume = False
            break
        if resume_app.lower() == "y":
            annual_salary = None
            portion_saved = None
            r = None
            total_cost = None
            portion_down_payment = None
            break
        else:
            print("Please enter a valid response!")
            continue






