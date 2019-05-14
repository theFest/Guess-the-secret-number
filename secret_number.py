secret = 33
user_i = int(input("Enter a lucky number(1-99) :"))
if secret == user_i:
    print("Congratulations, money is yours!")
elif user_i < 1:
    print("Unrecognized number")
elif user_i > 99:
    print("Unrecognized number")
else:
    print("Wrong")
