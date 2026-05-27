import prompt

ROUNDS_COUNT = 3


def play(game, game_rules, name):
    print(game_rules)
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
