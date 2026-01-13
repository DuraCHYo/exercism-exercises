def steps(number):
    steps_to_become_one = 0
    # пока нумбер больше 0 и не равняется 1, то делаем это
    if number > 1:
        while number != 1:
            # если нумбер четный - присваиваем нумберу его же, но поделенного на 2, и инкремент на шаг +1
            if number % 2 == 0:
                number = number / 2
                print(f' Число четное: {number}')
                steps_to_become_one += 1
                # если нумбер нечетный - присваиваем нумберу его же, но умноженного на 3 и добавляем в нему +1, и инкремент на шаг +1
            else:
                number = ((number * 3) + 1)
                print(f'Число нечетное: {number}')
                steps_to_become_one += 1
                # если нумбер == 1 выводим количество шагов
    elif number == 1:
        return steps_to_become_one
        # если ошибка значения
    else:
        raise ValueError("Only positive integers are allowed")
    return steps_to_become_one