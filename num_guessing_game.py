import random

com_guess = random.randint(1,100)
attemps = 0

while True:
    try:
        num = int(input("Enter a number from 1 to 100: "))
        attemps += 1
        if(num == com_guess):
            print("You win!")
            print(f"You win in {attemps} times of attemps")
            break

        elif(num > com_guess):
            print("Too high...")
            continue

        elif(num < com_guess):
            print("Too low...")
            continue
    except ValueError:
        print("Please, enter a valid integer value...")
