# Part 1: List of Students

    # using list_comprehention
def find_top_student(students): 
    topStudent = [student for student in students if student["score"]>=80]
    return topStudent


    # using for loop
    
    # topStudents = []
    # for student in students:
    #   if student["score"]>=80:
    #     topStudents.append(student)
    # return topStudents


def print_students_names(students):
    top_students = []
    for student in students:
        if student["score"]>=80:
            top_students.append(student["name"])
    return top_students


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": 92},
    {"name": "Diana", "score": 67},
    {"name": "Eve", "score": 88}
] 

top_students_result = find_top_student(students)
print('top_students_result = ', top_students_result)

top_student = print_students_names(students)
print('top_students_name = ', top_student)
 







# Task:
# Create a list of dictionaries where each dictionary represents a student with name and score attributes.
# Write a function find_top_students that takes this list and returns the names of students who scored above 80.
# Print the names of the top students.







