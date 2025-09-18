password_file = (open("password.txt", "r"))
sc_pass = password_file.read()
state =  0

while state == 0:
    user_pass = input('Please enter the password to access the system:')

    if user_pass == sc_pass:
        print('Access granted')
        state = 1
    else:
        print('Access denied')