"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя метод format
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  и не делить слова.
"""


def wiki_function():
    f = open('roguelike.txt', "r")

    line = f.readline()
    stroki = []
    while line:
        if line != "\n":
            stroki.append(line)
        line = f.readline()

    for i in range(len(stroki)):
        stroki[i] = stroki[i].translate(str.maketrans('', '', string.punctuation))  ##удаление всех знаков препинания

    for i in range(len(stroki)):
        changer = ''.join([i for i in stroki[i] if not i.isdigit()])  ##удаление всех цифр
        stroki[i] = changer

    all_strok = "".join(stroki)  ##все строки в одной

    L = all_strok.split()  ##Разбитие на слова
    Unique = set(L)
    slovar = {}

    for word in Unique:
        slovar[word] = L.count(word)  ##количество вхождений

    list_slovar = list(M.items())
    list_slovar.sort(key=lambda i: i[1])
    list_slovar.reverse()  ##обратный порядок отсортированных слов

    j = 1
    list_2 = []
    for i in list_slovar:
        if (j <= 10):
            list_2.append(i[0])
            print("{} place --- {} --- {} times".format(j, i[0], i[1]))
            j += 1
        else:
            break

    python = []
    s = ''
    for word in all_strok.split():
        if word in list_2:
            word = 'PYTHON'
        if len(s + word) < 100:
            s = s + word + " "
        else:
            python.append(s)
            s = word + " "

    with open('antimage again.txt', 'w') as f:
        for line in python:
            f.write(line + '\n')

    f.close()
    return 1


# Вызов функции
wiki_function()
