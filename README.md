# PRODIGY_CS_03
PASSWORD strength CHECKER

## Overview

The **Password Strength Checker** is a Python script that evaluates the strength of user passwords. It checks if the password meets certain security standards, such as length, the presence of uppercase letters, lowercase letters, digits, and special characters, providing feedback on the password's strength.

## Features

- **Strength Assessment**:
  - Checks if the password is at least 8 characters long.
  - Verifies the inclusion of uppercase and lowercase letters, numbers, and special characters.
- **Strength Feedback**:
  - **Weak Password**: If the password lacks essential criteria or is too short.
  - **Moderate Password**: When the password meets some but not all security requirements.
  - **Strong Password**: Meets all password security criteria.
- **User-Friendly Repetition**: After each password check, users can decide to check another password or exit the program.

## Requirements

- Python 3.x (built-in libraries are used)

## Usage

1. **Clone or download** the project.
2. Open a terminal and navigate to the project directory.
3. Run the script with the following command:
   ```bash
   python password_checker.py
   ```
4. Follow the prompts:
   - Enter a password to check its strength.
   - Decide whether to check another password by entering "yes" or "no."

## Code Explanation

### Function: `check_password_strength(password)`

The function `check_password_strength()` evaluates if the password meets the following security criteria:
  - Minimum length of 8 characters.
  - Presence of at least one uppercase letter, lowercase letter, digit, and special character.

Each criterion met increases the overall password strength score.

### Main Loop and User Interaction

The script runs in a loop, allowing users to check multiple passwords until they choose to exit by entering "no" when prompted.

### Example Usage

```
LET'S CHECK THAT PASSWORD SHALL WE...
ENTER A PASSWORD TO CHECK ITS STRENGTH: Password123!
password strength: strong password
DO YOU WANT TO CHECK PASSWORD AGAIN? ENTER YES/NO: yes
```

### Sample Output for Different Passwords

- **Weak Password**: "weak password - password must be at least 8 characters long"
- **Moderate Password**: "moderate password"
- **Strong Password**: "strong password"

## License

This project is open-source and available under the MIT License.
