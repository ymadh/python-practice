letters = ["a", "b", "c"]

# gives you a tuple (read only list)
for letter in enumerate(letters):
    # print(letter)
    # print(letter[0], letter[1])
    key, val = letter
    print(key, val)


for index, letter in enumerate(letters):
    print(index, letter)

