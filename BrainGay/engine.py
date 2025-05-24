# engine.py
def run_game(game_module, rounds=3):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    print("Find the answer to the following questions.\n")
    correct_count = 0

    for _ in range(rounds):
        question, correct_answer = game_module.get_question()
        print(f"Question: {question}")
        user_input = input("Your answer: ").strip()

        # Для сравнения — целое число
        try:
            user_answer = int(user_input)
        except ValueError:
            print(f"'{user_input}' is not a valid number.")
            print(f"Let's try again, {name}!\n")
            return

        if user_answer == correct_answer:
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"\nLet's try again, {name}!\n")
            return

    print(f"Congratulations, {name}!")