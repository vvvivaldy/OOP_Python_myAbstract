class Person:
    def __init__(slef, name, old):
        slef.__name = name
        slef.__old = old
    
    '''У нас есть приватные переменные, значит,что без сетеров и гетеров мы не можем к ним обратиться'''
    # def get_old(self):
    #     return self.__old
    # def set_old(self, old):
    #     self.__old = old
    
    '''но чтобы сократить код ,увеличить читамость и не запоминать каждый 
    сеттер и гетер под каждую приватную переменную можно вопспользоваться св-вом property'''
    # def get_old(self):
    #         return self.__old
    # def set_old(self, old):
    #     self.__old = old
    
    # #первым вводится обязательно геттер,а потом сеттер
    # old = property(get_old,set_old)
    '''
    p = Person('Vasya',13)
    p.old = 15
    print(p.old)
    >>> 15
    Вот таким образом используя только св-во old можно пользоваться геттерами и сеттерами
    Более того, это св-во old будет обладать самым высоким приоритетом. Т.е. если в словаре класса
    уже будет например переменная old, то она не будет меняться т.к. приоритет этого св-ва выше'''

    
    
    '''Однако есть более простой способ использовать ту же конструкцию'''
    
    #сначала объявляем геттер!
    @property
    def old(self):
        return self.__old
    
    #здесь мы расширяем св-во old для добавления setter'a
    #FIXME причем названия ф-ций должны быть одинаковы, как в геттере
    @old.setter 
    def old(self, old):
        self.__old = old
    
    #здесь мы расширяем св-во old для добавления deletter'a
    @old.deleter
    def old(self):
        del self.__old
    
p = Person('Vasya',13)
print(p.old)
p.old = 30
print(p.old)
del p.old
print(p.__dict__)
p.old = 15
print(p.__dict__)