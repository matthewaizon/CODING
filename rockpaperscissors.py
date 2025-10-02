import random, sys

wins = 0
losses = 0
ties = 0

while True:
    print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (x) to exit')
    player_input = input('> ')

    if player_input == 'x':
        sys.exit()
    elif player_input not in ['r', 'p', 's']:
        print('Invalid input, please try again.')
        continue
    elif player_input == 'r':
        print('Rock versus...')
    elif player_input == 'p':
        print('Paper versus...')
    elif player_input == 's':
        print('Scissors versus...')

    bot_input = random.randint(1, 4)
    if bot_input == 1:
        bot_input = 'r'
        print('Rock')
    elif bot_input == 2:
        bot_input = 'p'
        print('Paper')
    elif bot_input == 3:
        bot_input = 's'
        print('Scissors')

    if player_input == bot_input:
        print('It\'s a tie!')
        ties += 1
    elif (player_input == 'r' and bot_input == 's') or (player_input == 'p' and bot_input == 'r') or (player_input == 's' and bot_input == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1