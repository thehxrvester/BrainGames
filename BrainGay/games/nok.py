# games/nok.py
import math
import random

def get_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    # функция для нахождения НОК двух чисел
    def lcm(x, y):
        return abs(x * y) // math.gcd(x, y)

    answer = lcm(a, b)
    return question, answer