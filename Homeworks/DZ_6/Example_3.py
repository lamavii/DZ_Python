# С помощью использования zip

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def sum_polynomials(poly_1: str, poly_2: str):  # Функция сложения многочленов
    poly_1 = poly_1.replace('+', ' + ').replace('x', ' x').split()
    poly_2 = poly_2.replace('+', ' + ').replace('x', ' x').split()
    result = [int(el_1) + int(el_2) if el_1.isdigit() and el_2.isdigit() else el_1\
              for el_1, el_2 in zip(poly_1[::-1], poly_2[::-1])]
    result.reverse()
    result = ''.join(map(str, result))
    if len(poly_1) != len(poly_2):
        symbol = result[result.find('x'):result.find('x') + 3]
        if len(poly_1) > len(poly_2):
            result = ''.join(map(str, poly_1[:poly_1.index(symbol)+1])) + '+' + result + '=0'
        else:
            result = ''.join(map(str, poly_2[:poly_1.index(symbol)+1]))+ '+' + result + '=0'
    return result


def main():
    p_1 = '35x^5+42x^4+12x^3+3x^2+46x+5'
    p_2 = '12x^6+14x^5+24x^4+21x^3+9x^2+64x+25'
    print(f'Многочлен №1 = {p_1}')
    print(f'Многочлен №2 = {p_2}')
    print(f'сумма многочленов = {sum_polynomials(p_1, p_2)}')


if __name__ == '__main__':
    main()