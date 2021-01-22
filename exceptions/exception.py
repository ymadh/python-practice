
try:
    file = open("inputs.py")
    age = int(input("Age:"))
except (ValueError, ZeroDivisionError) as error:
    print(error)
else:
    print("no exceptions")
finally:
    # always executed
    # for closing connections
    file.close()

print("Execution continues")
