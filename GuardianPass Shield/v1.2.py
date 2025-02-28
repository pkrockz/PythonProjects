print("Welcome to GuardianPass Shield! v1.2")
print("The aim of the program is to check if your password is strong or not.")
print("Note the following criteria that will be checked in this version of the program in order:")
print(end='\n')
print("1. Length of the password.")
print("2. Combination of numbers & uppercase and lowercase letters.")
print("3. Inclusion of a special character.")
print("4. Absence of consecutive characters.")
print(end='\n')

Password_input=input("Input your password:")

Uppercase_Checker,Lowercase_Checker,Number_Checker,SpecialChar_Checker,Repeat_Checker=0,0,0,0,0
Lowercase='qwertyuioplkjhgfdsazxcvbnm'
Uppercase='QWERTYUIOPLKJHGFDSAZXCVBNM'
Special_Characters='!@#$%^&*()_+-={}[]|\:;<>,.?/'
Numbers='1234567890'

if len(Password_input)>=8:
    
    for Loop1 in Password_input:
        if Loop1 in Lowercase or Loop1 in Uppercase or Loop1 in Numbers:
            
            for Loop2 in Password_input:
                if Loop2.isupper():
                    Uppercase_Checker=1
                elif Loop2.islower():
                    Lowercase_Checker=1
                elif Loop2.isdigit():
                    Number_Checker=1
                    
            for Loop3 in Password_input:
                if Loop3 in Special_Characters:
                    SpecialChar_Checker=1
                    break
                
            if Uppercase_Checker==1 and Lowercase_Checker==1 and Number_Checker==1 and SpecialChar_Checker==1:

                for Loop4 in range (len(Password_input)-1):
                    if Password_input[Loop4]==Password_input[Loop4+1]:
                        Repeat_Checker=1
                        
                if Repeat_Checker==1:
                    print("Strong password.")
                else:
                    print("Password does not contain either both uppercase and lowercase lettersm a number, a special character or has consecutive characters.")
                    break   
        
else:
    print("Password too short.")
    
print(end='\n')
print("Thank you for using GuardianPass Shield v1.2.")

 

#Changelog
#v1.1 Optimised Loops
#v1.2 Added Consecutive Character Check
