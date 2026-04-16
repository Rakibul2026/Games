import random
import sys

roll = int(input("Enter how much time you wanna role: "))

for i in range(0,roll):
    while True:
        start = input("ready? (y/n): ")
        if(start == "y"):
            x = random.randint(1,6)
            y = random.randint(1,6)
            result = (x,y)
            print(f"your result: ({result[0]},{result[1]})")
            print()
            break

        elif(start == "n"):
           print("You yourself finished the game.")
           sys.exit(0)

        else:
            print("You just entered a wrong keyword...")
            continue

print(f"Your {roll} roll just finished. Thanks you for choosing us...")
        