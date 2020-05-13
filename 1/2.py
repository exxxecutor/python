# Написать функцию кодирования encode(message, key)
# Процесс шифрования: каждой букве латинского алфавита abcdefghijklmnopqrstuvwxyz
# последовательно ставится в соответствие число от 1 до 26.
# Дальше к каждому числу последовательно прибавляется цифры из ключа.
#
# Пример:
# слово: abcxyz, код: 4567 =>
# [a->1, b->2, c->3, x->24, y->25, z->26] =>
# [1 + 4, 2 + 5, 3 + 6, 24 + 7, 25 + 4, 26 + 5] => код: [5, 7, 8, 31, 29, 31]


import traceback


def encode(message, key):
    newMessage = []
    for char in message:
        newMessage.append(ord(char) - 96)

    rankList = []
    while (key > 0):
        rankList.insert(0, key % 10)
        key //= 10

    for idx, key in enumerate(newMessage):
        newMessage[idx] += rankList[idx % len(rankList)]

    return newMessage


# Тесты
try:
    assert encode("scout", 1939) == [20, 12, 18, 30, 21]
    assert encode("masterpiece", 1939) == [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")