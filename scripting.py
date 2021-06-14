# Strings

string_1 = "this is a string"

print(string_1)

first_word = 'Hello'
second_word = 'There'
print(first_word + ' ' + second_word)
print(first_word * 5)
print(len(first_word))   #integer

## index into strings
print(first_word[3])

## strings methods

### string method: format()
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))


maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))


animals = {"dog", "cat", "rabbit"}
actions = {"bite", "chew", "jump"}
for animal, action in zip(animals, actions):
   print("Does your {} {}". format(animal, action))


### string method: split() -- 2 arguments: sep, maxsplit

new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print('Verse has a length of {} character'.format(len(verse)))

print('The first occurrence of the word "and" occurs at the {}th index'.format(verse.find('and')))

print('The last occurrence of the word "you" occurs at the {}th index'.format(verse.rfind('you')))

print('The word "you" occurs {} times in the verse'.format(verse.count('you')

                                                           ))