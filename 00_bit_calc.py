# functions go here

# Puts series of symbols at the start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# checks user's choice is an integer, text or an image
def user_choice():
    
    # Lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"] 
    image_ok = ["image", "img", "I", "pix", "picture", "pic", "p"]
   
    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # Checks for valid response and returns text, integer or image

        if response in text_ok:
            return "text"
            
        elif response in integer_ok:
            return "integer"
            
        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image")
            if want_integer == "":
                return "Integer"
            else:
                return "image"
            
        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()

# checks input is a number more than a given value
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

# Heading
statement_generator("look - stars", "*")

# Display instructions if user has not used program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For interges, ask for integer
    if data_type =="integer":
        var_integer = num_check("Enter an integer: ", 0)
    # For images, ask for width and height
    # (must be and inetger more than or equal to 0)
    elif data_type =="image":
        image_height = num_check("Enter Image Height: ", 1)
        print()
        image_width = num_check("Enter Image Width: ", 1)

    # For text, ask for a string
    else:
        var_text = input("Enter some text: ")
