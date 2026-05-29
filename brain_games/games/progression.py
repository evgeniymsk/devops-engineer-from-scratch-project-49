import secrets

GAME_RULES = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 100
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, step, length):
    return [start + index * step for index in range(length)]


def get_question_and_correct_answer():
    length = secrets.randbelow(MAX_LENGTH - MIN_LENGTH + 1) + MIN_LENGTH
    start = secrets.randbelow(MAX_START - MIN_START + 1) + MIN_START
    step = secrets.randbelow(MAX_STEP - MIN_STEP + 1) + MIN_STEP
    hidden_index = secrets.randbelow(length)

    progression = generate_progression(start, step, length)
    correct_answer = str(progression[hidden_index])

    question_parts = []
    for index in range(length):
        if index == hidden_index:
            question_parts.append('..')
        else:
            question_parts.append(str(progression[index]))

    question = ' '.join(question_parts)
    return question, correct_answer
