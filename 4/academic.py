from discipline import Discipline
from practice import Practice
import log

class Academic(Discipline):
    """
    Создать производный от Discipline класс Academic. Новые поля: преподаватель, форма контроля (зачет или экзамен),
    часы (словарь вида форма занятия (лекция/лабораторная/практическая): количество занятий). Определить конструктор,
    с вызовом родительского конструктора. Определить функции изменения преподавателя и формы контроля,
    форматированной печати количества занятий различного вида. Переопределить метод преобразования в строку
    для печати основной информации (название, семестр, кафедра, преподаватель, форма контроля).
    """

    CLASS_LENGTH = 1.5

    def __init__(self, name, semestr, cafedra, teacher, control_form, hours):
        super().__init__(name, semestr, cafedra)
        self.teacher = teacher
        self.control_form = control_form
        self.hours = hours
        log.log(log.CRE, f'Создан объект Academic по адресу {self.__repr__()}')

    
    def set_teacher(self, teacher):
        log.log(log.INF, f'Измененено поле teacher объекта Academic по адресу {self.__repr__()}')
        self.teacher = teacher

    def set_control_form(self, control_form):
        self.control_form = control_form
        log.log(log.INF, f'Измененено поле control_form объекта Academic по адресу {self.__repr__()}')

    def print_hours(self):
        for class_type, amount in self.hours.items():
            print(str(amount * Academic.CLASS_LENGTH) + ' hours of ' + class_type)
            log.log(log.INF, f'Распечатано количество часов дисциплины {class_type} объекта Academic по адресу {self.__repr__()}')


    def __str__(self):
        return f'Academic {self.name}, in {self.semestr} semestr, on {self.cafedra} cafedra, by {self.teacher}. Control form: {self.control_form}'


if __name__=='__main__':
    academic = Academic(name='Math',
                        semestr=3,
                        cafedra='DontCareIfExists',
                        teacher='Random Guy',
                        control_form='exam',
                        hours={
                            'lecture': 3,
                            'practice': 10,
                            'labs': 2,
                        })
    academic.set_teacher('Alex Black')
    assert academic.teacher == 'Alex Black'
    academic.set_control_form('zachet')
    assert academic.control_form == 'zachet'
    academic.print_hours()
    print(str(academic))
