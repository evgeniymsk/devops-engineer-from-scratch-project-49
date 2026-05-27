import secrets

GAME_RULES = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_PRIME = 2
FIRST_DIVISOR = 2


def is_prime(number):
    if number < MIN_PRIME:
        return False
    divisor = FIRST_DIVISOR
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def get_question():
    number = secrets.randbelow(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER
    return str(number)


def get_correct_answer(question):
    number = int(question)
    return 'yes' if is_prime(number) else 'no'
