contact = []

friends_contact = { "Lizwi":" 0720601502", "Xo": "0724391800", "Al": "0691857980"}

contact_search = input("Enter name to search: ").title().strip()
if contact_search in friends_contact:
    print(f"Phone number for {contact_search}: {friends_contact[contact_search]}")
else:
    print(f"Contact '{contact_search}' not found.")