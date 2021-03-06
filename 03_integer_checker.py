# Checks if user has entered an integer that is more than zero


def num_check(question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than zero "
        "(or equal to) {}".format(low)
        print()

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
        
# Main Routine goes here
keep_going = ""
while keep_going == "":
    print()
    var_integer = num_check("Enter Integer: ", 0)
    print()
    # asks to enter a number more than or equal to 1
    image_width = num_check("Enter Image Width: ", 1)
    print()
    image_height = num_check("Enter Image Height: ", 1)
    print()
    