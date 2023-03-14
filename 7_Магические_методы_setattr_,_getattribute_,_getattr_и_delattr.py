print()
'''                             МАГИЧЕСКИЕ МЕТОДЫ ДЛЯ АТРИБУТОВ

>>> __setattr__(self,key,value) - автоматически вызыватся при изменении свойства класса key
>>> __getattribute__(self,item) - автоматически вызыватся при получении свойства класса с именем item
                                                        ^^^(возвращает знач атрибута,к которому обращаемся)
>>> __getattr__(self,item) - автоматически вызыватся при получении несещуствующего свойства класса tem
>>> __delattr__(self,item) - автоматически вызыватся при удалении свойства item(не важно: существует или нет)

'''
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def set_bound(self,left): #метод,в котором мы хотим изменить атрибуты класса
        self.MIN_COORD = left #МЫ не можем так сделать!
        # оператор присвоения (=) создает в экземпляре новый атрибут

    '''Сделаем теперь номарльно, так как получиться изменить значение атрибутов класса'''
    @classmethod
    def set_bound(cls,left):
        cls.MIN_COORD = left

    def __getattribute__(self,item):
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self,item)
        
    def __setattr__(self, key,value):
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self,key,value)

    def __getattr__(self,item):
        return False
    
    def __delattr__(self, item):
        print('__delattr__:',item)
        object.__delattr__(self,item)


pt1 =Point(1,2)
pt2 =Point(1,2)

# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)

''' тест __getattribute__ '''
#a = pt1.x # error
a = pt1.y #все ок
print(a)

''' тест __setattr__'''
# pt1.z = 5 #ошибка
pt1.s = 10 #все ок

''' тест __getattr__'''
print(pt1.qq) #False
#без этого метода выводило бы ошибку

''' тест __delattr__'''
del pt1.s #сначала выполниться print
#затем атрибут удалиться
print(pt1.__dict__)
