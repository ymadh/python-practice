# phonebook - name -> contact
# key value pairs
point = {"x": 1, "y": 2}
# same but cleaner
point = dict(x=1, y=2)
print(point)
print(point["x"])
point["x"] = 3
print(point)
point["z"] = 4

if "a" in point:
    print(point["a"])
# default value
print(point.get("a"), 0)
del point["x"]

# loop over dict
# holds key
for key in point:
    print(key, point[key])

# alternative - returns tuple
for key, value in point.items()
    print(key, value)
    