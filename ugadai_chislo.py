#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Простая игра "Угадай число"
Компьютер загадывает число от 1 до 100, а вы пытаетесь его угадать!
"""

import random
import sys

# Настройка кодировки для Windows консоли
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def main():
    print("=" * 50)
    print(">>> Добро пожаловать в игру 'Угадай число'! <<<")
    print("=" * 50)
    print("\nЯ загадал число от 1 до 100.")
    print("Попробуйте угадать его за минимальное количество попыток!\n")
    
    # Загадываем случайное число
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Получаем число от пользователя
            guess = input(f"Попытка {attempts + 1}/{max_attempts}. Введите число: ")
            guess = int(guess)
            attempts += 1
            
            # Проверяем угадали ли
            if guess == secret_number:
                print("\n" + "=" * 50)
                print(f"*** Поздравляю! Вы угадали число {secret_number}! ***")
                print(f"Количество попыток: {attempts}")
                
                if attempts == 1:
                    print("Невероятно! Вы угадали с первой попытки! ***")
                elif attempts <= 3:
                    print("Отличный результат!")
                elif attempts <= 5:
                    print("Хорошая игра!")
                else:
                    print("Неплохо!")
                
                print("=" * 50)
                break
            elif guess < secret_number:
                print(f"[!] Загаданное число больше {guess}")
            else:
                print(f"[!] Загаданное число меньше {guess}")
            
            # Подсказка оставшихся попытках
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"У вас осталось {remaining} попыток.\n")
            
        except ValueError:
            print("[!] Пожалуйста, введите целое число!\n")
            continue
    
    # Если не угадали
    if attempts >= max_attempts and guess != secret_number:
        print("\n" + "=" * 50)
        print(f"К сожалению, вы не угадали число за {max_attempts} попыток.")
        print(f"Загаданное число было: {secret_number}")
        print("Попробуйте еще раз!")
        print("=" * 50)
    
    # Спрашиваем, хочет ли игрок сыграть еще раз
    play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower().strip()
    if play_again in ['да', 'д', 'yes', 'y']:
        print("\n" * 2)
        main()
    else:
        print("\nСпасибо за игру! До встречи!")

if __name__ == "__main__":
    main()

