
students_count: int = 1000
print(type(students_count))

if students_count == 1000:
    print('yes')
else:
    print('no')



guess = 0
answer = 5
while answer != guess:
    guess = int(input("Guess: " ))
