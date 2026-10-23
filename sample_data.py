import csv

students = [
    (101, "Abebe", "Git Basics", 94.5),
    (102, "Sara", "Branching", 88.0),
    (103, "Dawit", "Remote Repos", 91.0),
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Module", "Score"])
    writer.writerows(students)

print("students.csv created")
