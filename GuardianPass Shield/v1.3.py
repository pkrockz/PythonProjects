print("Welcome to GuardianPass Shield! v1.3")
print("The aim of the program is to check if your password is strong or not.")
print("Note the following criteria that will be checked in this version of the program in order:")
print(end='\n')
print("1. Length of the password.")
print("2. Combination of numbers & uppercase and lowercase letters.")
print("3. Inclusion of a special character.")
print(end='\n')

password = input("Input your password:")
specialCharList = '!@#$%^&*()_+-={}[]|:;<>,.?/'

hasLower = False
hasUpper = False
hasSpecialChar = False

for char in password:
    if char.islower():
        hasLower = True
    elif char.isupper():
        hasUpper = True
    elif char in specialCharList:
        hasSpecialChar = True

if len(password) >= 8 and hasLower and hasUpper and hasSpecialChar:
    print("Strong password")
elif len(password) < 8:
    print("Password is too short.")
elif hasLower==False or hasUpper==False:
    print("Password should have a combination of uppercase and lowercase letters.")
else:
    print("Password should have at least 1 special character.")

print(end='\n')
print("Thank you for using GuardianPass Shield v1.3.")

 

