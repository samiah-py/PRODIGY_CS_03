import string


print("LET'S CHECK THAT PASSWORD, SHALL WE...")


def check_password():
    password =input("ENTER PASSWORD: ")
    strength = 0
    remark = ""
    
    # Criteria counters
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    is_long_enough = len(password) >= 8
    
    # Check if password is in a list of common passwords
    try:
        with open("password.txt", "r") as f:
            common_passwords = f.read().splitlines()
        if password in common_passwords:
            print("The password was identified in a list of commonly used passwords. Try a more unique one.")
            return
    except FileNotFoundError:
        print("File 'password.txt' not found. Skipping common password check.")
    
    # Check length
    if is_long_enough:
        strength += 1
    else:
        print("Password is too short. Minimum length is 8 characters.")
        return
    
    # Check for character types
    for char in password:
        if char in string.ascii_uppercase:
            has_upper = True
        elif char in string.ascii_lowercase:
            has_lower = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_special = True
    
    # Increment strength for each character type present
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    # Strength remarks based on score
    if strength == 1:
        remark = "Very Weak! - Easily guessable."
    elif strength == 2:
        remark = "Weak! - Too short; add more characters."
    elif strength == 3:
        remark = "Moderate! - Somewhat secure, but could be improved with special characters or numbers."
    elif strength == 4:
        remark = "Good! - Decent strength; consider adding more length or complexity."
    elif strength == 5:  # Maximum strength score with all conditions met
        remark = "Strong! - Your password is well-balanced and secure."

    # Print results
    print(f"Password strength: {strength}/5")
    print(f"Hint: {remark}")


# Check if password is in a list of common passwords
    with open("password.txt", "r") as f:
        common_passwords = f.read().splitlines()
        
        for common_password in enumerate(common_password):

            if password.lower() ==  common_passwords:
                print("The password was identified in a list of commonly used passwords. Try a more unique one.")
                return