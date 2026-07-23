# Input() variable assignments.
first_name = input("First Name: ")
last_name = input("Surname: ")
bio_message = input("Tell us about yourself: ").strip()

# Profile header and discription variables.
full_name = first_name.title() + ' ' + last_name.title()
username = f'{first_name[0].lower()}{last_name.lower()}'
bio_replacement = bio_message.replace("I am", "I'm")

# Profile output/ display.
print(f"{full_name}")
print(f"Username: {username}")
print(f"{bio_replacement}")
print(f"Bio length: {len(bio_message)} characters.")