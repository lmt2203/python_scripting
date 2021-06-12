def greet(name):
    print("Nice to meet you, {}!".format(name.title()))

greet("Linh")

how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)

name = input('Enter a name: ')
print('Hello',name.title())

# function `eval` evaluates a string as a line
# result = eval(input("Enter an expression: "))
# print(result)

names =  input('Enter a name: ')
assignments =  input('Enter number of missing assignment: ')
grades =  input('Enter a grade: ')

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade))