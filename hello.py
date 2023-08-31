import random


def choose_options():
  options = ('stein', 'papier', 'schere')
  user_option = input('stein, papier oder schere => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Keine gültige Auswahl')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('Spieler Auswahl =>', user_option)
  print('Computer Auswahl =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Unentschieden!')
  elif user_option == 'stein':
    if computer_option == 'schere':
      print('Der Stein gewinnt Schere')
      print('Der Spieler hat gewonnen!')
      user_wins += 1
    else:
      print('Das Papier gewinnt Stein')
      print('Der Computer hat gewonnen!')
      computer_wins += 1
  elif user_option == 'papier':
    if computer_option == 'stein':
      print('Das Papier gewinnt Stein')
      print('Der Spieler hat gewonnen!')
      user_wins += 1
    else:
      print('Die Schere gewinnt Papier')
      print('Der Computer hat gewonnen!')
      computer_wins += 1
  elif user_option == 'schere':
    if computer_option == 'papier':
      print('Die Schere gewinnt Papier')
      print('Der Spieler hat gewonnen!')
      user_wins += 1
    else:
      print('Der Stein gewinnt die Schere')
      print('Der Computer hat gewonnen!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('Der Gewinner ist der Computer')
      break

    if user_wins == 2:
      print('Der Gewinner ist der Spieler')
      break

run_game()
