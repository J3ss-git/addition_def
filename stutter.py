def stutter(word):
    two_letters = word[:2]
    return print(f"{two_letters}...{two_letters}...{word}?")

menu = True
while True:
    # Making sure user quits while loop
    choice = input("Do you want to continue? Y/N  ").upper()

    if choice == "Y":
    # Asking user's input on the word that needs to be stuttered
        word = input("What is the word you want to stutter?").lower()
        
        # Function in action
        stutter(word)

    elif choice == "N":
        quit()
        print("Thank you for your corparation!")

    else:
        print("Wrong value entered, please try again...")