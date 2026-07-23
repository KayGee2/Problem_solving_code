# Variable inputs.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

# Outta Variable Table
Addition = num1 + num2 
Subtraction = num1 - num2
Multiplication = num1 * num2

print(f"The answer Added: {round(Addition, 2)}")
print(f"The answer Subtracted: {round(Subtraction, 2)}")
print(f"The answer Multiplied: {round(Multiplication, 2)}")

# Divide by 0 Condition
if num2 == 0:
    print(f"Sorry, no dividing by zero! 😮")
else:
    # Inner Variable Table
    Division = num1 / num2
    Squareroot = num1 // num2
    Percentage = num1 % num2 

# Display table.
    print(f"The answer Divided: {round(Division, 2)}")
    print(f"The answer without any decimals: {round(Squareroot, 2)}")
    print(f"The remainders in the answer: {round(Percentage, 2)}")

