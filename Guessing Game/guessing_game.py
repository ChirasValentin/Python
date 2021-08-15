secret_number = 9
lives = 3
attempts = 0

while attempts != lives:
    input_number = int(input("Guess: "))
    attempts += 1
    if input_number == secret_number:
        print("Congrats!")
        break
else:
    print("You lose!")
