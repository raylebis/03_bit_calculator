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

# finds # of bits for 24 bit colour
def image_bits():

    image_height = num_check("Enter Image Height: ", 1)
    print()
    image_width = num_check("Enter Image Width: ", 1)
    
    pixels = image_width * image_height
    bits = pixels * 24

    print()
    print("The # of pixels for your height and width is {}".format(pixels))
    print("The number of bits is {}".format(bits))

    return ""

image_bits()

    


    

