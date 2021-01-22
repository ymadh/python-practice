numbers = [3, 51, 2, 8, 6]
# numbers.sort()

# numbers.sort(reverse=True)

newSorted = sorted(numbers, reverse=True)
print(numbers)
print(newSorted)

# list of tuples
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
