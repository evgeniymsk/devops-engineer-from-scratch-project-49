import math
import secrets

GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question():
    number1 = secrets.randbelow(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER
    number2 = secrets.randbelow(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER
    return f'{number1} {number2}'


def get_correct_answer(question):
    number1, number2 = question.split()
    return str(math.gcd(int(number1), int(number2)))
