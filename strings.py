# course = "python programming"
# print(len(course))
# # strings are immutable
# print(course[0])  # creates new memory and copies chars into that new memory
# print(course[-1])
# print(course[0:3])
# print(course[:3])
# print(course[0:])
# print(course[:])


first = "amy"
last = "wightman"
# full = first + " " + last

# formatted string
full = f"{first} {last}"
print(full)


course = "   Python Programming"
print(course.strip())
# case sensitive
print(course.find("pro"))

# replace

print("Programming" in course)
print("Programming" not in course)
