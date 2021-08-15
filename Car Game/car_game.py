command = ""
started = False
while True:
    command = input('>').lower()
    if command == "start":
        if started:

            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped!")
    elif command == "help":
        print("start = to start the car \nstop = to stop the car\nquit = to exit")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
