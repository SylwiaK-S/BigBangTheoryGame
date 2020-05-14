import random

CHOICES = {'rock': 1, 'paper': 2, 'scissors': 3, 'spock': 4, 'lizard': 5}
RULES = {
        'rock': ['scissors', 'lizard'],   # rock crushes scissors & lizard
        'paper': ['rock', 'spock'],       # paper covers rock & disproves Spock
        'scissors': ['paper', 'lizard'],  # scissors cuts paper & decapitates lizard
        'lizard': ['paper', 'spock'],     # lizard eats paper & poisons Spock
        'spock': ['rock', 'scissors']     # Spock vaporizes rock & smashes scissors
        }


def rules():
    print('The rules:\nScissors cuts paper, '
          'paper covers rock, rock crushes lizard, lizard poisons Spock,'
          'Spock smashes scissors,\nscissors decapitates lizard, lizard eats paper, '
          'paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.\n'
          '[https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock] ')


def welcome_msg():
    print('Welcome Big Bang Theory fan! Let\'s play a game of \'Rock, Paper, Scissors, Lizard, Spock.\' ')


class Player:


    def __init__(self, name, initial_score=0):
        self.name = name
        self.score = initial_score

    def make_a_move(self, choice):
        move = {key for key, value in CHOICES.items() if value == choice}
        print('Player {} choice: {}'.format(self.name,', '.join(map(str, move))))
        return ', '.join(map(str, move)) #move

    def add_score(self):
        self.score += 1


class User(Player):
    def __init__(self, name, initial_score=0):
        self.name = name
        Player.score = initial_score
        print('Player {} created!'.format(self.name))

    def make_a_choice(self):
        print('Available choices: 1:rock, 2:paper, 3:scissors, 4:spock, 5:lizard')
        choice = int(input('What\'s your move? Please enter a number corresponding to your choice.\n'))
        if choice not in range(1,6):
            print('Invalid number. Please try again')
        return choice

    def greetings(self):
        print('Hello {}! Let\'s play! Shall we?'.format(self.name))


class ComputerPlayer(Player):

    def __init__(self, name='Computer', initial_score=0):
        self.name = name
        Player.score = initial_score

    def make_a_choice(self):
        choice = random.randint(1,5)
        return choice


def assign_score(player1_choice, player2_choice):
    for key, value in RULES.items():
        if player1_choice == key and player2_choice in value:
            player1.add_score()
            print('You won! Congrats!')
        elif player1_choice == key and player2_choice == key:
            print('It\'s a draw. Keep trying!')
        elif player2_choice == key and player1_choice in value:
            player2.add_score()
            print('You loose! Sorry!')
    for player in players:
        print('Player {} has {} points'.format(player.name, player.score))


def player_name():
    name = input('What\'s your name?\n')
    return name


welcome_msg()
rules()
player1 = User(player_name())
player2 = ComputerPlayer()
players = (player1, player2) #[User(player_name()),ComputerPlayer()] #(player1, player2)
player1.greetings()

play = True
while play:
    player1_choice = player1.make_a_move(player1.make_a_choice())
    player2_choice = player2.make_a_move(player2.make_a_choice())
    assign_score(player1_choice, player2_choice)
    replay = input('Are you ready for replay? Yes or No\n').lower()
    if replay == 'yes' or replay == 'y':
        play = True
    elif replay == 'no' or replay == 'n':
        play = False
        print('Results:')
        [print('Player {} score: {}'.format(player.name, player.score)) for player in players]
        print('Goodbye!')
    else:
        print('Invalid input.Please try again')



