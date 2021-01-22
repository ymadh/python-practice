items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# returns a map function
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# returns a list
prices = list(map(lambda item: item[1], items))
print(prices)
