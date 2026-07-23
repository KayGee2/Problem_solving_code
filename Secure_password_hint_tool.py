print("   Please Enter your password  ")

password = input("Password: ").strip()

password_hint_1 = password[0].upper()
password_hint_2 = password[-1].upper()

print(f"Your password hint: It starts with {password_hint_1} and ends with {password_hint_2}")