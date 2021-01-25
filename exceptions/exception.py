
# raise = throw
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be lss than 0")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


# try:
#     # automatically closes this file
#     # ,open("another.txt") as target:
#     with open("../inputs.py") as file:
#         print("file open")
    
#     age = int(input("Age:"))
# except (ValueError, ZeroDivisionError) as error:
#     print(error)
# else:
#     print("no exceptions")
# finally:
#     print("always executed")
#     # always executed
#     # for closing connections
#     # not needed with file.close()

# print("Execution continues")
