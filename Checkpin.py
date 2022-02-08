
# Program to check a PIN
# Take input from the keyboard until it is identical to a password number which is hardcoded by this program

PIN = 1234

maxtry = 3
attempt = 1

while attempt < maxtry:
    supplied = input("Enter your PIN: ")
    if supplied.isdecimal():
        pinattempt = int(supplied)
        if pinattempt == PIN:
            print("You got it!")
            break
        else:
            print("Incorrect PIN, please try again.  Number of tries remaining: ", maxtry - attempt)
    else:
        print("You must attempt your PIN.  Number of tries remaining: ", maxtry - attempt)
    attempt = attempt + 1
    if attempt == maxtry:
        supplied = input("Enter your PIN: ")
        if supplied.isdecimal():
            pinattempt = int(supplied)
            if pinattempt == PIN:
                print("You got it!")
                break
            else:
                print("Sorry, your PIN is now locked.  Please contact your bank to reset")
        else:
            print("Sorry, your PIN is now locked.  Please contact your bank to reset")
    else:
        pass
