# Задан список положительных чисел arr и положительное число k.
# Написать функцию minimum_steps, которая определяет сколько наименьших элементов списка
# в порядке возрастания нужно сложить, чтобы их сумма была больше или равна числу k
#
# Пример:
# minimum_steps([4,6,3], 7) ==> 2


import traceback


def minimum_steps(arr, k):
    s = 0
    k2 = 0
    while len(arr) > 0 and s < k:
        s += min(arr)
        k2 += 1
        del arr[arr.index(min(arr))]

    if s >= k:
        return k2
    else:
        return -1




# Тесты
try:
    assert minimum_steps([8,9,10,4,2], 23) == 4
    assert minimum_steps([19,98,69,28,75,45,17,98,67], 464) == 9
    assert minimum_steps([10,9,9,8], 17) == 2
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")