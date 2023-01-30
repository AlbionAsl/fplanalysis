import random

def generate_question():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operation = random.choice(["+", "-", "*", "/"])
    question = f"{num1} {operation} {num2} = ?"
    answer = eval(f"{num1} {operation} {num2}")
    return (question, answer)

def play_game(num_questions):
    score = 0
    for i in range(num_questions):
        question, answer = generate_question()
        player_answer = int(input(question))
        if player_answer == answer:
            score += 1
    return score
