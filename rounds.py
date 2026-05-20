print("✖️➕➖➗Welcome to Basic Facts Quiz!!✖️➕➖➗")
print(" Do you want instructions?")

    # Main Routine


def yes_no(question):
    """Checks users enter yes / no"""

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if  response == "yes" or  response =="y" :
            return "yes"
        elif  response == "no" or response =="n" :
            return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Get the questions correct!   
    """)

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want instructions? ")

 # Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print ("Program continues")




# Ask user for number of questions
def int_check(question, exit_code=None):
    """ checks for an integer more than 0 (allows <enter>)"""


    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)


        # check for infinite mode / exit code
        if response == exit_code:
            return exit_code


        try:
            # tries to make the response into an integer
            response = int(response)


            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response


        except ValueError:
            # if the response is not an integer, displays an error
            print(error)




    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()



        for var_item in valid_ans:
            # check if the user response is a word in the list
            if var_item == user_response:
                return var_item



            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == var_item [0]:
                return var_item

# Ask user for number of rounds
rounds_wanted = int_check("How many rounds?","")



