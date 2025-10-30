# GuardianPass Shield 🛡️

A password strength validation tool with an intuitive graphical user interface that helps users create strong and secure passwords.

## 📖 Description

GuardianPass Shield is a password strength checker that evaluates passwords against industry-standard security criteria. The application provides real-time feedback and strength ratings to help users understand the security level of their passwords.

## ✨ Features

- **Length Validation**: Ensures passwords are at least 8 characters long
- **Character Diversity Check**: 
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*()_+-={}[]|:;<>,.?/)
- **Strength Rating System**: 
  - Weak
  - Good
  - Strong
  - Very Strong
- **User-Friendly GUI**: Built with Tkinter for easy interaction
- **Detailed Feedback**: Provides specific guidance on what's missing

## 🎯 Password Strength Criteria

The strength rating is calculated based on:

| Criteria | Points |
|----------|--------|
| Length > 12 characters | 3 points |
| Length 8-12 characters | 1 point |
| 4+ uppercase letters | 2 points |
| 1-3 uppercase letters | 1 point |
| 4+ lowercase letters | 2 points |
| 1-3 lowercase letters | 1 point |
| 3+ special characters | 2 points |
| 1-2 special characters | 1 point |
| 3+ numbers | 3 points |
| 1-2 numbers | 1 point |

**Rating Scale:**
- 11 points: Very Strong
- 8-10 points: Strong
- 6-7 points: Good
- 5 or less: Weak

## 🚀 How to Use

1. Navigate to the GuardianPass Shield directory:
```bash
cd "GuardianPass Shield"
```

2. Run the main program:
```bash
python "Main Program.py"
```

3. Enter your password in the text field

4. Click "Check Password Strength" to evaluate

5. Review the feedback and strength rating

## 📸 Screenshots

The application displays:
- Welcome message with password criteria
- Input field for password entry
- Check button to validate password
- Results showing password strength and any missing criteria
- Close button to exit the application

## 🔄 Version History

- **v1.1**: Optimized loops for better performance
- **v1.2**: Added consecutive character check
- **v1.3**: Major code overhaul for easier maintenance, removed consecutive character check
- **v1.3.1**: Added 'Planned' section
- **v1.3.2**: Code optimization
- **v1.4**: Major improvements
  - Implemented function-based architecture
  - Added password rating system
  - Added number inclusion criteria
  - Introduced password policies
- **v1.5**: Optimized function calling, removed password policies section
- **v1.6 (Final)**: Included GUI and final code optimization

## 💡 Usage Example

**Weak Password:**
- Input: `password`
- Feedback: "Password should have a combination of uppercase and lowercase letters."

**Good Password:**
- Input: `Password1!`
- Feedback: "Password meets all criteria. Strength: Good"

**Very Strong Password:**
- Input: `MyStr0ng!P@ssw0rd2024`
- Feedback: "Password meets all criteria. Strength: Very Strong"

## 🔧 Technical Details

**Language:** Python 3.x  
**GUI Framework:** Tkinter  
**Dependencies:** None (uses Python standard library)

**Key Functions:**
- `counter()`: Counts occurrences of specific character types
- `check_password()`: Main validation logic
- `strength_check()`: Calculates password strength score
- `strength_rate()`: Converts score to rating label

## 📚 Learning Outcomes

This project demonstrates:
- GUI development with Tkinter
- String manipulation and validation
- Function-based programming
- User input handling
- Conditional logic and scoring systems
- Software versioning and iterative development

## 🤝 Contributing

Suggestions for improvements are welcome! Some ideas for future enhancements:
- Add password generation feature
- Implement entropy calculation
- Check against common password databases
- Add password complexity visualization
- Multi-language support

## 📝 Notes

- The GUI is designed with a clean, professional appearance using Trebuchet MS font
- All validation is performed client-side
- No passwords are stored or transmitted
- The application provides educational feedback to help users understand password security

---

**Version:** 1.6 (Final)  
**Status:** Complete  
**Last Updated:** 2024
