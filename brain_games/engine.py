import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def play(game):
    name = welcome_user()
    print(game.GAME_RULES)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
