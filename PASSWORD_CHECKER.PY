import re

def check_password_strength(password):
    length = len(password) >= 8
    if not length:
        return "weak password - password must be at least 8 characters long"
    upper_case = re.search(r"[A-Z]", password) is not None
    lower_case = re.search(r"[a-z]", password) is not None
    digits = re.search(r"\d", password) is not None
    special_char = re.search(r"[!#$%&'()*+,-@./:;<=>?^|]", password) is not None
  
    all_character = sum([length, upper_case, lower_case, digits, special_char])

    if all_character == 5:
        return "strong password"
    elif 3 <= all_character < 5:
        return "moderate password"
    else:
        return "weak password"

print("LET'S CHECK THAT PASSWORD SHALL WE...")

while True:
    password = input("ENTER A PASSWORD TO CHECK ITS STRENGTH: ")   
    Strength = check_password_strength(password)    
    print(f"password strength: {Strength}")

    user_response = input("DO YOU WANT TO CHECK PASSWORD AGAIN? ENTER YES/NO: ").strip().lower()
    if user_response != "yes":
        print("THANK YOU FOR USING THE PASSWORD CHECKER.")
        break
