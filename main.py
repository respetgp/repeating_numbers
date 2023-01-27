import re


def max_repeating_funktion(string_symbol):
    """
    Функция на вход от пользователя получает строку.
    Выводит числа, которые повторяются максимальное количество раз.
    Вывод нужен в порядке убывания.
    """
    string_symbols = re.sub("[^-0-9]", " ", string_symbol)
    string_symbols = string_symbols.split()   # составление словаря только из чисел
    string_symbols_part_time = {i: string_symbols.count(i) for i in string_symbols}    # сортировка по количеству повторений
    max_value = max(string_symbols_part_time.values())
    final_dict = {k: v for k, v in string_symbols_part_time.items() if v == max_value}   # выбор максимальных значений
    string_symbols_part_time = str(" ".join(final_dict.keys()))
    return string_symbols_part_time


assert max_repeating_funktion('[1, 2, 3, [5, 5], 6, [7, 8, 9, [10, 11]]]') == '5'
assert max_repeating_funktion('[5, 5, 1, 3, 1, 2]') == '5 1'
assert max_repeating_funktion('[[[[[[1]]]], []]]') == '1'
assert max_repeating_funktion('[0, 10, 2, 5, -999999999]') == '0 10 2 5 -999999999'
