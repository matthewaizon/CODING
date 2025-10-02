import sys

name = ''

while name != 'your name':
    print('Please type your name.')
    name = input('>')

    if name == 'x':
        break

print('Thank you!')