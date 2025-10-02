import sys

while True:
    print('x for exit')
    response = input('> ')
    
    if response == 'x':
        sys.exit()

    print('You typed ' + response)
