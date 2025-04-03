import math
import random


while True:
    try:
        # Lista para armazenar os números
        numbers = []
        for i in range(1, 6):
            num = random.randint(1, 49)
            if num not in numbers:
                numbers.append(num)
        
        print('Números:')
        print(numbers)  # Exibe os números gerados
        
        print('\nEstrelas:')
        # Lista para armazenar as estrelas
        stars = []
        for i in range(1, 3):
            num2 = random.randint(1, 10)
            if num2 not in stars:
                stars.append(num2)
        
        print(stars)  # Exibe as estrelas geradas
        break
    except ValueError:
        print("Valor inválido! Tente novamente.")

