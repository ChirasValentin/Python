command = ""
while True:
    command = input('>').lower()
    if command == "start":
        print("Car started...Ready to go!")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("start = to start the car \nstop = to stop the car\nquit = to exit")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")