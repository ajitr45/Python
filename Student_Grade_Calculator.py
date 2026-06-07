def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))
marks4 = float(input("Enter marks of Subject 4: "))
marks5 = float(input("Enter marks of Subject 5: "))

average = (marks1 + marks2 + marks3 + marks4 + marks5) / 5

grade = calculate_grade(average)

print("Average Marks:", average)
print("Grade:", grade)