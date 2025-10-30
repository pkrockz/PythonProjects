# Quick Start Guide 🚀

Get started with Python Projects in minutes!

## Prerequisites Check

Before running any project, ensure you have Python installed:

```bash
python --version
```

or

```bash
python3 --version
```

You should see Python 3.6 or higher.

## Running GuardianPass Shield

**Step 1:** Open your terminal/command prompt

**Step 2:** Navigate to the project directory:
```bash
cd "GuardianPass Shield"
```

**Step 3:** Run the program:
```bash
python "Main Program.py"
```

or

```bash
python3 "Main Program.py"
```

**Step 4:** A GUI window will open. Enter a password and click "Check Password Strength"

### Example Passwords to Try:

| Password | Expected Result |
|----------|----------------|
| `password` | Weak - missing uppercase, numbers, special chars |
| `Password1` | Good - missing special character |
| `P@ssw0rd` | Good - meets basic criteria |
| `MySecure!P@ss123` | Strong/Very Strong - excellent password |

## Running Recipe Organiser

**Step 1:** Open your terminal/command prompt

**Step 2:** Navigate to the project directory:
```bash
cd "Recipe Organiser"
```

**Step 3:** Run the program:
```bash
python V7.py
```

or

```bash
python3 V7.py
```

**Step 4:** A GUI window will open with buttons for different operations

### Try These Steps:

1. **Add a Recipe:**
   - Click "Add Recipe"
   - Fill in: Name: "Pasta", Ingredients: "pasta, tomato sauce, cheese", Time: "20", Instructions: "Boil pasta, add sauce", Category: "Main Course"
   - Click "Save Recipe"

2. **Display Recipes:**
   - Click "Display Recipes"
   - View your recipe in a new window

3. **Search Recipe:**
   - Click "Search Recipe"
   - Select "Category" and enter "Main Course"
   - Click "Search"

4. **Sort Recipes:**
   - Add a few more recipes first
   - Click "Sort Recipes"
   - Choose "name" or "time"
   - Click "Sort"

5. **Delete Recipe:**
   - Click "Delete Recipe"
   - Enter the recipe name
   - Click "Delete"

## Troubleshooting

### "No module named 'tkinter'"

**Windows:**
- Tkinter usually comes with Python. Try reinstalling Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "tcl/tk and IDLE" during installation

**macOS:**
```bash
brew install python-tk
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora):**
```bash
sudo dnf install python3-tkinter
```

### "python: command not found"

Try using `python3` instead of `python`:
```bash
python3 "Main Program.py"
```

### GUI Doesn't Appear

1. Ensure you're running the command from the correct directory
2. Check that you're using Python 3.6 or higher
3. Verify tkinter is installed (see above)
4. Try closing and reopening your terminal

### Permission Denied

**macOS/Linux:**
```bash
chmod +x "Main Program.py"
```

Then run again.

## Next Steps

- Read the full [README.md](README.md) for detailed information
- Check individual project READMEs for specific features
- Review [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute
- Explore the version history in each project folder to see how they evolved

## Need Help?

- Check the main README.md for detailed documentation
- Review project-specific READMEs in each folder
- Look at the code comments for implementation details
- Open an issue on GitHub if you find bugs

## Tips

- **For Students:** Study the code progression from V1 to final versions to see how the projects evolved
- **For Developers:** The projects demonstrate clean coding practices and iterative development
- **For Learners:** Start with the simpler versions (V1) and progress to understand each improvement

---

Happy coding! 🎉
