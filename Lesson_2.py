# Tracking individual letters
name = "Kagisho"

print(name[0])
print(name[-1])
print(name[2])

# Using string methods
town = "  Cape Town  "
print(town.upper())
print(town.strip())

# Email generating system 
first_name = input("First Name: ").strip()
last_name = input("Last Name: ").strip()

username = f"{first_name[0].lower()}{last_name.lower()}"

print(f"Your email adress is {username}@gmail.com ")