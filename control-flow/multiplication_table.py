number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    # i will take values 1, 2, 3 … 10
    product = number * i
# using f string
print(f"{number} * {i} = {product}")


# multiplication_table.py

# Step 1: Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Loop from 1 to 10
for i in range(1, 11):
    # Step 3: Multiply
    product = number * i
    
    # Step 4: Print in format
    print(f"{number} * {i} = {product}")
