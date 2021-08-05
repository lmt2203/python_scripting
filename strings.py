# Replacing function
s = 'pinapple'
s.replace('p', 'b')



# Ask user for a string and prints out the location of each 'a' in the string:
s = input('Enter a string: ')
for i in range(len(s)):
    if s[i] == 'a':
        print(i)


# Asks user for a string and creates a new string that doubles each character of the original string:
s = input('Enter a string: ')
new_string = ''
for char in s:
    new_string = new_string + char*2
print (new_string)

# Write a program that asks a user for their name and prints it in the following funny pattern. E.g: E El Elv Elvi Elvis

s = input('Enter your name: ')
for i in range(len(s)):
    print s[:i+1, end = ' ']

# Write a program that removes all capitalization and common punctuation from a string s
s = input('Enter a string: ')
s = s.lower()
for c in ',.;:-?!()\'"':
    s = s.replace(c, '')

# Write a program that, given a string that contains a decimal number, prints out the decimal part of the number. For instance, given 3.14159 the program should print out.14159
s = input('Enter a decimal number: ')
index = s.find('.')
print (s[index:])

# join: a string method that takes a list of strings and join them together into a single string

