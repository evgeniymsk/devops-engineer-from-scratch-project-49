import secrets

GAME_RULES = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)
MIN_NUMBER = 1
MAX_NUMBER = 100
EVEN_DIVISOR = 2


def get_question_and_correct_answer():
    number = secrets.randbelow(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER
    question = str(number)
    correct_answer = 'yes' if number % EVEN_DIVISOR == 0 else 'no'
    return question, correct_answer
