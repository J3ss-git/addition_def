# Function that uses the user's input to convert minutes in seconds
def convert(min):
    sec = min * 60
    return print(f"The total number of seconds in {str(min)} minutes is {str(sec)} seconds.")

menu = True
while True:
    # Making sure user quits while loop
    choice = input("Do you want to continue? Y/N  ").upper()

    if choice == "Y":
    # Asking user's input on numbers
        min = int(input("What is the total minutes you want to convert?"))
        
        # Function in action
        convert(min)

    elif choice == "N":
        quit()
        print("Thank you for your corparation!")

    else:
        print("Wrong value entered, please try again...")