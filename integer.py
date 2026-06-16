print("✖️➕➖➗Welcome to Basic Facts Quiz!!✖️➕➖➗")


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

import random
def string_checker(question, valid_ans=("yes", "no")):

    """ Check that users enter a valid word / first
    letter of the word based on a list of options. Defaults to yes / no."""

    error = f"Please enter a valid option from the following list: {valid_ans}"


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


        # print error if user does not enter something that is valid
        print(error)
        print()

# Ask user for number of questions
def int_check(question, exit_code=None):
    """ checks for an integer more than 0 (allows <enter>)"""


    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)



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


def quiz_compare(user, comp):
    # there is one way to get a correct answer
    if user == comp:
        result = "accurate"
    # if it is not correct, then it's wrong
    else:
        result = "inaccurate"
    return result


# Displays rounds
rounds_played = 0

# Main routine

# Initilise game variables
mode = "regular"
comp = 0
round_accurate = 0
round_inaccurate = 0


# Ask user for number of rounds
rounds_wanted = int_check("How many rounds?", "")
print("Rounds_wanted", rounds_wanted)

if rounds_wanted == "":
    # set rounds_wanted to a number for comparison later.
    rounds_wanted = 5

# Game loop starts here
while rounds_played < rounds_wanted:

    # Rounds headings
    rounds_heading = f"\n🦑🦑🦑 Round {rounds_played + 1} of {rounds_wanted} 🦑🦑🦑"

    print(rounds_heading)
    print()

    break

import random
# Generate random numbers

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

print("addition:")
print("num1 =", num1)
print("num2 =", num2)

# equations
addition = num1 + num2


user_addition = int(input("Enter the answer:"))

result = quiz_compare(user_addition, addition)
print(f" user answer:{user_addition} accurate answer:{addition}, result{result}")

# Adjust quiz correct/ wrong encounters and add results to quiz history

if result == "inaccurate":
    round_inaccurate += 1
    feedback = "inaccurate"


else:
    feedback = "Accurate"

# Set up round feedback output it user.
# Add it to the quiz history list (include the round number)

    round_feedback = f"{user_addition} vs {addition}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {result}"
    print(result)

    # Loop until we have a winner...
    print()
    input("Press <enter> to continue this round\n")









rounds_played += 1


# Game history
while True:
    rounds_played = input(" ")
    if rounds_played == "":
        break






