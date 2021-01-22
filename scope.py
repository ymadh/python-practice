global_message = "b"
message = "c"


def greet():
    if True:
        # to override the global message
        global message
        message = "a"
    print(message)
    print(global_message)

# dont have blocklevel scope
# we do have fn level scope

# global variables
greet()
print(message)
