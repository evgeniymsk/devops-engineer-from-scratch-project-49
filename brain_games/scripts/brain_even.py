import prompt

from brain_games.games import even

ROUNDS_COUNT = 3


def run_game(name):
    print(even.GAME_RULES)
    for _ in range(ROUNDS_COUNT):
        question = even.get_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = even.get_correct_answer(question)
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    run_game(name)


if __name__ == '__main__':
    main()
