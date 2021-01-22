from array import array
# array takes less memory and performs faster on large datasets (10K +)

numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(2, 4)

