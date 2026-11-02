string1 = "Hello "
name = input("Enter your Name: ")

# Concatenate string1 and name
greeting = string1 + name
print(greeting)

# Concatenate another string
string3 = ", welcome to Python programming"
greeting = greeting + string3

print(greeting)

# =====================================
# 2. STRING SLICING AND INDEXING
# =====================================

print("\nString Slicing and Indexing")

# a. First character
print("a. First character:", greeting[0])

# b. Last character
print("b. Last character:", greeting[-1])

# c. First 5 characters
print("c. First 5 characters:", greeting[:5])

# d. Last 11 characters
print("d. Last 11 characters:", greeting[-11:])

# e. Reverse the string
print("e. Reversed string:", greeting[::-1])

# f. Extract the word 'Python'
start = greeting.find("Python")
end = start + len("Python")
print("f. Extracted word:", greeting[start:end])

# =====================================
# 3. STRING METHODS
# =====================================

strM = "Python beginner tutorial"

print("\nString Methods")

# a. Uppercase
print("a. Uppercase:", strM.upper())

# b. Lowercase
print("b. Lowercase:", strM.lower())

# c. Capitalize
print("c. Capitalize:", strM.capitalize())

# d. Count occurrences of 't'
print("d. Count of 't':", strM.count('t'))

# e. Replace Python with Machine Learning
print("e. Replaced String:",
      strM.replace("Python", "Machine Learning"))

# =====================================
# 4. TUPLES
# =====================================

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate tuples
t_combine = tuple1 + tuple2
print("\na. Concatenated Tuple:", t_combine)

# b. Repeat tuple 3 times
print("b. Tuple repeated 3 times:", t_combine * 3)

# c. Access 3rd element
print("c. 3rd element:", t_combine[2])

# d. First three elements
print("d. First three elements:", t_combine[:3])

# e. Last three elements
print("e. Last three elements:", t_combine[-3:])
