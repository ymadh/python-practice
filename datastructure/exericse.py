# from pprint import pprint
sentence = "This is a common interview question"
foundLetters = {}

for key in sentence:
    if key in foundLetters:
        foundLetters[key] += 1
    else:
        foundLetters[key] = 1

# pprint(foundLetters)

# get max
# sort reverse
# convert to a list

sortedItems = (sorted(foundLetters.items(), key=lambda kv:kv[1], reverse=True))
print(sortedItems[0])

