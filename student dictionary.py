##
# Student Directory
# maybe change add to be seperate

def menu():
    print("""
    Options:
    1. Add
    2. Change age
    3. Delete
    4. List all eye colours
    5. Search by eye colour
    6. Search for student and show their eye colour""")

def force_number(message):
    "Force number function"
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("You must enter a integer")

def valid_option(option):
    """check if option is within range"""
    if option < 1 or option > 6:
        valid = False
        print("That is not an available option")
    else:
        valid = True

    return valid

def add():
    name = input("Enter student name: ").strip().title()
    eye_colour = input("Enter students eye colour: ").strip().title()
    age = force_number("Enter students age: ")
    students.append(dict())
    for student in students:
        if student.get("name") == None:
            student["name"] = name
            student["eye colour"] = eye_colour
            student["age"] = age

    print("Student added")

def change_age():
    student_change = input("Enter the name of the student whose age you want to change: ").strip().title()
    for student in students:
        
        if student.get("name") == student_change:
            age = force_number("Enter students age you want to change it to: ")
            student["age"]  = age
            break

        

def delete():
    student_delete = input("Enter name of student you want to delete: ").strip().title()
    print(student_delete)
    for student in students:
        if student.get("name") == student_delete:
            print("You have removed {} from the list".format(student_delete))
            students.remove(student)
            break
        

if __name__ == "__main__":
    students = [
        {"name": "Harini", "eye colour": "brown" , "age": 16},
        {"name": "Anna", "eye colour": "blue", "age": 15,},
        {"name": "Korimako", "eye colour": "brown", "age": 16},
        {"name": "Fleur", "eye colour": "blue", "age": 16}
    ]

    valid = False
    option = 0
    menu()
    while valid is False:
        option = force_number("Enter option: ")
        valid = valid_option(option)

    if option == 1:
        add()

    if option == 2:
        change_age()

    if option == 3:
        delete()

    print(students)
        
        

