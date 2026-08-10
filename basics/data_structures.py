# 1. List
# A list is ordered, changeable (mutable), and allows duplicate values.
fruits = ["apple", "banana", "mango", "apple"]

print("List:", fruits)
print("First fruit:", fruits[0])

# Add an item
fruits.append("orange")

# 2. Tuple
# A tuple is ordered, but it cannot be changed (immutable).
colors = ("red", "green", "blue")

print("Tuple:", colors)
print("First color:", colors[0])


# 3. Dictionary
# A dictionary stores data as key-value pairs.
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)
print("Student name:", student["name"])

# Add a new key-value pair
student["city"] = "Aurangabad"

# 4. Set
# A set is unordered and stores only unique values.
numbers = {1, 2, 3, 4, 4, 5}

print("Set:", numbers)

# Add an item
numbers.add(6)

print("Updated Set:", numbers)
