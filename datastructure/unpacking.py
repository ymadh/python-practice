numbers = [1, 2, 3]
print(numbers)
# want to print 1,2,3
# unpack = spread ....
print(*numbers)

values = [*range(5)]
print(*values)

first = [1,2]
second = [3]
values = [*first, *second]
print(values)

first = { "x": 1 }
second = {"x": 2, "y": 3}
combined = {**first, **second}
print(combined)
