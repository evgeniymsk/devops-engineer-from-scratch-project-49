import math
import secrets

GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_correct_answer():
    number1 = secrets.randbelow(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER
    number2 = secrets.randbelow(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER
    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
