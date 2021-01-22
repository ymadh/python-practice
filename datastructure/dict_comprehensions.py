# values = []
# for x in range(5):
#     values.append(x * 2)

# print(values)
# same as ...
values = [x * 2 for x in range(5)]
# sets - have values, dic - key value pair
values = {x * 2 for x in range(5)}
values = {x: x * 2 for x in range(5)}
print(values)

