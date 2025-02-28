import tkinter as tk

def counter(password, char_list):
    count = 0
    for char in password:
        if char in char_list:
            count += 1
    return count

def check_password():
    password = entry_password.get()
    
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
            label_result["text"] = "Password meets all criteria.\nStrength: " + check_strength
        elif total_lower == 0 or total_upper == 0:
            label_result["text"] = "Password should have a combination of uppercase and lowercase letters."
        elif total_number == 0:
            label_result["text"] = "Password should have at least 1 number."
        else:
            label_result["text"] = "Password should have at least 1 special character."
    else:
        label_result["text"] = "Password needs to be at least 8 characters long."

def strength_check(length, total_upper, total_lower, total_special_char, total_number):
    strength = 0
    strength += 3 if length > 12 else 1
    strength += 2 if total_upper >= 4 else 1
    strength += 2 if total_lower >= 4 else 1
    strength += 2 if total_special_char >= 3 else 1
    strength += 3 if total_number >= 3 else 1
    return strength

def strength_rate(strength):
    if strength == 11:
        return "Very strong"
    elif 8 <= strength < 11:
        return "Strong"
    elif 5 < strength < 8:
        return "Good"
    else:
        return "Weak"

root = tk.Tk()
root.title("GuardianPass Shield")
root.geometry("500x450")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

text = """Welcome to GuardianPass Shield!
The aim of the program is to check whether or not you have a strong password.
The password strength criteria are:

Length of the password | Combination of uppercase and lowercase letters
Inclusion of a special character | Inclusion of a number

If all the above criteria are met, a password rating ranging from Weak
to Very Strong will be given based on the intricacy of the given password.
"""
welcome_label = tk.Label(frame, text=text, font=('Trebuchet MS',9))
welcome_label.grid(row=0, column=0)

label_password = tk.Label(frame, text="Enter password", font=('Trebuchet MS',9))
label_password.grid(row=1, pady=10)
entry_password = tk.Entry(frame)
entry_password.grid(row=2)

check_button = tk.Button(frame, text="Check Password Strength", font=('Trebuchet MS',9), command=check_password)
check_button.grid(row=3, pady=10)

close_button = tk.Button(frame, text="Close", font=('Trebuchet MS',9), command=root.destroy)
close_button.grid(row=4)

label_result = tk.Label(frame, font=('Trebuchet MS',11))
label_result.grid(row=5, pady=10)

root.mainloop()
