from classroom import Classroom
from student import Student
import math

def mean_mark(classroom : Classroom) -> int:
    total = 0
    for student in classroom.class_details:
        total += student[3]
    
    mean = total / len(classroom.class_details)
    
    return mean


def class_median(classroom : Classroom) -> int:
    list_of_marks = []
    
    for student in classroom.class_details:
        list_of_marks.append(student[3])

    # Using selection sort
    n = len(list_of_marks)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if list_of_marks[j] < list_of_marks[min_index]:
                min_index = j

        if min_index != i:
            list_of_marks[i], list_of_marks[min_index] = list_of_marks[min_index], list_of_marks[i]       

    mid_point = n // 2
    
    if n % 2 == 0:
        median = (list_of_marks[mid_point - 1] + list_of_marks[mid_point]) / 2
    else:
        median = (list_of_marks[mid_point])
    
    return median


def std_deviation(classroom : Classroom) -> float:
    divisor = len(classroom.class_details)
    dividend = 0

    for student in classroom.class_details:
        dividend += (student[3] - mean_mark(classroom))**2

    std_dev = math.sqrt(dividend / divisor)
    
    return std_dev


def best_student(classroom : Classroom) -> list[Student]:
    best_student = classroom.class_details[0]
    best_mark = 0
    
    for student in classroom.class_details:
        if student[3] > best_mark:
            best_mark = student[3]
            best_student = student

    return best_student


def worst_student(classroom : Classroom) -> list[Student]:
    worst_student = classroom.class_details[0]
    worst_mark = 100
    
    for student in classroom.class_details:
        if student[3] < worst_mark:
            worst_mark = student[3]
            worst_student = student
        
    return worst_student