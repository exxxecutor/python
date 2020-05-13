# Написать функцию order_weight, которая сортирует список положительных чисел.
# Критерий сортировки - возрастание веса числа (сумма всех цифр числа).
# Если два числа имеют одинаковый вес, сортировать их так, словно они строки.
#
# Примеры:
# [56, 65, 74, 100, 99, 68, 86, 180, 90] ==>
# [100, 180, 90, 56, 65, 74, 68, 86, 99]


import traceback


def order_weight(integers):

    newList = [];
    for idx, int in enumerate(integers):
        newInt = 0
        while int > 0:
            newInt += int % 10
            int //= 10
        newList.append(newInt)

    # selection sort with extra swaps for original arr
    for i in range(0, len(newList) - 1):
        for j in range(i, len(newList)):
            if newList[i] >= newList[j]:
                t = newList[i]
                newList[i] = newList[j]
                newList[j] = t
                # also swap corresponding elems in origin. arr
                t = integers[i]
                integers[i] = integers[j]
                integers[j] = t

    for int in newList:
        print(int, '//')

    for int in integers:
        print(int)

    return integers

# Тесты
try:
    assert order_weight([103, 123, 4444, 99, 2000]) == [2000, 103, 123, 4444, 99]
    assert order_weight([2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]) == [11, 11, 2000, 22, 10003, 123, 1234000, 44444444, 9999]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")