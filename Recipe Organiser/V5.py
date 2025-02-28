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
            self.head = new_recipe
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_recipe

    def display_recipes(self):
        if not self.head:
            print("No recipes available.")
            return
        
        current = self.head
        while current:
            self._print_recipe(current)
            current = current.next

    def _print_recipe(self, recipe):
        print("-----------------------------------------------------------")
        print(f"Recipe Name: {recipe.name}")
        print(f"Category: {recipe.category}")
        print(f"Cooking Time: {recipe.time} minutes")
        print(f"Ingredients: {', '.join(recipe.ingredients)}")
        print(f"Instructions: {recipe.instructions}")
        print("-----------------------------------------------------------")

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

    def insertion_sort(self, key):
        if not self.head or not self.head.next:
            return  # No sorting needed for an empty or single-node list

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current, key)
            current = next_node

        self.head = sorted_list  # Update head to the sorted list

    def _sorted_insert(self, sorted_list, new_node, key):
        new_node_value = getattr(new_node, key)
        sorted_list_value = getattr(sorted_list, key) if sorted_list else None

        # Convert strings to lowercase for case-insensitive sorting
        if isinstance(new_node_value, str):
            new_node_value = new_node_value.lower()
        if isinstance(sorted_list_value, str):
            sorted_list_value = sorted_list_value.lower()

        # Insert at the beginning if needed
        if not sorted_list or new_node_value < sorted_list_value:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next:
            next_value = getattr(current.next, key)
            if isinstance(next_value, str):
                next_value = next_value.lower()

            if next_value >= new_node_value:
                break
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_list

    def linear_search(self, key, value):
        if not self.head:
            print("No recipes available to search.")
            return
        
        current = self.head
        found = False

        while current:
            attr_value = getattr(current, key, None)  # Check if key exists in RecipeNode
            if attr_value is not None and str(attr_value).lower() == value.lower():
                self._print_recipe(current)
                found = True
            current = current.next
        
        if not found:
            print(f"No recipe found with {key}: {value}")


# Example Usage:
recipe_list = RecipeLinkedList()
recipe_list.add_recipe("Pancakes", ["Flour", "Milk", "Eggs", "Sugar"], 15, "Mix and cook on skillet.", "Breakfast")
recipe_list.add_recipe("Pasta", ["Pasta", "Tomato Sauce", "Cheese"], 20, "Boil pasta, add sauce, serve.", "Dinner")
recipe_list.add_recipe("Omelette", ["Eggs", "Milk", "Salt", "Pepper"], 10, "Whisk and cook in a pan.", "Breakfast")

print("Before Sorting:")
recipe_list.display_recipes()

recipe_list.insertion_sort("time")  # Sort by cooking time
print("\nAfter Sorting by Time:")
recipe_list.display_recipes()

recipe_list.insertion_sort("name")  # Sort by name
print("\nAfter Sorting by Name:")
recipe_list.display_recipes()

# Searching Example:
print("\nSearching for 'Pancakes' by Name:")
recipe_list.linear_search("name", "Pancakes")

print("\nSearching for 'Dinner' by Category:")
recipe_list.linear_search("category", "Dinner")


# Change logs
# V1: Recipe functions added 
# V2: display_recipes() function's output format changed 
#     Added bubble sorting algorithm 
# V3: Replaced Bubble ssort with Insertion sort for higher efficiency
#     Added Linear Search Algorithm (Errors found)
# V4: Corrected Linear Search errors 
# V5: Optimised Code #