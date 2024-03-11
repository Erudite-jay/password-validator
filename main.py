def getDetails():
    username=input("Enter user name ")

    print("Enter password")
    print("Note: Password should contains \n length greater than 12 and less than 20 characters")
    print("Three Uppercase letter")
    print("Three lowercase letter")
    print("One number")
    print("Three special character")
    print("Only letters, numbers, and !@#$%^&*()_-~ are allowed")
    print("Start a 2 digit number or special character")
    print("Should not contain 5 same characters or numbers consecutively")
    print("Should not contain user name")
    print("Should not 3 same special characters consecutively")

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

def checkPasswordStart(password):
 if (password[0].isdigit() and password[1].isdigit()) or password[0] in "!@#$%^&*()_-~":
    return True
 return False

def checkConsecutiveCharNum(password):
    count=1
    for i in range(len(password)-1):
        if password[i]==password[i+1]:
            count=count+1
        elif password[i]!=password[i+1]:
            count=1
    if count>4:
        return False
    return True

def checkPasswordContainUsername(username,password):
    if username in password:
        return False
    return True

def checkConsecutiveSpecial(password):
    count=1
    for i in range(len(password)-1):
     if password[i] in "!@#$%^&*()_-~" and password[i+1] in "!@#$%^&*()_-~":
        if password[i]==password[i+1]:
            count=count+1
     elif password[i]!=password[i+1]:
        count=1

    if count>=3:
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

    if checkPasswordStart(password)==False:
        print("Password should start with a 2 digit number or special character")
        
    if checkConsecutiveCharNum(password)==False:
        print("Password string cannot contain 5 same characters or numbers consecutively")

    if checkPasswordContainUsername(username, password)==False:
        print("Password should not contain username")
    
    if checkConsecutiveSpecial(password)==False:
        print("Password should not contain atleast three special character consecutively")
    
if __name__ == "__main__":
    main()
