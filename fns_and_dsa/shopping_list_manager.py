# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # list implementation

    while True:
        display_menu()  # calling display_menu

        # Choice input as a number (int) with validation
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input: please enter a number (1-4).")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added '{item}' has been added to your list.")
            else:
                print("No item entered. Nothing was added.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"No item found '{item}' has been removed from your list.")
            else:
                print(f"Removed'{item}' was not found in the list.")

        elif choice == 3:
            if shopping_list:
                print("Your shopping list:")
                for idx, it in enumerate(shopping_list, start=1):
                    print(f"{idx}. {it}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
# shopping_list.py

# Array (list) for shopping items
shopping_list = []

# Function to display menu
def display_menu():
    print("=== Shopping List Menu ===")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

def main():
    while True:
        display_menu()  # calling display_menu function

        # Choice input as a number
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            if shopping_list:
                print("Your shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 2:
            item = input("Enter an item to add: ")
            shopping_list.append(item)
            print(f"{item} added to shopping list.")
        elif choice == 3:
            if shopping_list:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                try:
                    remove_index = int(input("Enter number of item to remove: ")) - 1
                    if 0 <= remove_index < len(shopping_list):
                        removed = shopping_list.pop(remove_index)
                        print(f"{removed} removed from shopping list.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
