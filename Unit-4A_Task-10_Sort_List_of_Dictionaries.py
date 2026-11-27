students = [
    {"name": "sanjana", "marks": 97},
    {"name": "hema", "marks": 88},
    {"name": "nutan", "marks": 72},
]

by_marks = sorted(students, key=lambda d: d["marks"])
print("By marks ascending:", by_marks)

by_marks_desc = sorted(students, key=lambda d: d["marks"], reverse=True)
print("By marks descending:", by_marks_desc)



