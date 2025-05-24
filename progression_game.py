"""Brain Game: Arithmetic Progression (Geometric variant)."""

import random


def generate_geometric_progression():
    """Generate a geometric progression with a hidden element.

    Returns:
        tuple: (question_str, correct_answer_str)
    """
    # Генерируем случайные параметры прогрессии
    start = random.randint(1, 5)
    step = random.randint(2, 5)
    length = random.randint(5, 10)

    progression = [start * (step ** i) for i in range(length)]

    # Выбираем случайный элемент для замены
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    # Создаем строку с пропуском
    progression_str = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_str.append("..")
        else:
            progression_str.append(str(num))

    question = " ".join(progression_str)

    return question, str(correct_answer)


def play_progression_game():
    """Play the geometric progression brain game."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_geometric_progression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()