##
# Student Directory

#functions
def menu():
    """print menu"""
    
    print("""
    Options:
    1. Add a student
    2. Change age
    3. Delete
    4. List all eye colours
    5. Search by eye colour
    6. Search for student and show their eye colour
    7. QUIT""")

def force_number(message):
    """Force number function"""
    
    # loop until integer entered
    while True:

        # ask user for interger accounting for value error
        try:
            number = int(input(message))
            return number
            
        except ValueError:
            print("You must enter a integer")

def valid_option(option):
    """Check if option is within range"""

    #constants
    MAX_OPTION = 7
    MIN_OPTION = 1

    # check if option is within min and max
    if option < MIN_OPTION or option > MAX_OPTION:

        # change valid to false becuase option is not within range
        valid = False
        print("That is not an available option")
    else:
        valid = True

    #return valid
    return valid

def add():
    """add a student to dictionary"""

    # ask user for relevant information
    name = input("Enter student name: ").strip().title()
    eye_colour = input("Enter students eye colour: ").strip().lower()
    age = force_number("Enter students age: ")

    # add student to dictionary
    students.append(dict())

    # loop through student dictionaries
    for student in students:
        
        if student.get("name") == None:
            student["name"] = name
            student["eye colour"] = eye_colour
            student["age"] = age
            
    print("Student added")

def change_age():
    """change a students age"""
    
    change = False

    # ask user for students name
    student_change = input("Enter the name of the student whose age you want to change: ").strip().title()

    #loop through student dictionaries
    for student in students:
        
        if student.get("name") == student_change:
            age = force_number("Enter students age you want to change it to: ")
            student["age"]  = age
            change = True
            break

    # check if anything has been changed if not student is not in dictionary
    if change == False:
        print("That student is not in the dictionary")
        

def delete():
    """delete a student"""
    change = False

    # ask user for students name
    student_delete = input("Enter name of student you want to delete: ").strip().title()

    #loop through student dictoinary
    for student in students:
        
        if student.get("name") == student_delete:
            print("You have removed {} from the list".format(student_delete))
            students.remove(student)
            change = True
            break

    # check if anything has been changed
    if change == False:
        print("That student is not in the dictionary")

def list_eye_colours():
    """list all eye colours"""

    # create emtpy list to append to
    all_eye_colours = []

    # loop through student dicitonaries
    for student in students:
        
        eye_colour = student["eye colour"]
        if eye_colour not in all_eye_colours:
            all_eye_colours.append(eye_colour)
            
    print("Eye colours in list:")
    
    # print all eye colours
    for colour in all_eye_colours:
        print(colour)

def search_eye_colour():
    """enter an eye colour and return students who have that eye colour"""
    valid = False

    # create empty list to append to
    students_with_colour =[]

    # ask user for eye colour
    search_colour = input("Enter eye colour you want to know what students have: ")

    # loop through student dictionaries
    for student in students:
        
        if search_colour in student.values():
            student_name = student["name"]
            students_with_colour.append(student_name)
            valid = True

    # check if eye colour exsits in dictionaries
    if valid == True:
        print("The students with that eye colour are:")
        for student in students_with_colour:
            print(student)

    # if eye colour is not in any dictionary
    else:
        print("That eye colour is not in the dictionary")

def search_student_colour():
    """enter student and return their eye colour"""
    valid = False

    # ask user for student name
    student_name = input("Enter name of student you want to know the eye colour of: ").strip().title()

    # loop through student dicitonarys
    for student in students:

        
        if student.get("name") == student_name:
            print("{}'s eye colour is {}".format(student_name, student["eye colour"]))
            valid = True
            break

    # if student is not in dictionary
    if valid is False:
        print("That student is not in the dictionary")
            
# main routine
if __name__ == "__main__":
    option = 0
    students = [
        {"name": "Harini", "eye colour": "brown" , "age": 16},
        {"name": "Anna", "eye colour": "blue", "age": 15,},
        {"name": "Korimako", "eye colour": "brown", "age": 16},
        {"name": "Fleur", "eye colour": "blue", "age": 16}
    ]

    print("Welcome to the student directory")
    while option != 7:

        valid = False
        menu()
        while valid is False:
            option = force_number("Enter option: ")
            valid = valid_option(option)
    
        if option == 1:
            add()
    
        elif option == 2:
            change_age()
    
        elif option == 3:
            delete()
    
        elif option == 4:
            list_eye_colours()
    
        elif option == 5:
            search_eye_colour()
    
        elif option == 6:
            search_student_colour()

        elif option == 7:
            print("Quitting...")