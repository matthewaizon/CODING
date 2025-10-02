while True:
    print('Who are you?')
    name = input('> ')

    if name != 'mat':
        print('Access denied!')
        continue
    
    print('Hello, mat. What is the password? (It is a fish.)')

    password = input('> ')
    if password == 'swordfish':
        break
    else:
        print('Wrong password!')

print('Access granted.')