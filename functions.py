def increment(number: int, by: int=1) -> tuple:
    # returns a tuple which is  a read only list
    return (number, number + by)


print(increment(2, 3))

# tuple - read only
# (1,2,3)
# list
# [1,2,3]
