class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls,arg):
        '''Метод класса. Может обращаться к локальным атрибутам класса, 
        но не может обращаться к атрибутам экземпляра класса'''
        '''NOTE: Это значит,что мы не можем использовать этод метод для изменения
          каких либо значений экземпляра класса'''
        return cls.MIN_COORD <= arg <=cls.MAX_COORD

    def __init__(self, x,y):
        self.X = self.Y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.X = x
            self.Y = y
        ''' Есть более универсальный способ:
                if self.validate(x) and self.validate(y):
                    self.X = x
                    self.Y = y
            Да, мы пишем self. Т.к. эта ссылка содержит и информацию о классе
            По этому интерпритатор поймет к какому классу мы обращаемся'''
        print(self.norm2(self.X,self.Y)) #пример работы статической ф-ции

    def get_coord(self):
        return self.X, self.Y
    
    @staticmethod
    def norm2(x,y):
        '''Статический метод. 
        Метод не имеет доступа к атрибутам КЛАССА и к атрибутам ЭКЗЕМПЛЯРА
        Обычно это какие-то вспомогательные функции. Их можно использовать везде'''
        #если очень хочется обратиться к атрибутам класса,то пишите так:
        # Vector.MAX_COORD ... надо обращаться полностью, что не очень хорошо
        return x*x + y*y
    
v = Vector(10,20)
print(Vector.norm2(1,2),"Я вызвал напрямую")
print(v.norm2(v.X,v.Y),'Вызвал через экземпляр')
print(Vector.validate(5)) #мы можем даже вызвать этот метод таким образом
res = v.get_coord() #первый способ
# res = Vector.get_coord(v) - второй способ
print(res)