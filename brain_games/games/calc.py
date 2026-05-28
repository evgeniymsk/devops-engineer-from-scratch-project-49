import secrets

GAME_RULES = 'What is the result of the expression?'
MIN_OPERAND = 1
MAX_OPERAND = 100
OPERATIONS = ('+', '-', '*')


def generate_round():
    operand1 = secrets.randbelow(MAX_OPERAND - MIN_OPERAND + 1) + MIN_OPERAND
    operand2 = secrets.randbelow(MAX_OPERAND - MIN_OPERAND + 1) + MIN_OPERAND
    operation = OPERATIONS[secrets.randbelow(len(OPERATIONS))]
    match operation:
        case '+':
            question = f'{operand1} + {operand2}'
            correct_answer = str(operand1 + operand2)
        case '-':
            larger_operand = max(operand1, operand2)
            smaller_operand = min(operand1, operand2)
            question = f'{larger_operand} - {smaller_operand}'
            correct_answer = str(larger_operand - smaller_operand)
        case '*':
            question = f'{operand1} * {operand2}'
            correct_answer = str(operand1 * operand2)
    return question, correct_answer


def get_question():
    question, correct_answer = generate_round()
    get_question.round = (question, correct_answer)
    return question


def get_correct_answer(question):
    stored_question, correct_answer = get_question.round
    assert question == stored_question
    return correct_answer
