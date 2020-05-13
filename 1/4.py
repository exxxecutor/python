# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.

cars = [
    {
        'id': 123456,
        'model': 'Mercedes-Benz',
        'year': 2019,
        'price': 3000,
        'warranty': 5,
    },
    {
        'id': 123457,
        'model': 'Volkswagen',
        'year': 2017,
        'price': 1000,
        'warranty': 3,
    },
    {
        'id': 123458,
        'model': 'Toyota',
        'year': 2018,
        'price': 2000,
        'warranty': 7,
    },
    {
        'id': 123459,
        'model': 'Hummer',
        'year': 2016,
        'price': 4000,
        'warranty': 9,
    },
    {
        'id': 123460,
        'model': 'Kia',
        'year': 2019,
        'price': 2000,
        'warranty': 6,
    },
    {
        'id': 123461,
        'model': 'Peugeot',
        'year': 2016,
        'price': 1000,
        'warranty': 3,
    },
    {
        'id': 123462,
        'model': 'BMW',
        'year': 2019,
        'price': 5000,
        'warranty': 10,
    },
    {
        'id': 123463,
        'model': 'Audi',
        'year': 2015,
        'price': 1500,
        'warranty': 5,
    },
    {
        'id': 123464,
        'model': 'Alfa Romeo',
        'year': 2013,
        'price': 2000,
        'warranty': 5,
    },
    {
        'id': 123465,
        'model': 'Nissan',
        'year': 2016,
        'price': 1300,
        'warranty': 4,
    },
]

def getInfo(cars):
    for dict in cars:
        for item in dict.items():
            print(item[0], ":", item[1])
        print()

def find(cars):
    id = int(input("Enter car ID\n"))
    for dict in cars:
        if (dict.get('id') == id):
            return dict
    return -1

def getByYear(cars, year):
    k = 0
    for dict in cars:
        if dict.get('year') > year:
            k += 1
    return k

def delCar(cars, id):
    for ind, dict in enumerate(cars):
        if dict.get('id') == id:
            del cars[ind]
            return dict
    return -1

def refreshInfo(cars):
    dict = find(cars)
    for key in dict.keys():
        value = input("Enter " + key + ":\n")
        dict[key] = value

# getInfo(cars)
# print(getByYear(cars, 2017))
# delCar(cars, 123456)
# print(find(cars).get('model'))
refreshInfo(cars)
print(getInfo(cars))