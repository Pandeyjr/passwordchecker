import re
import math

# List of common passwords
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", 
    "abc123", "password1", "123123", "admin", "letmein", "welcome"
]

# Function to estimate password cracking time
def calculate_crack_time(password):
    # Character set size based on password composition
    char_set_size = 0
    if re.search(r'[a-z]', password):
        char_set_size += 26  # Lowercase letters
    if re.search(r'[A-Z]', password):
        char_set_size += 26  # Uppercase letters
    if re.search(r'[0-9]', password):
        char_set_size += 10  # Numbers
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        char_set_size += 32  # Special characters

    # Total number of possible combinations
    total_combinations = char_set_size ** len(password)

    # Assuming 1 billion guesses per second (modern GPU capabilities)
    guesses_per_second = 1_000_000_000
    seconds_to_crack = total_combinations / guesses_per_second

    # Convert seconds to human-readable time
    if seconds_to_crack < 60:
        return f"{seconds_to_crack:.2f} seconds"
    elif seconds_to_crack < 3600:
        return f"{seconds_to_crack / 60:.2f} minutes"
    elif seconds_to_crack < 86400:
        return f"{seconds_to_crack / 3600:.2f} hours"
    elif seconds_to_crack < 31536000:
        return f"{seconds_to_crack / 86400:.2f} days"
    else:
        return f"{seconds_to_crack / 31536000:.2f} years"

# Function to check if the password is common
def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Rule 1: Length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Rule 2: Uppercase and Lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    # Rule 3: Digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Rule 4: Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Rule 5: Check for common passwords
    if is_common_password(password):
        feedback.append("This is a very common password. Avoid using it.")
        strength = max(0, strength - 2)  # Heavily penalize common passwords

    # Determine password strength
    if strength >= 5:
        status = "Strong"
    elif strength >= 3:
        status = "Moderate"
    else:
        status = "Weak"

    return status, feedback

# Main interactive function
if __name__ == "__main__":
    print("Welcome to the Interactive Password Strength Checker!")
    password = input("Enter a password to check its strength: ")

    # Check password strength
    status, feedback = check_password_strength(password)
    crack_time = calculate_crack_time(password)
    common_password = is_common_password(password)

    # Display results
    print("\n--- Password Analysis ---")
    print(f"Password Strength: {status}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Your password is strong. Great job!")

    # Display password cracking time
    print(f"Estimated Time to Crack: {crack_time}")

    # Common password check
    if common_password:
        print("Warning: Your password is among the most common passwords. Avoid using it!")

    print("\nThank you for using the Password Strength Checker!")
