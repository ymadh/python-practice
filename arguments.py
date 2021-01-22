def multiple(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiple(2, 3, 4, 5))

# when you pass an arbitrary number of arguments,
# py treats it like atuple
