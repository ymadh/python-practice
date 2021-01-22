from sys import getsizeof

values = (x * 2 for x in range(100000))
# generator object - size stays the same no matter how big
print("gen:", getsizeof(values))
# for x in values:
#     print(x)

# large ds - memory inefficient
# range(1B)
