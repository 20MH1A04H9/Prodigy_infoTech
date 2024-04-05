password = input("Enter your password: ")

if len(password) < 8:
    print("Password is weak. Please follow the password requirements.")
else:
    lowercase_flag = False
    uppercase_flag = False
    digit_flag = False
    special_character_flag = False
    space_flag = False
    
    special_characters = "!@#$%^&*()-=_+[]{}|;:'\",.<>/?"
    
    for char in password:
        if char.islower():
            lowercase_flag = True
        elif char.isupper():
            uppercase_flag = True
        elif char.isdigit():
            digit_flag = True
        elif char in special_characters:
            special_character_flag = True
        elif char == ' ':
            space_flag = True

    if lowercase_flag and uppercase_flag and digit_flag and special_character_flag and not space_flag:
        print("Password is strong!")
    else:
        print("Password is weak. Please follow the password requirements.")
