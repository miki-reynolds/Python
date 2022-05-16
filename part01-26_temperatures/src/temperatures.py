f = float(input("Please tye in a temperature (F): "))
c = ((f-32) * 5 / 9)
print(f"{f} degrees Fahrenheit equals {c} degrees Celsius")

condition = c < 0
if condition:
    print("Brr! It's cold in here!")
