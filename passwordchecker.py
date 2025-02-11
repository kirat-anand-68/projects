def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_digit = has_lower = has_upper = has_special = False
    special_chars = '!@#$%^&*()_+'
    
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char in special_chars:
            has_special = True
    
    return has_digit and has_lower and has_upper and has_special

# Test case
print(is_strong_password("Kirat@1313"))  # Output: True
