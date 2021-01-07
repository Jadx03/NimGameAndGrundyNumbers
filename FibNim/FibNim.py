"""
Name: Jainam Dhruva
Class: CS 315
Project: A Fibonacci Nim Game and a program to check the grundy numbers
Date: Dec 1, 2020
"""

# First 20 Fibonacci Numbers
fibNums = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181}


# Helper function for Zeckendorf representation
def smallestFib(n):

    # Edge case
    if (n == 0 or n == 1):
        return n

    F1, F2, F3 = 0, 1, 1
    while (F3 <= n):
        F1 = F2
        F2 = F3
        F3 = F1 + F2

    return F2


# Zeckendorf representation
def lowZrep(n):

    while (n > 0):

        # Fib num < n
        F = smallestFib(n)
        a = F
        # Reduce n
        n = n-F

    # print(a)
    return a


# Function to Check if G(n,r) == 0
def checkG0(n, r):
    Znums = []
    while (n > 0):

        F = smallestFib(n)
        Znums.append(F)
       
        n = n-F

    if (r < Znums[len(Znums)-1]):
        return True
    else:
        return False


# Function to Check if G(n,r) == 1
def checkG1(n, r):
    Znums = []
    while (n > 0):

        F = smallestFib(n)
        Znums.append(F)
       
        n = n-F

    if ( (Znums[len(Znums)-1] == 1) and ( r >=1 and r < Znums[len(Znums)-2]) ):
        return True
    else:
        return False


# Function to Check if G(n,r) == 2
def checkG2(n, r):
    Znums = []
    while (n > 0):

        F = smallestFib(n)
        Znums.append(F)
       
        n = n-F

    if ( (Znums[len(Znums)-1] == 2) and (r >=2 and r <= Znums[len(Znums)-2])):
        return True
    else:
        return False

# Function to Check if G(n,r) == 3
def checkG3(n, r):
    Znums = []
    while (n > 0):

        F = smallestFib(n)
        Znums.append(F)
       
        n = n-F

    if ( (Znums[len(Znums)-1] == 1) and (Znums[len(Znums)-2] == 3)):
        if (len(Znums)==2):
            return True
        elif (r >= 3 and r<Znums[len(Znums)-3]):
            return True
    elif ( (Znums[len(Znums)-1] == 3) and ( r >=3 and (r < Znums[len(Znums)-2]-1) )):
        return True
    else:
        return False

# Position Check
def checkPos(n, r):
    if (checkG0(n,r)):
        print("You are in a losing position")
    elif(not(checkG0(n,r))):
        print("You are in a winning position")


numItems = int(input("Enter the number of items: "))
legalmove = max(numItems - 1, 1)

# Fibonacci Nim
while True:

    # Player's move
    print("")
    print(f'You are allowed to remove {legalmove} items')
    checkPos(numItems, legalmove)
    playerIn = int(input("Enter the number of items you want to remove: "))
    while(playerIn > legalmove or playerIn < 1 or playerIn > numItems):
        playerIn = int(input(f'Please enter a number <={min(legalmove,numItems)} and >=1 : '))

    legalmove = 2 * playerIn

    numItems = numItems - playerIn

    print("The number of items after your move are", numItems)
    if (numItems == 0):
        win = 1
        break
    print("")

    # Computer's move
    if (lowZrep(numItems) > legalmove):
        print("Computer removes 1 item")
        numItems = numItems - 1
        legalmove = 2 * 1
    else:
        print("Computer removes", lowZrep(numItems), "items ")
        legalmove = 2 * lowZrep(numItems)
        numItems = numItems - lowZrep(numItems)

    print("The number of items after computer's move are", numItems)
    if (numItems == 0):
        win = 0
        break

print("")
if (win == 1):
    print("You win!")
elif (win == 0):
    print("Computer wins!")
print("")

# Grundy Numbers:
usr_in = input("Do you want to find a Grundy Value of a position (Y/N):")

while(usr_in == 'Y' or usr_in == 'y'):

    print("A program to check if the Grundy value of a position is in [0,3]: ")
    print("")
    usr_in_N = int(input("Enter the Number of Items left in the heap:"))
    usr_in_R = int(input("Enter the Number of Items the player can remove:"))
    while (usr_in_R >= usr_in_N):
        usr_in_R = int(input(f"Enter a number less than {usr_in_N}: "))  

    print("")
    if (checkG3(usr_in_N,usr_in_R)):
        print("The Grundy Value of this position is 3")
    elif (checkG2(usr_in_N,usr_in_R)):
        print("The Grundy Value of this position is 2")
    elif (checkG1(usr_in_N,usr_in_R)):
        print("The Grundy Value of this position is 1")
    elif (checkG0(usr_in_N,usr_in_R)):
        print("The Grundy Value of this position is 0")
    else:
        print("The Grundy value of the position is not in [0,3]")

    checkPos(usr_in_N,usr_in_R)
    print("")

    usr_in = input("Do you want to find a Grundy Value of a position (Y/N):")

print("Thank you for using the program")