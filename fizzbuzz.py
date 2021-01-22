# if / 3 == fizz
# if / 5 == buzz
# if / 3 and / 5 fizzbuz


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

print(fizz_buzz(12))
