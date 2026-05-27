import prompt

from brain_games.engine import play
from brain_games.games import calc


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    play(calc, calc.GAME_RULES, name)


if __name__ == '__main__':
    main()
