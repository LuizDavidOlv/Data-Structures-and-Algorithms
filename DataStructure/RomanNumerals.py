from typing import Dict

class IntegerToRoman:  
    def translate(number: int) -> str:
        romanNumerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        romanNumeral = ""
        for (integer,roman) in romanNumerals:
            while number >= integer:
                romanNumeral += roman
                number -= integer
        return romanNumeral

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    romanNumeral = IntegerToRoman.translate2(2576)
    #"MMDLXXVI"
    print("Roman Numeral:")
    print(romanNumeral)
    print('\n')



  