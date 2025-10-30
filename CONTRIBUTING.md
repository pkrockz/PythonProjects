# Contributing to Python Projects

Thank you for your interest in contributing to this repository! This document provides guidelines for contributing to the Python Projects collection.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Guidelines](#development-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other contributors

## 💡 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Python version** and operating system
- **Screenshots** if applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear description** of the enhancement
- **Use case** for the feature
- **Possible implementation** approach
- **Examples** of similar features in other projects

### Code Contributions

Areas where contributions are especially welcome:

#### GuardianPass Shield
- Password generation feature
- Entropy calculation
- Common password database checking
- Password strength visualization
- Multi-language support
- Password history tracking

#### Recipe Organiser
- Export/Import functionality (JSON, CSV, PDF)
- Recipe ratings and reviews
- Nutritional information tracking
- Recipe images support
- Shopping list generation
- Serving size calculator
- Unit conversion for ingredients
- Persistent storage (database or file)
- Recipe sharing features

#### General
- Code optimization
- Bug fixes
- Documentation improvements
- Unit tests
- Cross-platform compatibility improvements

## 🚀 Getting Started

1. **Fork the repository** to your GitHub account

2. **Clone your fork** locally:
```bash
git clone https://github.com/YOUR-USERNAME/PythonProjects.git
cd PythonProjects
```

3. **Create a branch** for your changes:
```bash
git checkout -b feature/your-feature-name
```

4. **Make your changes** following the development guidelines below

5. **Test your changes** thoroughly

6. **Commit your changes** with clear commit messages

7. **Push to your fork**:
```bash
git push origin feature/your-feature-name
```

8. **Create a Pull Request** from your fork to the main repository

## 🛠️ Development Guidelines

### Code Style

- Follow **PEP 8** style guide for Python code
- Use **meaningful variable names**
- Keep functions **small and focused**
- Add **comments** for complex logic
- Use **docstrings** for classes and functions

Example:
```python
def calculate_strength(password, criteria):
    """
    Calculate the strength score of a password.
    
    Args:
        password (str): The password to evaluate
        criteria (dict): Dictionary of validation criteria
        
    Returns:
        int: Strength score between 0 and 11
    """
    score = 0
    # Implementation
    return score
```

### Code Organization

- Keep related code together
- Use classes for complex data structures
- Separate GUI code from business logic when possible
- Create helper functions for repeated operations

### Testing

- Test all new features manually
- Verify that existing functionality still works
- Test edge cases and error conditions
- Test on different Python versions if possible (3.6+)

### Documentation

- Update README files when adding features
- Add inline comments for complex algorithms
- Update version history in changelogs
- Include usage examples for new features

## 📝 Commit Guidelines

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat: Add password generation feature to GuardianPass Shield

- Implement random password generator
- Add controls for length and character types
- Update GUI with new button
- Add tests for password generation

Closes #15
```

```
fix: Correct recipe deletion bug in Recipe Organiser

Fixed issue where deleting recipes with similar names
would delete the wrong recipe. Updated search logic
to use exact name matching.

Fixes #23
```

```
docs: Update installation instructions in README

- Add troubleshooting section
- Include Python version requirements
- Add screenshots of applications
```

## 🔄 Pull Request Process

1. **Ensure your code follows** the development guidelines
2. **Update documentation** to reflect your changes
3. **Test thoroughly** before submitting
4. **Fill out the PR template** with all relevant information
5. **Link related issues** in your PR description
6. **Respond to feedback** from reviewers promptly
7. **Keep your PR focused** on a single feature or fix

### PR Title Format

Use the same format as commit messages:
- `feat: Add recipe export feature`
- `fix: Resolve password validation bug`
- `docs: Improve contributing guidelines`

### PR Description Should Include

- **What** changes were made
- **Why** the changes were necessary
- **How** to test the changes
- **Screenshots** for UI changes
- **Related issues** being addressed

### Review Process

- PRs will be reviewed by maintainers
- Feedback will be provided within a reasonable timeframe
- Changes may be requested before merging
- Once approved, PRs will be merged by maintainers

## 🎯 Priorities

Current priorities for contributions:

1. **Bug fixes** - Always welcome
2. **Documentation improvements** - Help others understand the code
3. **Code optimization** - Improve performance
4. **New features** - As discussed in issues
5. **Tests** - Add unit tests for existing functionality

## ❓ Questions?

If you have questions about contributing:

- Check existing issues and pull requests
- Review the README and project documentation
- Open an issue with the `question` label
- Be patient and respectful

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

---

**Note:** This is an educational project. All contributions should maintain the educational value while improving functionality and code quality.
