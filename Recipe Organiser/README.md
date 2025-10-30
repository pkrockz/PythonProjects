# Recipe Organiser 🍳

A comprehensive recipe management system built with Python, featuring a linked list data structure implementation and an intuitive graphical user interface.

## 📖 Description

Recipe Organiser is a desktop application that allows users to manage their recipe collection efficiently. It implements fundamental data structures and algorithms, including linked lists, insertion sort, and linear search, providing both educational value and practical functionality.

## ✨ Features

- **Add Recipes**: Store recipes with detailed information
  - Recipe name
  - Ingredients list
  - Cooking time (in minutes)
  - Step-by-step instructions
  - Category classification
- **Display All Recipes**: View your complete recipe collection
- **Search Recipes**: Find recipes by name or category using linear search
- **Sort Recipes**: Organize recipes by name or cooking time using insertion sort
- **Delete Recipes**: Remove recipes from the collection
- **Persistent Data Structure**: Linked list implementation for efficient memory management
- **User-Friendly GUI**: Built with Tkinter for easy navigation

## 🏗️ Architecture

### Data Structures

**RecipeNode Class:**
- Represents a single recipe in the linked list
- Contains: name, ingredients, time, instructions, category
- Points to the next recipe node

**RecipeLinkedList Class:**
- Manages the entire recipe collection
- Implements core operations: add, search, delete, sort
- Uses linked list for dynamic memory allocation

### Algorithms

1. **Insertion Sort**
   - Time Complexity: O(n²)
   - Used for sorting recipes by name or cooking time
   - Case-insensitive string comparison

2. **Linear Search**
   - Time Complexity: O(n)
   - Used for finding recipes by name or category
   - Returns all matching results

## 🚀 How to Use

1. Navigate to the Recipe Organiser directory:
```bash
cd "Recipe Organiser"
```

2. Run the latest version:
```bash
python V7.py
```

3. Use the main menu buttons:
   - **Add Recipe**: Opens a form to enter new recipe details
   - **Display Recipes**: Shows all stored recipes
   - **Search Recipe**: Find recipes by name or category
   - **Sort Recipes**: Organize recipes alphabetically or by cooking time
   - **Delete Recipe**: Remove a recipe by name
   - **Exit**: Close the application

## 📋 Usage Examples

### Adding a Recipe

1. Click "Add Recipe"
2. Fill in the form:
   - **Recipe Name**: "Chocolate Cake"
   - **Ingredients**: "flour, sugar, cocoa, eggs, butter"
   - **Cooking Time**: "45"
   - **Instructions**: "Mix dry ingredients, add wet ingredients, bake at 350°F"
   - **Category**: "Dessert"
3. Click "Save Recipe"

### Searching for Recipes

1. Click "Search Recipe"
2. Select search type: "Name" or "Category"
3. Enter search value (e.g., "Dessert")
4. Click "Search"
5. View matching recipes in the results window

### Sorting Recipes

1. Click "Sort Recipes"
2. Choose sort criteria: "name" or "time"
3. Click "Sort"
4. View sorted recipes using "Display Recipes"

## 🔄 Version History

- **V1**: Initial implementation with basic recipe functions
- **V2**: 
  - Improved display_recipes() output format
  - Added bubble sort algorithm
- **V3**: 
  - Replaced bubble sort with insertion sort for better efficiency
  - Added linear search algorithm
  - Fixed initial bugs
- **V4**: 
  - Corrected linear search errors
  - Improved search functionality
- **V5**: 
  - Code optimization
  - Improved readability and maintainability
- **V6**: 
  - Implemented GUI with Tkinter
  - Integrated linear search with visual interface
- **V7 (Final)**: 
  - Added recipe deletion feature
  - Implemented insertion sort in GUI
  - Complete CRUD operations with GUI
  - Final optimization and bug fixes

## 🔧 Technical Details

**Language:** Python 3.x  
**GUI Framework:** Tkinter  
**Dependencies:** 
- tkinter (standard library)
- tkinter.ttk (standard library)
- tkinter.messagebox (standard library)

**Key Classes and Methods:**

```python
class RecipeNode:
    def __init__(self, name, ingredients, time, instructions, category)
    
class RecipeLinkedList:
    def add_recipe(name, ingredients, time, instructions, category)
    def search_recipe(key, value)
    def delete_recipe(name)
    def insertion_sort(key)
    def _sorted_insert(sorted_list, new_node, key)
    
class RecipeGUI:
    def add_recipe_window()
    def display_recipes()
    def search_recipe_window()
    def sort_recipes_window()
    def delete_recipe_window()
```

## 📚 Learning Outcomes

This project demonstrates:
- **Data Structures**: Implementation of linked lists from scratch
- **Algorithms**: Insertion sort and linear search
- **GUI Programming**: Multi-window Tkinter applications
- **Object-Oriented Programming**: Classes and methods
- **Input Validation**: Error handling and user feedback
- **Software Development**: Iterative improvement through versions
- **CRUD Operations**: Create, Read, Update, Delete functionality

## 💡 Best Practices

- **Case-Insensitive Operations**: All searches and sorts handle case variations
- **Input Validation**: All fields are validated before processing
- **User Feedback**: Informative messages for all operations
- **Error Handling**: Graceful handling of invalid inputs
- **Clean UI**: Organized layout with clear button labels

## 🎯 Use Cases

- **Home Cooks**: Organize personal recipe collection
- **Students**: Learn data structures and algorithms
- **Meal Planning**: Search recipes by category
- **Quick Reference**: Find recipes by cooking time
- **Recipe Management**: Keep track of favorite recipes

## 🔮 Future Enhancement Ideas

- Export recipes to PDF or text file
- Import recipes from files
- Add recipe ratings and reviews
- Include nutritional information
- Add recipe images
- Implement recipe sharing features
- Add serving size calculations
- Create shopping list from ingredients
- Implement more advanced search (partial matches)
- Add recipe tags for better categorization

## 🤝 Contributing

Suggestions and improvements are welcome! Areas for contribution:
- Enhanced search algorithms (binary search for sorted lists)
- Database integration for persistent storage
- Recipe scaling feature (adjust serving sizes)
- Unit conversions for ingredients
- Recipe import/export functionality

## 📝 Notes

- Recipes are stored in memory only (not persisted to disk)
- Ingredients are stored as a list and displayed comma-separated
- Cooking time must be entered as an integer (minutes)
- Recipe names are used as unique identifiers for deletion
- The linked list grows dynamically as recipes are added
- Sorting creates a new sorted linked list structure

## 🧪 Testing the Application

To test all features:

1. **Add 3-4 recipes** with different categories and cooking times
2. **Display all recipes** to verify they were added
3. **Search by category** (e.g., "Dessert")
4. **Search by name** to find a specific recipe
5. **Sort by name** and display to see alphabetical order
6. **Sort by time** and display to see time-based order
7. **Delete a recipe** and verify it's removed
8. **Try invalid inputs** to test error handling

---

**Version:** V7 (Final)  
**Status:** Complete  
**Last Updated:** 2024

**Data Structure Complexity:**
- Add: O(n) - traverse to end of list
- Search: O(n) - linear search through list
- Delete: O(n) - search and remove node
- Sort: O(n²) - insertion sort algorithm
- Display: O(n) - traverse entire list
