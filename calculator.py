
# Creating a calculator: ask the user for two numbers and an operator
# and based on their choice perform the correct operation.
# Display the result to the user and ask them if they wish to continue.

# If so, ask them again for two numbers and an operator,
# display result and do this on repeat
# until they do not wish to participate any more
# (maybe they press a special character -i.e. 'x'- to exit)

try2 = input("Would you like to try a calculation? Y/N ").upper()

while try2 == "Y":
    num1 = float(input("Please input number 1: "))
    num2 = float(input("Please input number 2: "))
    operator = input("Please input an operator: ")

    if operator == "+":
        print("The result is: " + str(round(num1 + num2, 2)))
    elif operator == "-":
        print("The result is: " + str(round(num1 - num2, 2)))
    elif operator == "*":
        print("The result is: " + str(round(num1 * num2, 2)))
    elif operator == "/":
        print("The result is: " + str(round(num1 / num2, 2)))
    else:
        print("Sorry, you must input one of the following operators: +, -, *, / ")
    try2 = input("Would you like to try another calculation? Y/N ").upper()

else:
    print("Thank you for using this python calculator!")

