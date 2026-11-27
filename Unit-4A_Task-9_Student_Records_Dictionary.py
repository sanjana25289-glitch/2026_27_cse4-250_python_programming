name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

student = {"name": name, "marks": marks, "grade": grade}
print("Record:", student)
for key, value in student.items():
    print(f"{key}: {value}")



    