def password_checker(password):
    error = []
    has_uppercase = has_lowercase = has_digit = has_special = ""
    if len(password)<8:
        error.append('Minimum 8 characters required')
    for char in password:
        if char.isupper():
            has_uppercase = 'Yes'
        elif char.islower():
            has_lowercase = 'Yes'
        elif char.isdigit():
            has_digit = 'Yes'
        elif not char.isalnum():
            has_special = 'Yes'
    if has_uppercase != 'Yes':
        error.append('Missing uppercase letter')
    if has_lowercase != 'Yes':
        error.append('Missinng lowercase letter')
    if has_digit != 'Yes':
        error.append('Missing digit')
    if has_special != 'Yes':
        error.append('Missing special character')
    return error

def main():
    password = input('Enter password:')
    errors = password_checker(password)
    if not errors:
        print('Strong')
    else:
        print('Weak')
        for error in errors:
            print(error)
main()