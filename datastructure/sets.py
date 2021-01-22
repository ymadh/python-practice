# collection with no duplicates
# unordered, so we cant do first[0]
# indexes - use a list
numbers = [1, 1, 2, 3, 4]
first = set(numbers)

second = {1, 5}

# union
print(first | second)

# intersection
print(first & second)
# not intersection
print(first - second)
# symmetric distance unique from each
print(first ^ second)

if 1 in first:
    print("yes")
# secondset.add(5)
# secondset.remove(1)
# print(secondset)
# print(len(secondset))
