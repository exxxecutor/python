from discipline import Discipline
import log

class Practice(Discipline):
    """
    Создать производный от Discipline класс Practice. Новые поля: вид практики (учебная/производственная/преддипломная),
    руководитель практики, тематика практики (список тем). Определить конструктор, с вызовом родительского
    конструктора. Определить функции изменения руководителя, добавления, удаления и изменения тематики.
    Переопределить метод преобразования в строку для печати основной информации (название, вид практики, семестр,
    кафедра, руководитель).
    """

    def __init__(self, name, semestr, cafedra, type, senior, theme):
        super().__init__(name=name,
                         semestr=semestr,
                         cafedra=cafedra)
        self.type = type
        self.senior = senior
        self.theme = theme
        log.log(log.CRE, f'Создан объект Practice по адресу {self.__repr__()}')

    def set_senior(self, senior):
        self.senior = senior
        log.log(log.INF, f'Измененено поле senior объекта Practice по адресу {self.__repr__()}')

    def add_theme(self, theme):
        self.theme.append(theme)
        log.log(log.INF, f'Добавлена тема у объекта Practice по адресу {self.__repr__()}')


    def remove_theme(self, theme):
        if theme in self.theme:
            self.theme.pop(self.theme.index(theme))
            log.log(log.INF, f'Удалена тема у объекта Practice по адресу {self.__repr__()}')

    def change_theme(self, theme):
        self.theme = theme
        log.log(log.INF, f'Изменены темы у объекта Practice по адресу {self.__repr__()}')

    def __str__(self):
        return f'Practice {self.name}, type: {self.type}, semestr: {self.semestr}, cafedra: {self.cafedra}, senior: {self.senior}, themes: {self.theme}'


if __name__=='__main__':
    practice = Practice(name='Math',
                        semestr=3,
                        cafedra='DontCareIfExists',
                        type='educational',
                        senior='Real Guy',
                        theme=['Integration', 'Statistics'])
    practice.set_senior('Alex Black')
    assert practice.senior == 'Alex Black'
    practice.add_theme('AnotherTheme')
    assert 'AnotherTheme' in practice.theme
    practice.remove_theme('AnotherTheme')
    assert 'AnotherTheme' not in practice.theme
    new_themes = ['OneTheme']
    practice.change_theme(new_themes)
    assert practice.theme == new_themes
    print(str(practice))
