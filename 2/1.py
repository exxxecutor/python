# Написать функцию freq_seq(s, sep), которая возвращает строку s, заменив каждый
# символ числом - количеством повторов этого символа в строке, при этом
# sep - разделительный символ между числами
#
# Примеры:
# freq_seq("qqwwwerrtttt", "@")  => "2@2@3@3@3@1@2@2@4@4@4@4"

import traceback


def freq_seq(s, sep):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    s = list(s)

    for i in range(len(s)):
        s[i] = str(freq[s[i]])

    return sep.join(s)



# Тесты
try:
    assert freq_seq("hello world", "-") == "1-1-3-3-2-1-1-2-1-3-1"
    assert freq_seq("19999999", ":") == "1:7:7:7:7:7:7:7"
    assert freq_seq("^^^**$", "x") == "3x3x3x2x2x1"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")