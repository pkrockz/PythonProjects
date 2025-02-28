class RecipeNode:
    def __init__(self, name, ingredients, time, instructions, category):
        self.name = name
        self.ingredients = ingredients  # List of ingredients
        self.time = time  # Cooking time in minutes
        self.instructions = instructions  # Step-by-step instructions
        self.category = category  # Type of recipe (e.g., Dessert, Main Course)
        self.next = None  # Pointer to the next recipe

class RecipeLinkedList:
    def __init__(self):
        self.head = None  # Start of the linked list

    def add_recipe(self, name, ingredients, time, instructions, category):
        new_recipe = RecipeNode(name, ingredients, time, instructions, category)
        if not self.head:
            self.head = new_recipe  # First recipe in the list
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_recipe  # Add to the end of the list

    def display_recipes(self):
        if not self.head:
            print("No recipes available.")
            return
        
        current = self.head
        while current:
            print(f"\nRecipe Name: {current.name}")
            print(f"Category: {current.category}")
            print(f"Cooking Time: {current.time} minutes")
            print(f"Ingredients: {', '.join(current.ingredients)}")
            print(f"Instructions: {current.instructions}")
            print("-" * 40)
            current = current.next

    def delete_recipe(self, name):
        if not self.head:
            print("No recipes to delete.")
            return
        
        if self.head.name == name:
            self.head = self.head.next
            print(f"Recipe '{name}' deleted.")
            return
        
        current = self.head
        while current.next and current.next.name != name:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            print(f"Recipe '{name}' deleted.")
        else:
            print(f"Recipe '{name}' not found.")

# Example Usage:
recipe_list = RecipeLinkedList()
recipe_list.add_recipe("Pancakes", ["Flour", "Milk", "Eggs", "Sugar"], 15, "Mix and cook on skillet.", "Breakfast")
recipe_list.add_recipe("Pasta", ["Pasta", "Tomato Sauce", "Cheese"], 20, "Boil pasta, add sauce, serve.", "Dinner")
recipe_list.display_recipes()
recipe_list.delete_recipe("Pasta")
recipe_list.display_recipes()


# Change logs
# V1: Recipe functions added #