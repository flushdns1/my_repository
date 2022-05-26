"""Игра угадай число"""

import numpy as np

max_number_value = 101
number = np.random.randint(1, max_number_value) # загадываем число

# количество попыток
count = 0

while True:
    count+=1
    
    predict_number = max_number_value / 2
    
    left_border = 0
    right_border = max_number_value
        
    if predict_number > number:
        #print("Число должно быть меньше!")
        right_border = predict_number

    elif predict_number < number:
        #print("Число должно быть больше!")
        left_border = predict_number
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла
