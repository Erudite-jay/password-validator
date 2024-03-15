# Password Validator

This Python script is designed to validate user passwords based on specific criteria to ensure they are strong and secure. It prompts users to input a username and a password, then applies a series of checks to verify if the password meets the required standards.

## Features

- **Password Length:** Ensures the password length is between 12 and 20 characters.
- **Case Sensitivity:** Requires at least three uppercase and three lowercase letters.
- **Numeric Requirement:** Mandates the presence of at least one number.
- **Special Characters:** Enforces the inclusion of at least three special characters.
- **Character Restrictions:** Allows only specific characters: letters, numbers, and a defined set of special characters.
- **Start Restrictions:** Requires the password to start with either a 2-digit number or a special character.
- **Consecutive Character Check:** Prevents the occurrence of five consecutive identical characters or numbers.
- **Username Check:** Verifies that the password does not contain the username.
- **Consecutive Special Character Check:** Ensures that there are no three consecutive special characters.
- **Common Password Check:** Verifies that the password is not one of the commonly used passwords.

  ### __Phase 2__
- **User Ask:** Prompt to ask user to retry to make new password

  ### __Phase 3__
- **Username Validator:** Validate User Name , cannot contains spaces and cannot be blank
- Print last Wrong Password 

## Functions

1. **getUsername():**
   - Prompts the user to input a username.
   - Returns the username entered by the user.

2. **getPassword():**
   - Provides instructions for creating a password meeting specific criteria.
   - Prompts the user to input a password.
   - Returns the password entered by the user.

3. **checkPasswordLength(password):**
   - Checks if the password length is within the specified range.
   - Returns True if the length is valid, False otherwise.

4. **checkAtleastThreeUpperCase(password):**
   - Counts the number of uppercase letters in the password.
   - Returns True if there are at least three uppercase letters, False otherwise.

5. **checkAtleastThreeLowerCase(password):**
   - Counts the number of lowercase letters in the password.
   - Returns True if there are at least three lowercase letters, False otherwise.

6. **checkAtleastOneNumber(password):**
   - Checks if the password contains at least one number.
   - Returns True if a number is found, False otherwise.

7. **checkThreeSpecialCharacter(password):**
   - Counts the number of special characters in the password.
   - Returns True if there are at least three special characters, False otherwise.

8. **allowedCharacters(password):**
   - Checks if the password contains only allowed characters.
   - Returns True if all characters are allowed, False otherwise.

9. **checkPasswordStart(password):**
   - Checks if the password starts with a 2-digit number or a special character.
   - Returns True if the password meets the criteria, False otherwise.

10. **checkConsecutiveCharNum(password):**
    - Checks if the password contains five consecutive identical characters or numbers.
    - Returns True if the password does not contain consecutive characters, False otherwise.

11. **checkPasswordContainUsername(username, password):**
    - Checks if the password contains the username.
    - Returns True if the password does not contain the username, False otherwise.

12. **checkConsecutiveSpecial(password):**
    - Checks if the password contains three consecutive special characters.
    - Returns True if the password meets the criteria, False otherwise.

13. **checkCommonPassword(password):**
    - Checks if the password is one of the commonly used passwords.
    - Returns True if the password is not common, False otherwise.

14. **passwordValidator(username, password):**
    - Validates the password based on all the above functions.
    - Provides feedback to the user if the password is not valid.

15. **main():**
    - Entry point of the script.
    - Calls getUsername(), getPassword(), and validator() functions.

 ### Phase 2 Functions
16. **askUser():**
    - Prompt user that he wants continue creating or not.
    - Calls validator() functions in respond of Yes and Calls main() in case of Retry.

 ### Phase 2 Functions
16. **usernameValidator():**
    - validate Username .
    - Calls getUsername() functions in fail validation of username.

## How to Use

1. Run the script.
2. Enter the desired username when prompted.
3. Follow the instructions to input a password.
4. The script will validate the password based on the defined criteria.
5. It validate the username and proceed to ask password 
6. If the password is valid, a confirmation message will be displayed. Otherwise, the user will be prompted to enter a new password that meets the requirements.
7. Ask User whether he wants to continue making password in 3 times wrong password input and ask to retry in 6 times wrong passsword input

## Requirements

- Python 3.x
