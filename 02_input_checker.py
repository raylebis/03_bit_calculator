# checks user choice is 'integer', 'text', or 'image'


def user_choice():

    valid = False
    while not valid:
        response = input("File type (integer / text / image): ").lower()
        
        # If they chose "t" or "text" or "txt"
        text_ok = ["Text", "t", "txt"]
        if response in text_ok:
            return "text"

        else:
            print("Please choose a valid file type!")
            print()
        # If they chose integer
        int_ok = ["Integer", "Int", "I"]
        if response in int_ok:
            return "integer"

        # If they chose image
        image_ok = ["Image", "Img", "I"]
        if response in image_ok:
            return "Image"

        
# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()
        