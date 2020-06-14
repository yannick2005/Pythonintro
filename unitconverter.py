print("Welcome, this file turns kilometers into miles")
while True:
    user_input = input("Enter number of kilometers: ")
    km = int(user_input)


    print("Converted into miles: " +str(int(km * 0.62137)))
    more = str(input("Do you want to convert another number of kilometer, Yes or No? "))
    if more == str("No"):
        print("goodbye")
        break
    else:
        print("Lets Continue")
