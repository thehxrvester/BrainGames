#!/usr/bin/env python3
"""Brain Games: Least Common Multiple (LCM) calculation game."""

import math
import random
from functools import reduce


def welcome_user():
    """Greet the user and get their name."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    return name


def generate_numbers(count=2, min_num=1, max_num=100):
    """Generate random numbers for the game.
    
    Args:
        count: Number of values to generate
        min_num: Minimum value
        max_num: Maximum value
    
    Returns:
        List of random integers
    """
    return [random.randint(min_num, max_num) for _ in range(count)]


def calculate_lcm(numbers):
    """Calculate the least common multiple for numbers.
    
    Args:
        numbers: List of integers
    
    Returns:
        LCM of input numbers
    """
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b) if a and b else 0
    return reduce(lcm, numbers)


def play_lcm_game():
    """Execute the main LCM game logic."""
    name = welcome_user()
    print("Find the smallest common multiple of given numbers.")
    
    correct_answers_needed = 3
    correct_answers = 0
    
    while correct_answers < correct_answers_needed:
        numbers = generate_numbers()
        correct_answer = calculate_lcm(numbers)
        
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ").strip()
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is not a number!")
            print(f"Let's try again, {name}!")
            return
            
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_lcm_game()