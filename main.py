from commonPassword import passwordList as pl

def getUsername():
    username = input("Enter user name ")
    return username


def getPassword():

    print("Note: Password should contains :")
    print("Length greater than 12 and less than 20 characters")
    print("Three Uppercase letter")
    print("Three lowercase letter")
    print("One number")
    print("Three special character")
    print("Only letters, numbers, and !@#$%^&*()_-~ are allowed")
    print("Start a 2 digit number or special character")
    print("Should not contain 5 same characters or numbers consecutively")
    print("Should not contain user name")
    print("Should not 3 same special characters consecutively")

    password = input("Enter password: ")

    return password


def checkPasswordLength(password):
    if len(password) < 12 or len(password) > 20:
        return False
    return True


def checkAtleastThreeUpperCase(password):
    countUpperCase = 0
    for char in password:
        if char.isupper():
            countUpperCase = countUpperCase + 1
        if countUpperCase >= 3:
            return True
    return False


def checkAtleastThreeLowerCase(password):
    countLowerCase = 0
    for char in password:
        if char.islower():
            countLowerCase = countLowerCase + 1
        if countLowerCase >= 3:
            return True
    return False


def checkAtleastOneNumber(password):
    if any(char.isdigit() for char in password):
        return True
    return False


def checkThreeSpecialCharacter(password):
    countSpecialCharacters = 0
    for char in password:
        if char in "!@#$%^&*()_-~":
            countSpecialCharacters = countSpecialCharacters + 1
    if countSpecialCharacters >= 3:
        return True
    return False


def allowedCharacters(password):
    for char in password:
        if (
            char
            not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-~"
        ):
            return False
    return True


def checkPasswordStart(password):
    if (password[0].isdigit() and password[1].isdigit()) or password[
        0
    ] in "!@#$%^&*()_-~":
        return True
    return False


def checkConsecutiveCharNum(password):
    count = 1
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            count = count + 1
            if count >= 5:
                return False
        elif password[i] != password[i + 1]:
            count = 1
    return True


def checkPasswordContainUsername(username, password):
    if username in password:
        return False
    return True


def checkConsecutiveSpecial(password):
    count = 1
    for i in range(len(password) - 1):
        if password[i] in "!@#$%^&*()_-~" and password[i + 1] in "!@#$%^&*()_-~":
            if password[i] == password[i + 1]:
                count = count + 1
                if count >= 3:
                    return False
        elif password[i] != password[i + 1]:
            count = 1
    return True


def checkCommonPassword(password):
    for i in pl:
        if password == i:
            return False
    return True


def validator(username, password, count):

    if count == 3:
        return askUser(username, count)
    elif count == 6:
        return askUser(username, count)

    if checkPasswordLength(password) == False:
        password = input(
            "Password length Should be more than 12 and less than 20 characters : ")
        return validator(username, password, count+1)

    elif checkAtleastThreeUpperCase(password) == False:
        password = input(
            "Password should contain atleast Three upper case letter : ")
        return validator(username, password, count+1)

    elif checkAtleastThreeLowerCase(password) == False:
        password = input(
            "Password should contain atleast Three lower case letter : ")
        return validator(username, password, count+1)

    elif checkAtleastOneNumber(password) == False:
        password = input("Password should contain atleast one number : ")
        return validator(username, password, count+1)

    elif checkThreeSpecialCharacter(password) == False:
        password = input(
            "Password should contain atleast three special character : ")
        return validator(username, password, count+1)

    elif allowedCharacters(password) == False:
        password = input(
            "Only letters, numbers, and !@#$%^&*()_-~ are allowed : ")
        return validator(username, password, count+1)

    elif checkPasswordStart(password) == False:
        password = input(
            "Password should start with a 2 digit number or special character : ")
        return validator(username, password, count+1)

    elif checkConsecutiveCharNum(password) == False:
        password = input(
            "Password string cannot contain 5 same characters or numbers consecutively : "
        )
        return validator(username, password, count+1)

    elif checkPasswordContainUsername(username, password) == False:
        password = input("Password should not contain username : ")
        return validator(username, password, count+1)

    elif checkConsecutiveSpecial(password) == False:
        password = input(
            "Password should not contain three special character consecutively : "
        )
        return validator(username, password, count+1)

    elif checkCommonPassword(password) == False:
        password = input(
            "Password should not contain common password : ")
        return validator(username, password, count+1)

    else:
        return print("Password is valid")

#this function is to ask user that he wants continue creating or not
def askUser(username, count):
    if count == 3:
        respond = input(
            "Do you want to Continue Again? Y For Yes Otherwise Enter any Other Key : ")
        
        if (respond.upper() == "Y"):
            password = getPassword()
            return validator(username, password, count+1)
        else:
            return print("Thank you for using our service")

    elif count == 6:
        print("You have Reached Maximum try !! Please Retry")
        return main()


def main():
    username = getUsername()
    password = getPassword()
    validator(username, password, 0)


if __name__ == "__main__":
    main()
