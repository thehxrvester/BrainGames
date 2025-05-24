# games/geometric_progression.py
import random

def get_question():
    length = random.randint(5, 10)
    first_term = random.randint(1, 20)
    ratio = random.randint(2, 5)
    progression = [first_term]
    for _ in range(1, length):
        progression.append(progression[-1] * ratio)

    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]

    display_list = []
    for idx, num in enumerate(progression):
        if idx == hidden_index:
            display_list.append("..")
        else:
            display_list.append(str(num))
    question_str = " ".join(display_list)

    return question_str, correct_answer