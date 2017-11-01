students = [] # Master list of students

def create_student():
    name = input("Enter student's name: ")
    student = {
        'name': name,
        'marks': []
    }
    return student

def add_score(student, score):
    student['marks'].append(score)

def calculate_avg_score(student):
    scores = student['marks']
    list_size = len(scores)
    if list_size == 0:
        return 0

    total = sum(scores)
    return total/list_size

def print_student_details(student):
    print("{}, average score: {}.".format(student['name'], calculate_avg_score(student)))

def print_details():
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")

    while selection != 'q':
        if selection == 'p':
            print_details()
        elif selection == 's':
            student = create_student()
            students.append(student)
        elif selection == 'a':
            try:
                student_id = int(input("Enter the student id:"))
                student = students[student_id]
                score = int(input("Enter score for the student: ".format(student['name'])))
                add_score(student, score)
            except Exception:
                print("Incorrect student ID")

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")


menu()
