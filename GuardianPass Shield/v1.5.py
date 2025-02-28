def counter(password, char_list):
    count = 0
    for char in password:
        if char in char_list:
            count += 1
    return count

def check_password(password):
    special_char_list = '!@#$%^&*()_+-={}[]|:;<>,.?/'
    num_list = '123456789'
    lower_list = 'qwertyuioplkjhgfdsazxcvbnm'
    upper_list = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    
    total_lower = counter(password, lower_list)
    total_upper = counter(password, upper_list)
    total_special_char = counter(password, special_char_list)
    total_number = counter(password, num_list)
    
    length = len(password)
    
    if length >= 8:
        if total_lower > 0 and total_upper > 0 and total_special_char > 0 and total_number > 0:
            strength = strength_check(length, total_upper, total_lower, total_special_char, total_number)
            check_strength = strength_rate(strength)
            return "The password meets all criteria. \n" + check_strength
        elif total_lower == 0 or total_upper == 0:
            return "Password should have a combination of uppercase and lowercase letters."
        elif total_number == 0:
            return "Password should have at least 1 number."
        else:
            return "Password should have at least 1 special character."
    else:
        return "Password needs to be at least 8 characters long."

def strength_check(length, total_upper, total_lower, total_special_char, total_number):
    strength = 0
    strength += 3 if length > 12 else 1
    strength += 2 if total_upper >= 4 else 1
    strength += 2 if total_lower >= 4 else 1
    strength += 2 if total_special_char >= 3 else 1
    strength += 3 if total_number >= 3 else 1
    return strength

def strength_rate(strength):
    if strength >= 12:
        return "Rating: Very strong"
    elif 8 <= strength < 12:
        return "Rating: Strong"
    elif 5 <= strength < 8:
        return "Rating: Good"
    else:
        return "Rating: Weak"

password = input("Enter password:")
checker = check_password(password)
print(checker)
