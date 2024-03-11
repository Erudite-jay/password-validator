def getDetails():
    username=input("Enter user name ")

    print("Enter password")
    print("Note:\nPassword length should be greater than 12 and less than 20 characters")
    print("Three Uppercase letter")
    print("Three lowercase letter")
    print("One number")
    print("Three special character")

    password=input()
       
    return username,password

def checkPasswordLength(password):
    if len(password)<12 and len(password)<20:
        return False
    return True

def checkAtleastThreeUpperCase(password):
    countUpperCase=0
    for char in password:
        if char.isupper():
            countUpperCase=countUpperCase+1
        if countUpperCase>=3:
            return True 
        return False

def checkAtleastThreeLowerCase(password):
    countLowerCase=0
    for char in password:
        if char.islower():
            countLowerCase=countLowerCase+1
        if countLowerCase>=3:
            return True 
        return False

def checkAtleastOneNumber(password):
    if any(char.isdigit() for char in password):
        return True
    return False

def checkThreeSpecialCharacter(password):
    countSpecialCharacters=0
    for char in password:
        if char in "!@#$%^&*()_-~":
            countSpecialCharacters=countSpecialCharacters+1
    if countSpecialCharacters>=3:
        return True
    return False

def allowedCharacters(password):
    for char in password:
        if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-~":
            return False
        return True

def main():
    username,password=getDetails()
    if checkPasswordLength(password)==False:
        print("Password length Should be less than 12 tand more than 20 characters")
    
    if checkAtleastThreeUpperCase(password)==False:
        print("Password should contain atleast Three upper case letter")

    if checkAtleastThreeLowerCase(password)==False:
        print("Password should contain atleast Three lower case letter")

    if checkAtleastOneNumber(password)==False:
        print("Password should contain atleast one number")

    if checkThreeSpecialCharacter(password)==False:
        print("Password should contain atleast three special character")

    if allowedCharacters(password)==False:
        print("Only letters, numbers, and !@#$%^&*()_-~ are allowed")
        
if __name__ == "__main__":
    main()

