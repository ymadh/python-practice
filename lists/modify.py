letters = ["a", "b", "c"]

# append
letters.append("d")

# insert
letters.insert(0, "-")
print(letters)

letters.pop()
print(letters)

# remove at index
letters.pop(2)
print(letters)

letters.remove("b")

del letters[0]
del letters[0:3]

# remove all
letters.clear()
