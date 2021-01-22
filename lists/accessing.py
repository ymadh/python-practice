# letters = ["a", "b", "c", "d"]
# print(letters[0])
# print(letters[-1])
# print(letters[::3])

numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-1])

# first = numbers[0]
# second = numbers[1]
numbers = list(range(20))

first, second, *other = numbers
first, *other, last = numbers

print(first, last)

