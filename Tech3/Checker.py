def has_minimum_length(password):
    return len(password) >= 8
def has_lowercase(password):
    return any(char.islower() for char in password)
def has_uppercase(password):
    return any(char.isupper() for char in password)
def has_digit(password):
    return any(char.isdigit() for char in password)
def has_special_character(password):
    special_characters = "!@#$%^&*()-=_+[]{}|;:'\",.<>/?"
    return any(char in special_characters for char in password)
def has_no_spaces(password):
    return ' ' not in password


password = input("Enter your password: ")


if (has_minimum_length(password) and
    has_lowercase(password) and
    has_uppercase(password) and
    has_digit(password) and
    has_special_character(password) and
    has_no_spaces(password)):
    print("Password is strong!")
else:
    print("Password is weak. Please follow the password requirements.")
