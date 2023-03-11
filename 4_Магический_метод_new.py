class Point:
    '''Разница между __init__ и __new__ :
    __new__ вызывается ДО создания объекта, а
    __init__ вызывается сразу ПОСЛЕ создания объекта  
    '''

    def __new__(cls, *args, **kwargs):
        '''cls - ссылка на САМ КЛАСС (в нашем случае Point)'''

        print('вызов __new__' + str(cls))
        return super().__new__(cls) #обязательная строка!
    #попробуйте взять в комментарий строку с return и увидите что __init__
    #не вызовится, а print(pt) выведет None
    '''Если не написать return... то pt - не создастся!
        эта строка возвращает id созданного объекта'''

    def __init__(self,a,b):
        print('вызов __init__'+str(self)+'\n')
        self.A = a
        self.B = b

pt = Point(1,3)
print(pt)