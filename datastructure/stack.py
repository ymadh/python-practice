b = []
b.append(1)
b.append(2)
b.append(3)

b.pop()
b.pop()
b.pop()
if not b:
    print("disable")

# LIFO
print("redirect", b[-1])
