def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # array/list
    while True:
        display_menu()  # calling display_menu
        choice = int(input("Enter your choice: "))  # ensure number input

        if choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

