Student = input("Student Name & surname: ")
Computer_Science = float(input("Computer Science mark: "))
Mathematics = float(input("Mathematics mark: "))
Networking = float(input("Networking mark: "))

total_comp_sci = (100)
total_math = (100)
total_net = (100)

Total_grade = Computer_Science + Mathematics + Networking
Max_grade = total_comp_sci + total_math + total_net
Average_grade = float((Total_grade/ Max_grade) * 100)
Subjects = [("Computer Science", float(Computer_Science)), ("Mathematics", float(Mathematics)), ("Networking", float(Networking))]

print(f"{Student.upper()}'s COMPUTER SCIENCE mark: {Computer_Science}")
print(f"{Student.upper()}'s MATHEMATICS mark: {Mathematics}")
print(f"{Student.upper()}'s NETWORKING mark: {Networking}")



if Average_grade >= 80:
    print(f"Average grade: {round(Average_grade, 2)} - Symbol: A - Status: PASS !!!")
elif Average_grade >= 70:
    print(f"Average grade: {round(Average_grade, 2)} - Symbol: B - Status: PASS !!!")
elif Average_grade >= 60:
    print(f"Grade average: {round(Average_grade, 2)} - Symbol: C - Status PASS !!!")
elif Average_grade >= 50:
    print(f"Grade average: {round(Average_grade, 2)} - Symbol: D - Status: PASS !!!")
elif Average_grade < 50:
    print(f"Grade average: {round(Average_grade, 2)} - Symbol: F - Status: FAIL !!!")
else:
    print("Please fill in grades !!!")

for name, mark in Subjects:
    if Average_grade >= 50 and mark < 40 :
       print(f"{name.upper()}, needs intervention (Overall Status: PASS).")


for name, mark in Subjects:
    if mark < 40 or mark == 0:
        print( name, f"needs intervention")

    