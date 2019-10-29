counter = 0
while counter < 11:
    number = input("\n Hello! Please enter a number other than 5 : ")

    if int(number) == 5:
        print("Hey! You weren't supposed to enter " +
              str(counter) + "!")
        break
    elif counter == 10:
        print("Wow, you're more patient than I am, you win.")
    counter += 1
