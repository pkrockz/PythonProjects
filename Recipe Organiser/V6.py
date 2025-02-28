import tkinter as tk
from tkinter import ttk, messagebox

# Recipe Node (Linked List)
class RecipeNode:
    def __init__(self, name, ingredients, time, instructions, category):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions
        self.category = category
        self.next = None

# Recipe Linked List with Linear Search
class RecipeLinkedList:
    def __init__(self):
        self.head = None

    def add_recipe(self, name, ingredients, time, instructions, category):
        """Adds a new recipe to the linked list."""
        new_recipe = RecipeNode(name, ingredients, time, instructions, category)
        if not self.head:
            self.head = new_recipe
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_recipe

    def search_recipe(self, key, value):
        """
        Searches for recipes by the specified key (e.g. 'name' or 'category')
        using a linear search and returns a list of matching nodes.
        """
        results = []
        current = self.head

        while current:
            # Get the attribute (if it doesn't exist, default to an empty string)
            attr_value = getattr(current, key, "").lower()
            if attr_value == value.lower():
                results.append(current)
            current = current.next

        return results

# GUI Class
class RecipeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Organizer")
        self.root.geometry("600x400")

        self.recipe_list = RecipeLinkedList()

        # Title Label
        title_label = tk.Label(root, text="Recipe Organizer", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Button Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        # Buttons for different actions
        tk.Button(btn_frame, text="Add Recipe", width=15, command=self.add_recipe_window).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Display Recipes", width=15, command=self.display_recipes).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Search Recipe", width=15, command=self.search_recipe_window).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Exit", width=15, command=root.quit).grid(row=1, column=1, padx=5, pady=5)

    def add_recipe_window(self):
        """Opens a new window to add a recipe."""
        add_win = tk.Toplevel(self.root)
        add_win.title("Add Recipe")
        add_win.geometry("400x350")

        tk.Label(add_win, text="Recipe Name:").pack(pady=2)
        name_entry = tk.Entry(add_win, width=40)
        name_entry.pack(pady=2)

        tk.Label(add_win, text="Ingredients (comma separated):").pack(pady=2)
        ingredients_entry = tk.Entry(add_win, width=40)
        ingredients_entry.pack(pady=2)

        tk.Label(add_win, text="Cooking Time (minutes):").pack(pady=2)
        time_entry = tk.Entry(add_win, width=40)
        time_entry.pack(pady=2)

        tk.Label(add_win, text="Instructions:").pack(pady=2)
        instructions_entry = tk.Entry(add_win, width=40)
        instructions_entry.pack(pady=2)

        tk.Label(add_win, text="Category:").pack(pady=2)
        category_entry = tk.Entry(add_win, width=40)
        category_entry.pack(pady=2)

        def save_recipe():
            name = name_entry.get().strip()
            ingredients = [i.strip() for i in ingredients_entry.get().split(",")]
            time = time_entry.get().strip()
            instructions = instructions_entry.get().strip()
            category = category_entry.get().strip()

            if not name or not ingredients or not time or not instructions or not category:
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                time = int(time)
                self.recipe_list.add_recipe(name, ingredients, time, instructions, category)
                messagebox.showinfo("Success", f"Recipe '{name}' added successfully!")
                add_win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Cooking time must be a number!")

        tk.Button(add_win, text="Save Recipe", command=save_recipe).pack(pady=10)

    def display_recipes(self):
        """Displays all recipes in a new window."""
        display_win = tk.Toplevel(self.root)
        display_win.title("All Recipes")
        display_win.geometry("500x400")

        if not self.recipe_list.head:
            messagebox.showinfo("No Recipes", "No recipes available.")
            display_win.destroy()
            return

        text_area = tk.Text(display_win, wrap=tk.WORD, width=60, height=20)
        text_area.pack(pady=10)

        current = self.recipe_list.head
        while current:
            text_area.insert(tk.END, f"Recipe Name: {current.name}\n")
            text_area.insert(tk.END, f"Category: {current.category}\n")
            text_area.insert(tk.END, f"Cooking Time: {current.time} minutes\n")
            text_area.insert(tk.END, f"Ingredients: {', '.join(current.ingredients)}\n")
            text_area.insert(tk.END, f"Instructions: {current.instructions}\n")
            text_area.insert(tk.END, "-" * 50 + "\n")
            current = current.next

        text_area.config(state=tk.DISABLED)

    def search_recipe_window(self):
        """Opens a window to search for a recipe."""
        search_win = tk.Toplevel(self.root)
        search_win.title("Search Recipe")
        search_win.geometry("400x200")

        tk.Label(search_win, text="Search by:").pack(pady=5)

        # Let the user choose whether to search by Name or Category
        search_type = ttk.Combobox(search_win, values=["Name", "Category"], state="readonly", width=30)
        search_type.pack(pady=5)
        search_type.current(0)  # Default to "Name"

        tk.Label(search_win, text="Enter value:").pack(pady=5)
        search_entry = tk.Entry(search_win, width=40)
        search_entry.pack(pady=5)

        def perform_search():
            # Use "name" key if searching by Name, otherwise "category"
            key = "name" if search_type.get() == "Name" else "category"
            value = search_entry.get().strip()

            if not value:
                messagebox.showerror("Error", "Please enter a search value.")
                return

            results = self.recipe_list.search_recipe(key, value)

            if not results:
                messagebox.showinfo("Not Found", f"No recipes found for {key}: {value}")
                return

            result_win = tk.Toplevel(search_win)
            result_win.title("Search Results")
            result_win.geometry("500x300")

            text_area = tk.Text(result_win, wrap=tk.WORD, width=60, height=15)
            text_area.pack(pady=10)

            for recipe in results:
                text_area.insert(tk.END, f"Recipe Name: {recipe.name}\n")
                text_area.insert(tk.END, f"Category: {recipe.category}\n")
                text_area.insert(tk.END, f"Cooking Time: {recipe.time} minutes\n")
                text_area.insert(tk.END, f"Ingredients: {', '.join(recipe.ingredients)}\n")
                text_area.insert(tk.END, f"Instructions: {recipe.instructions}\n")
                text_area.insert(tk.END, "-" * 50 + "\n")

            text_area.config(state=tk.DISABLED)

        tk.Button(search_win, text="Search", command=perform_search).pack(pady=10)

# Run GUI
root = tk.Tk()
app = RecipeGUI(root)
root.mainloop()

# Change logs
# V1: Recipe functions added 
# V2: display_recipes() function's output format changed 
#     Added bubble sorting algorithm 
# V3: Replaced Bubble ssort with Insertion sort for higher efficiency
#     Added Linear Search Algorithm (Errors found)
# V4: Corrected Linear Search errors 
# V5: Optimised Code 
# V6: Linear Search with GUI implemented#