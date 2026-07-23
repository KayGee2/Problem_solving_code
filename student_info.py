first_name = input("First Name: ")
last_name = input("Surname: ")
age = input("Age: ")
favourite_num = input("Favourite number: ")

types = [("first name", first_name), ("last name", last_name), ("age", int(age)), ("favourite number", float(favourite_num))]

for label, value in types:
    print(label, type(value))

age_months = int(age) * 12
fav_num = float(favourite_num)


title_name =  first_name.title() + " " + last_name.title()
print(title_name)


print(f"Welcome, {first_name.upper()} {last_name.upper()}")

print(age_months)
print(round(fav_num, 2))