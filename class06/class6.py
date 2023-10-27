# grade: Union[int, float] = 7.0
# print(grade)

from typing import Union 

# alias
PerType = Union[float, int]

percentages: list[PerType] = [88, 82.3, 90, 54, 65.72]

grades: list[str] = []

for student_percentage in percentages: 
    if student_percentage >= 90:
        grade = "A+"
        grades.append(grade)
    elif student_percentage >= 85:
        grade = "A"
        grades.append(grade)
    elif student_percentage >= 80:
        grade = "B+"
        grades.append(grade)
    elif student_percentage >= 75:
        grade = "B"
        grades.append(grade)
    elif student_percentage >= 70:
        grade = "C+"
        grades.append(grade)
    elif student_percentage >= 65:
        grade = "C"
        grades.append(grade)
    elif student_percentage >= 60:
        grade = "D"
        grades.append(grade)
    else:
        grade = "Fail"
        grades.append(grade)
print(grades)

#zipping

print(list(zip(percentages, grades)))
