import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)  # Загадываем число от 1 до 100
    attempts = 0

    print("Привет! Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
        guess = int(input("Введи свою догадку: "))
        attempts += 1

        if guess < number_to_guess:
            print("Загаданное число больше, чем твоя догадка.")
        elif guess > number_to_guess:
            print("Загаданное число меньше, чем твоя догадка.")
        else:
            print("Поздравляю! Ты угадал число", number_to_guess, "за", attempts, "попыток!")
            break

guess_number_game()
