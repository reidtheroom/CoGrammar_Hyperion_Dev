favourite_number = int(input("What's your favourite number? "))

if favourite_number > 100:
    print("Why's it so high?")
elif favourite_number > 25:
    print("Cool.")
# logical error - any number over 75 is over 25, but the 25 code will run instead of 75
elif favourite_number > 75:
    print("Woah, good number. Never would've thought of that.")
elif favourite_number < 5:
    print("Why's it so low? Do you feel like you're this age at heart?")
elif favourite_number % 2 != 0:
    print("I don't know what to say about this number other than it's odd.")
elif favourite_number == 7:
    print("You are simply correct. This is the best number.")
else:
    print("Okay. What do I do with this?")
