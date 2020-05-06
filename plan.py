from discipline import Discipline
from academic import Academic
from practice import Practice


class Plan:
    """
Создать класс Plan. Поля: код направления, название направления, кафедр, список основных дисциплин (список
    экземпляров класса Academic), список практик (список экземпляров класса Practice). Определить конструктор.
    Переопределить метод преобразования в строку для печати всей информации об учебном плане (с использованием
    переопределения в классах Academic и Practice). Переопределить методы получения количества дисциплин
    функцией len, получения дисциплины по индексу, изменения по индексу, удаления по индексу (пусть вначале
    идут индексы основных дисциплин, затем практик). Переопределить операции + и - для добавления или удаления
    дисциплины. Добавить функцию создания txt-файла и записи всей информации в него (в том числе количество
    часов и тематику практик).
    """
    def __init__(self, code, name, cafedra, disciplines, practices):
        self.code = code
        self.name = name
        self.cafedra = cafedra
        self.disciplines = disciplines
        self.practices = practices

    def __str__(self):
        return f'{self.name}, code: {self.code}, cafedra: {self.cafedra}, {len(self.disciplines)} disciplines, {len(self.practices)} practices.'

    def __len__(self):
        return len(self.disciplines)

    def __getitem__(self, num):
        return self.disciplines[num]

    def __setitem__(self, key, value):
        self.disciplines[key] = value

    def __delitem__(self, key):
        l = len(self.disciplines)
        if key > l:
            del self.practices[key - l]
        else:
            del self.disciplines[key]

    def __add__(self, other):
        self.disciplines.append(other)

    def __sub__(self, other):
        if other in self.disciplines:
            return self.disciplines.pop(self.disciplines.index(other))

    def write_to_file(self):
        with open('info.txt', 'w') as f:
            f.write(str(self) + '\n')

            for discipline in self.disciplines:
                f.write(str(discipline) + '\n')

            for practice in self.practices:
                f.write(str(practice) + '\n')

if __name__=='__main__':
    plan = Plan(code=735,
                name='StringName',
                cafedra='IBetExists',
                disciplines=[
                    Academic(name='Math',
                             semestr=3,
                             cafedra='DontCareIfExists',
                             teacher='Random Guy',
                             control_form='exam',
                             hours={
                                'lecture': 3,
                                'practice': 9,
                                'labs': 3,}),
                    Academic(name='Physics',
                             semestr=3,
                             cafedra='DontCareIfExists',
                             teacher='Another Guy',
                             control_form='exam',
                             hours={
                                'lecture': 3,
                                'practice': 10,
                                'labs': 2,}),
                ],
                practices=[
                    Practice(name='Math',
                             semestr=3,
                             cafedra='DontCareIfExists',
                             type='educational',
                             senior='Real Guy',
                             theme=['Integration', 'Statistics']),
                    Practice(name='Math',
                             semestr=3,
                             cafedra='DontCareIfExists',
                             type='educational',
                             senior='Real Guy2',
                             theme=['Mechanics', 'Nuclear Something']),
                ])
    plan + Academic(name='Biology',
                    semestr=3,
                    cafedra='BiologyCafedra',
                    teacher='Some Guy',
                    control_form='exam',
                    hours={
                        'lecture': 3,
                        'practice': 10,
                        'labs': 2,})
    
    assert len(plan) == 3
    plan.write_to_file()
