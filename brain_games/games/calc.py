import random

GAME_RULES = 'What is the result of the expression?'
MIN_OPERAND = 1
MAX_OPERAND = 100
OPERATIONS = ('+', '-', '*')


def get_question():
    operand1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operation = random.choice(OPERATIONS)
    match operation:
        case '+':
            return f'{operand1} + {operand2}'
        case '-':
            return f'{max(operand1, operand2)} - {min(operand1, operand2)}'
        case '*':
            return f'{operand1} * {operand2}'


def get_correct_answer(question):
    operand1, operation, operand2 = question.split()
    operand1 = int(operand1)
    operand2 = int(operand2)
    match operation:
        case '+':
            return str(operand1 + operand2)
        case '-':
            return str(operand1 - operand2)
        case '*':
            return str(operand1 * operand2)
