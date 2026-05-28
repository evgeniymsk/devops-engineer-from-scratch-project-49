import prompt

ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    play(game, name)


def play(game, name):
    print(game.GAME_RULES)
    for _ in range(ROUNDS_COUNT):
        question = game.get_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = game.get_correct_answer(question)
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
