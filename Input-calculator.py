print("Write first number symbol second number and seporate with space")
input_calculation = input("")  # Asking for the calcuation

output_calcluation = input_calculation.split(" ")
# splitting the input_calculation stuff (using space " " ) and making the result output_calcluation

num1 = float(output_calcluation[0])
symbol = output_calcluation[1]
num2 = float(output_calcluation[2])

# Calculating the input
if symbol == "-":
    print(num1 - num2)
elif symbol == "+":
    print(num1+num2)
elif symbol == "/":
    print(num1/num2)
elif symbol == "*":
    print(num1*num2)
else:
    print("Invalid Symbol")
