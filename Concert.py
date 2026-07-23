Applicant = input("Applicant name: ")
Age = input("Age: ")
Band_name = input("Band: ")

Applicant_age = int(Age)

if Applicant_age < 18:
    print("Sorry concert tickets are only sold to people 18 and older 🔞")
else:
    print(f"Hey, {Applicant}!! Your tickets to see {Band_name} are booked successfully 🤘😝🤘! See you there 😉")

