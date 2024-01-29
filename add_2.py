# Function that uses the user's input to add to values together
def add(num1):
    sum = num1 + 1
    return print(f"Sum of {str(num1)} and 1 is {str(sum)}")

menu = True
while True:
    # Making sure user quits while loop
    choice = input("Do you want to add numbers? Y/N  ").upper()

    if choice == "Y":
    # Asking user's input on numbers
        num1 = int(input("What is the  number you want to add by 1?"))
        
        # Function in action
        add(num1)

    elif choice == "N":
        quit()
        print("Thank you for your corparation!")

    else:
        print("Wrong value entered, please try again...")