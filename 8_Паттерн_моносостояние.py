class ThreadData:
    __shared_attrs = {
        'name': 'thread',
        'data': {},
        'id': 1
    }
    
    attrs = {
        1: 3,
        2: 4
    }
    def __init__(self):
        self.__dict__ = self.__shared_attrs
        '''теперь в каждом экземпляре класса словарь будет ссылаться на shared_attrs
        это значит,что любое создание,изменение и удаление аттрибутов класса будет происходить
        в shared_attrs. Следовательно -> у всех создаваемых экземпляров будет ВСЕГДА одинаковые атрибуты,
        причем не имеет значения в каком экземпляре вы меняете атрибут'''

th1 = ThreadData()
th2 = ThreadData()
print(th1.__dict__,'    ',th2.__dict__)
th1.id = 10
print(th1.__dict__,'    ',th2.__dict__)
del th2.data
print(th1.__dict__,'    ',th2.__dict__)