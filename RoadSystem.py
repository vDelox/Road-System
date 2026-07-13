Speed = int(input("what is your speed : "))

command = input("Whats the current road code (A1, A2, A3) : ")

if command == "A1" or command == "a1":
    if Speed <= 40:
        print("Thanks for following the rules.")
    elif Speed > 40:
        print ("Please follow the rules.")

if command == "A2" or command == "a2":
    if Speed <= 100:
        print("Thanks for following the rules.")
    elif Speed > 100:
        print ("Please follow the rules.")

if command == "A3" or command == "a3":
    if Speed <= 150:
        print("Thanks for following the rules.")
    elif Speed > 150:
        print ("Please follow the rules.")
