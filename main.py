from classroom import Classroom
from student import Student
from teacher import Teacher
import statistical_values 
from art import text2art


def startup_screen():
    border = "=" * 177
    formatted_title = text2art("CLASS DATA CALCULATOR", font = 'standard')
    centered_lines = "\n".join(line.center(177) for line in formatted_title.split("\n"))
    return f"{border}\n{centered_lines}\n{border}"


def program_start():
    print(startup_screen())
    try:
        class_ID, class_size, number = input("Enter the details of the classroom: ").split(" ")
        token = class_ID, class_size, number
        
        class_ID = int(class_ID)
        class_size = int(class_size)
        number = int(number)
    
        classroom = Classroom(class_ID, class_size, number)
        
        print(classroom.__str__())
        
        
    except ValueError:
        print("The values are all numbers and not letters or characters.")
        
    print(classroom.get_class_details())

    i = 0
    while True:
        token = input("Enter Student details: ")
        if token == "I am done":
            break
            
        try:
            SID, first_name, last_name, age, mark = token.split(" ")

            SID = int(SID)
            age = int(age)
            mark = float(mark)
            
            students = Student(SID, first_name, last_name, age, mark)

            print(students.__str__())
            classroom.adding_students(students)
            
            i += 1
            
        except ValueError:
            print("Note that the Student ID, age and mark must be a number. Please enter again.")
            
    print(classroom.get_class_details())
    grades = input("Would you like to calculate their grades? ")
    if grades.lower() == "yes":
        student_grades = ""
        for i in range(classroom.get_number_of_students()):
            students.set_grade()
            student_grades += f"{students.get_grade()}\n"
        print(student_grades)


if __name__ == "__main__":
    program_start()