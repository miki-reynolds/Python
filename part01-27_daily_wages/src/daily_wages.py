h_wage = float(input("Hourly wage: "))
h_worked = float(input("Hours worked: "))
day = input("Day of the week: ")
condition = day == "Sunday"
if condition:
    print(f"Daily wages: {2 * h_wage * h_worked} euros")
condition = day != "Sunday"
if condition:
    print(f"Daily wages: {h_wage * h_worked} euros")
