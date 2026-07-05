# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Tuple:", fruits)

# Accessing elements
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Length of tuple
print("Length:", len(fruits))

# Loop through tuple
print("\nAll Fruits:")
for fruit in fruits:
    print(fruit)

# Check if an item exists
if "Mango" in fruits:
    print("\nMango is present in the tuple.")