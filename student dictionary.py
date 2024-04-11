##
# Student Directory

# functions
def menu():
    """print menu"""

    # print menu
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
            print("You must enter an integer")

def valid_option(option):
    """Check if option is within range"""

    # constants
    MAX_OPTION = 7
    MIN_OPTION = 1

    # check if option is within min and max
    if option < MIN_OPTION or option > MAX_OPTION:

        # change valid to false becuase option is not within range
        valid = False
        print("That is not an available option")
        
    # if option is in range set vaild to true
    else:
        valid = True

    #return valid
    return valid

def add_student(name, eye_colour, age):
    """add a student to dictionary"""
    
    # append new dictionary to list
    students.append(dict())

    # loop through student dictionaries
    for student in students:

        # find dictionary that is empty and add users information
        if student.get("name") == None:
            student["name"] = name
            student["eye colour"] = eye_colour
            student["age"] = age
            
    print("Student added")

def change_age(student_change):
    """change a students age"""
    
    change = False

    # loop through student dictionaries
    for student in students:

        # find which dictionary contains the student the user wants to change the age of
        if student.get("name") == student_change:

            #forcing user to enter age as interger and change chosen student age to that
            age = force_number("Enter students age you want to change it to: ")
            student["age"]  = age
            print("{} age has been changed".format(student["name"]))

            #record that something has been changed
            change = True


    # if nothing has been changed student is not in dictionary
    if change == False:
        print("That student is not in the dictionary")
        

def delete_student(student_delete):
    """delete a student"""
    change = False

    #loop through student dictoinary
    for student in students:

        # find dictionary for chosen student
        if student.get("name") == student_delete:

            #remove student's dictionary
            print("You have removed {} from the list".format(student_delete))
            students.remove(student)

            # change is true 
            change = True

    # check if nothing has been changed
    if change == False:
        print("That student is not in the dictionary")

def list_eye_colours():
    """list all eye colours"""

    # create emtpy list to append to
    all_eye_colours = []

    # loop through student dicitonaries
    for student in students:

        #  take students eye colour
        eye_colour = student["eye colour"]

        # if eye colour is not already in the list append it
        if eye_colour not in all_eye_colours:
            all_eye_colours.append(eye_colour)
            
    print("Eye colours in list:")
    
    # print all eye colours
    for colour in all_eye_colours:
        print(colour)

def search_eye_colour(search_colour):
    """enter an eye colour and return students who have that eye colour"""
    valid = False

    # create empty list to append to
    students_with_colour =[]

    # loop through student dictionaries
    for student in students:

        # check if student had chosen eye colour, if so add student name to list
        if search_colour in student.values():
            student_name = student["name"]
            students_with_colour.append(student_name)

            #record that eye colour has been found at least once
            valid = True

    # check if eye colour exists in dictionaries
    if valid == True:

        #print students in list
        print("The students with that eye colour are:")
        for student in students_with_colour:
            print(student)

    # if eye colour is not in any dictionary
    else:
        print("That eye colour is not in the dictionary")

def search_student_colour(student_name):
    """enter student and return their eye colour"""
    valid = False

    # loop through student dicitonarys
    for student in students:

        # check if student is the student user entered
        if student.get("name") == student_name:

            #print their eye colour
            print("{}'s eye colour is {}".format(student_name, student["eye colour"]))

            # record that student is in dictionary
            valid = True

    # if student is not in dictionary
    if valid is False:
        print("That student is not in the dictionary")
            
# main routine
if __name__ == "__main__":
    option = 0

    #dictionary of students
    students = [
        {"name": "Harini", "eye colour": "brown" , "age": 16},
        {"name": "Anna", "eye colour": "blue", "age": 15,},
        {"name": "Korimako", "eye colour": "brown", "age": 16},
        {"name": "Fleur", "eye colour": "blue", "age": 16}
    ]

    #welcome user
    print("Welcome to the student directory")

    #loop while user has not entered 7 to quit
    while option != 7:

        valid = False

        #print menu
        menu()

        #force user to enter vaild option
        while valid is False:
            option = force_number("Enter option: ")
            valid = valid_option(option)

        # do appropriate thing for each option
        if option == 1:
            
            # ask user for relevant information
            name = input("Enter student name: ").strip().title()
            eye_colour = input("Enter students eye colour: ").strip().lower()
            age = force_number("Enter students age: ")

            # run function with arguments
            add_student(name, eye_colour, age)
    
        elif option == 2:

            # ask user for students name
            student_change = input("Enter the name of the student whose age you want to change: ").strip().title()

            # run function with argument
            change_age(student_change)
            
        elif option == 3:

            # ask user for students name
            student_delete = input("Enter name of student you want to delete: ").strip().title()

            # run function with argument
            delete_student(student_delete)
    
        elif option == 4:
            list_eye_colours()
    
        elif option == 5:

            # ask user for eye colour
            search_colour = input("Enter eye colour you want to know what students have: ")

            # run function with argument
            search_eye_colour(search_colour)
    
        elif option == 6:

            # ask user for student name
            student_name = input("Enter name of student you want to know the eye colour of: ").strip().title()

            # run function with argument
            search_student_colour(student_name)

        elif option == 7:

            #option is 7 so program will stop looping
            print("Quitting...")