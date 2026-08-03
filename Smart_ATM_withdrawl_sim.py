balance = float(input("Enter bank balance: R"))
withdrawl = float(input("How much would you like to withdraw: R"))

if withdrawl > balance:
    print("Declined. Insufficient funds!")
elif withdrawl <= 0:
    print("Invalid amount! you must withdraw more than R0.00")
else:
    balance -= withdrawl
    print(f"Withdrawal successful. Your new balance is: R{balance}")
