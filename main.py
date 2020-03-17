import numpy as np
def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    # начальные значения
    count = 0
    min = 1
    max = 101
    predict = 50
    while True:
        count+=1
        # метод дихотомии (делении диапазона пополам)
        
        if number == predict: return(count) # выход из цикла, если угадали
        elif number > predict: # если число больше, то диапазон делим пололам вправо
            if predict == min:
                predict = max
            else:
                min = predict
                predict = np.round(np.mean((min, max)))
        elif number < predict: # если меньше, то влево
            if predict == max:
                predict = min
            else:
                max = predict
                predict = np.round(np.mean((min, max)))

def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v1)