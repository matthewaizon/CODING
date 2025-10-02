import random, sys

random_number = random.randint(1, 7)

def eightball(x):
    if x == 1:
        return 'Yes - definitely.'
    elif x == 2:
        return 'It is decidedly so.'
    elif x == 3:
        return 'Without a doubt.'
    elif x == 4:
        return 'Reply hazy, try again.'
    elif x == 5:
        return 'Ask again later.'
    elif x == 6:
        return 'Better not tell you now.'
    
eightball(random_number)
print(eightball(random_number) + ' (Random number was ' + str(random_number) + ')')
    
