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


def get_question():
    length = secrets.randbelow(MAX_LENGTH - MIN_LENGTH + 1) + MIN_LENGTH
    start = secrets.randbelow(MAX_START - MIN_START + 1) + MIN_START
    step = secrets.randbelow(MAX_STEP - MIN_STEP + 1) + MIN_STEP
    hidden_index = secrets.randbelow(length)

    progression = generate_progression(start, step, length)

    question_parts = []
    for index in range(length):
        if index == hidden_index:
            question_parts.append('..')
        else:
            question_parts.append(str(progression[index]))

    return ' '.join(question_parts)


def get_correct_answer(question):
    parts = question.split()
    hidden_index = parts.index('..')

    numbers = []
    for index, part in enumerate(parts):
        if part != '..':
            numbers.append((index, int(part)))

    first_index, first_value = numbers[0]
    second_index, second_value = numbers[1]
    step = (second_value - first_value) // (second_index - first_index)
    start = first_value - first_index * step

    return str(start + hidden_index * step)
