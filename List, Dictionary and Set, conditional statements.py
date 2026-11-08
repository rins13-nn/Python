# List Creation

age_list = [24, 25, 26, 27, 28]
name_list = ["Ravi", "Priya", "Karthik", "Anu", "Meena"]

print("Original age list:", age_list)
print("Original name list:", name_list)

# List Operations

# a. Append "Yazhini"
name_list.append("Yazhini")
print("\nAfter appending Yazhini:", name_list)

# b. Insert 30 at index 2
age_list.insert(2, 30)
print("After inserting 30:", age_list)

# c. Remove "Yazhini"
name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)

# d. Pop last element
removed_age = age_list.pop()
print("After pop:", age_list)
print("Popped element:", removed_age)

# e. Extend age_list
age_list.extend([29, 30, 26])
print("After extend:", age_list)

# f. Sort in descending order
age_list.sort(reverse=True)
print("After sorting (descending):", age_list)

# g. Max, Min and Sum
print("\nMaximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))

# Accessing Elements

print("\nFirst element:", name_list[0])
print("Last element:", name_list[-1])
print("Elements from index 2 to 4:", name_list[2:5])
print("Reverse order:", name_list[::-1])
