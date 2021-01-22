items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# items with price >= 10
print(list(filter(lambda item: item[1] >= 10, items)))

# comprehension
# [expression for item in items]
# these are the same code.
prices = list(map(lambda item: item[1], items))
print(prices)
print([item[1] for item in items])


print(list(filter(lambda item: item[1] >= 10, items)))
print([item for item in items if item[1] >= 10])
