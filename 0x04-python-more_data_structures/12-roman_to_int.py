#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    int_value = 0
    for num in range(len(roman_string)):
        if num > 0 and roman_numerals[roman_string[num]] > roman_numerals[roman_string[num - 1]]:
            int_value += roman_numeral[roman_string[num]] - 2 * roman_numerals[roman_string[num - 1]]
        else:
            int_value += roman_numerals[roman_string[num]]
    return int_value
