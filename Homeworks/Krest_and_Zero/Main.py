# import Module_Frontend as F
from Module_tic_tac_toe_2_players import two_players

#Этап 1:
# 1. Выбрал структуру для хранения данных для поля "крестиков-ноликов" (словарь).
# 2. Наполненил ее случайным состоянием для каждой ячейки: крестик, нолик, пусто
#    Вызов функции structure()
# 3. Рисование поля клеток с отображением текущего состояния (frontend в консоли):
#    Вызов функции rendering(dictinary: dict). Используем библиотеку Texttable
# 4. Создаем frontend модуль: все, что связано с прорисовкой поля и импортируем в основную программу:
#    Импортирем Module_Frontend и запускаем

# F

# Этап 2.
# - Интерактивность.
# Играют два игрока, каждый выбирает ячейку, в которую поставить свой знак (крестик или нолик)
# - Игроки делают свои ходы пока поле полностью не заполнится, потом выход из программы
# с соответствующим сообщением.
# - Полная проверка "на дурака", например, ячейка уже занята.
# Если используем номера ячеек, то корректность ввода данных от игрока.
# Вывод значимых и понятных для игрока сообщений о неправильных данных и возможность ошибаться сколько угодно раз.
# - Возможность игроку прервать игру в любой момент, "если надоест"
# - Изменение состояния системы, если ход игрока прошел верификацию
# - Отображение поля с новым состояние и переход хода к следующему игроку.

two_players()