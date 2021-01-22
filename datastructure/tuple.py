# tuple is read only list
point = (1, 2)
# point = 1, 2 works as well
# point = 1, 
# point = () 
point = (1, 2) + (3, 4)
print(point)
point = (1, 2) * 3
print(point)
point = tuple([1, 2])
point = tuple("Hello World")
print(point[0:2])
# unpack
x, y = point
print(x)

# can't do point[0] = 10; 
# cant add or remove an object
# tuples are used for a seq of objects that doesnt change
