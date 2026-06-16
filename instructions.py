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
*** 𝓘𝓝𝓢𝓣𝓡𝓤𝓒𝓣𝓘𝓞𝓝𝓢 ***

Get the questions correct!   
    """)

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want instructions? ")

 # Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print ("Program continues")










