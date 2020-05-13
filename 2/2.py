# Написать функцию blocks, которая получает строку, состоящую из букв и цифр и возвращает строку в виде блоков,
# разделенных символом дефис. Элементы блока должны быть отсортированы по принципу, указанному ниже, и
# каждый блок не может содержать несколько экземпляров одного и того же символа.
# Порядок блоков:
# строчные буквы (a - z) в алфавитном порядке
# заглавные буквы (A - Z) в алфавитном порядке
# цифры (0 - 9) в порядке возрастания
#
#
# Примеры:
# blocks("21AxBz") ==> "xzAB12"
# blocks("abacad") ==> "abcd-a-a"

import traceback


def key_func(a):
    if a.isupper():
        # to make sure it goes after any lower
        return ord(a) + 100
    elif a.isdigit():
        # make sure it goes after any literal
        return ord(a) + 200

    # lower goes before anything
    return ord(a)


def blocks(s):
    freq = {}
    maxFreq = 0

    # find freq.
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        if freq[char] > maxFreq:
            maxFreq = freq[char]

    res = []
    # list(filter(bool, freq.values()))
    for i in range(maxFreq):

        tempres = []
        for (k, v) in freq.items():
            if v:
                tempres.append(k)
                freq[k] -= 1

        tempres.sort(key=key_func)
        tempres.append('-')
        res.extend(tempres)

    del res[-1]
    print(''.join(res))
    return ''.join(res)

# Тесты
try:
    assert blocks("21AxBz") == "xzAB12"
    assert blocks("abacad") == "abcd-a-a"
    assert blocks("heyitssampletestkk") == "aehiklmpsty-ekst-est"
    assert blocks(
        "6zjX9qcwTIuYNvdmL3CtElHa2n0rogKsSVPRWG4QAMUOe8JkyfxZDiBpb1Fh75GUTLMcbio7HO6rvn1NtDRmPJAejuXVFgaZI3pK90s4fBzqwEd5yWCQh8Sl2kxY") == \
           "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")