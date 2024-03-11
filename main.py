def getDetails():
    username=input("Enter user name ")
    password=input("Enter password ")

    print("Note:\nPassword length should be greater than 12 and less than 20 characters")
    print("Uppercase letter")
    print("One lowercase letter")
    print("One number")
    print("One special character")
    
          
    return username,password

def checkPasswordLength(password):
    if len(password)<12 and len(password)<20:
        return False
    return True

def checkAtleastOneUpperCase(password):
    if any(char.isupper() for char in password):
        return True
    return False

def checkAtleastOneLowerCase(password):
    if any(char.islower() for char in password):
        return True
    return False

def checkAtleastOneNumber(password):
    if any(char.isdigit() for char in password):
        return True
    return False

def main():
    username,password=getDetails()
    if checkPasswordLength(password)==False:
        print("Password length Should be less than 12 tand more than 20 characters")
    
    if checkAtleastOneUpperCase(password)==False:
        print("Password should contain atleast one upper case letter")

    if checkAtleastOneLowerCase(password)==False:
        print("Password should contain atleast one lower case letter")

    if checkAtleastOneNumber(password)==False:
        print("Password should contain atleast one number")

if __name__ == "__main__":
    main()

