import os
from doctest import testmod
from abc import abstractmethod, abstractproperty, ABCMeta


class Shape(metaclass=ABCMeta):
    """
    Создайте абстрактный класс Shape для рисования плоских фигур
    Класс должен наследовать метакласс ABCMeta
    Определите абстрактные методы:
        show() - вывод на экран информации о фигуре
        save() - сохранение фигуры в файл
        load() - считывание фигуры из файла

    >>> type(Shape)
    <class 'abc.ABCMeta'>
    >>> shape = Shape()
    Traceback (most recent call last):
    ...
    TypeError: Can't instantiate abstract class Shape with abstract methods load, save, show
    """

    def __init__(self, point=(0, 0), length=0):
        self.__x = x
        self.__y = y
        self.__length = length

    @abstractmethod
    def show(self):
        print('x = ', self.__x, ', y = ', self.__y, ', length = ', self.__length)

    @abstractmethod
    def save(self, file):
        with open(file, 'w') as f:
            to_string = str(self.__x) + ' ' + str(self.__y) + ' ' + str(self.__length)
            f.write(to_string)

    @abstractmethod
    def load(self, file):
        with open(file) as f:
            prop = f.read()
            self.__x = int(prop[0])
            self.__y = int(prop[1])
            self.__length = int(prop[2])


class Square(Shape):
    """
    Square  - класс, производный от Square, который описывает квадрат и
    характеризуется координатами левого верхнего угла и длиной стороны

    Создайте конструктор с параметрами - координаты верхнего левого угла
    (кортеж значений (x, y)) и длина стороны.

    П араметры конструктора должны иметь значения по умолчанию: x = 0, y = 0
    length = 0

    Создайте три свойства: x, y и length для доступа к закрытым атрибутам
    объекта

    Реализуйте метод show, который должен выводит информацию о фигуре, например,
    если заданы координаты квадрата x = 10, y = 20 и длина 30, то вывод
    должен выглядеть так:

        Квадрат: x = 10, y = 20, length = 30

    Реализуйте метод save, кторый принимет имя файла, в котором будут сохранены
    данные о фигуре

    Реализуйте метод load, который считывает данные из заданного файла и устанавливает
    необходимые атрибуты объекта

    >>> point=(10, 20)
    >>> length = 30
    >>> square = Square(point, length)
    >>> square.show()
    Квадрат: x = 10, y = 20, length = 30
    >>> square.save('square.txt')
    >>> s = Square()
    >>> s.load('square.txt')
    >>> s.show()
    Квадрат: x = 10, y = 20, length = 30
    >>> s.x
    10
    >>> s.y
    20
    >>> s.length
    30
    """

    def __init__(self, point=(0, 0), length=0):
        self.__x = point[0]
        self.__y = point[1]
        self.__length = length


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def length(self):
         return self.__length

    def show(self):
        print('Квадрат: x = {}, y = {}, length = {}'.format(self.__x, self.__y, self.__length))

    def save(self, file):
        with open(file, 'w') as f:
            to_string = str(self.__x) + ' ' + str(self.__y) + ' ' + str(self.__length)
            f.write(to_string)

    def load(self, file):
        with open(file) as f:
            prop = f.read()
            l_prop = prop.split()
            self.__x = int(l_prop[0])
            self.__y = int(l_prop[1])
            self.__length = int(l_prop[2])


if __name__ == "__main__":
    testmod()




