import string
def rows(letter):
    
    if letter == "A":
        return list(letter)
    else:
        ascii_letters = string.ascii_uppercase
        target_index = ascii_letters.find(letter)
    
        rows = []
        # Генерируем верхнюю часть алмаза (включая серединную строку)
        for i in range(target_index + 1):
            current_letter = ascii_letters[i]
    
            # Вычисляем внешние отступы
            outer_padding = " " * (target_index - i)
    
            if i == 0:
                # Для буквы 'A' особый случай — она одна
                row = f"{outer_padding}A{outer_padding}"
            else:
                # Для остальных букв считаем внутренние отступы
                inner_padding = " " * (2 * i - 1)
                row = f"{outer_padding}{current_letter}{inner_padding}{current_letter}{outer_padding}"
    
            rows.append(row)
    
        # Собираем алмаз целиком: верхняя часть + нижняя (перевернутая верхняя без центральной строки)
        # rows[:-1][::-1] берет все строки, кроме последней (центральной), и переворачивает их
        full_diamond = rows + rows[:-1][::-1]
    
        return(full_diamond)
