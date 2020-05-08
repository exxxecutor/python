import log

class Discipline:
    def __init__(self, name, semestr, cafedra):
        self.name = name
        self.semestr = semestr
        self.cafedra = cafedra
        log.log(log.CRE, f'Создан объект Discipline по адресу {self.__repr__()}')