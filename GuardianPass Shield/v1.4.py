def counter(password, char_list):
    count = 0
    for char in password:
        if char in char_list:
            count += 1
    return count

def check_password(password):
    special_char_list = '!@#$%^&*()_+-={}[]|:;<>,.?/'
    num_list = '123456789'
    lower_list = 'abcdefghijklmnopqrstuvwxyz'
    upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    total_lower = counter(password, lower_list)
    total_upper = counter(password, upper_list)
    total_special_char = counter(password, special_char_list)
    total_number = counter(password, num_list)
    
    length = len(password)
    strength = 0
    
    if length >= 8:
        if total_lower and total_upper and total_special_char and total_number:
            return "The password meets all criteria."
        elif total_lower == 0 or total_upper == 0:
            return "Password should have a combination of uppercase and lowercase letters."
        elif total_number == 0:
            return "Password should have at least 1 number."
        else:
            return "Password should have at least 1 special character."
    else:
        return "Password is too short."

def strength_check(length, total_upper, total_lower, total_special_char, total_number):
    strength = 0
    strength += 3 if length > 12 else 1
    strength += 2 if total_upper > 4 else 1
    strength += 2 if total_lower > 4 else 1
    strength += 2 if total_special_char > 3 else 1
    strength += 3 if total_number > 3 else 1
    return strength

def strength_rate(strength):
    if strength == 12:
        return "Rating: Very strong"
    elif 8 <= strength <= 11:
        return "Rating: Strong"
    elif 5 <= strength <= 7:
        return "Rating: Good"
    else:
        return "Rating: Weak"

length=0
total_lower = 0
total_upper = 0
total_special_char = 0
total_number = 0

password = input("Enter password:")
checker = check_password(password)
print(checker)
strength = strength_check(length, total_upper, total_lower, total_special_char, total_number)
check_strength = strength_rate(strength)
print(check_strength)




