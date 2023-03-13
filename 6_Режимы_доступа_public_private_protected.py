class Point:
    def __init__(self,x,y):
        '''В данный момент переменные self.x и self.y - публичные'''
        self.x = x
        self.y = y

    '''Но существуют более безопасные модификации 
    >>> protected - структуры данных с использованием только в классе и
                его дочерних классах. Для этого надо перед названием
                перменной или ф-ции поставить _ . Однако это всего лишь
                формальность. Мы все равно сможем обратиться к такой 
                перменной/ф-ции где и когда угодно

    >>> private - структуры данных с использованием только в текущем классе
                Для этого надо перед названием перменной или ф-ции
                поставить __ (два нижних подчеркивания). Это не формальность, а
                действительно рабочая вещь. Мы не сможем обратиться к этому просто
                так. Но это все равно возможно! Для этого пишется так:
                Экземпляр._НазваниеКласса__ПриватныйОбъект '''

    @staticmethod
    def __private_method(a,b):
        return (type(a) and type(b)) in (int,float)
    
    def set_coord_protected(self,x,y):
        self._X, self._Y = x,y #protected

    def set_coord_private(self,x,y):
        self.__X, self.__Y = 0,0 #private
        if self.__private_method(x,y):
            self.__X, self.__Y = x,y

    def get_coord_private(self): #приватные координаты мы можем вывести только так
        return self.__X, self.__Y
    
    


pt = Point(1,2)
pt.set_coord_protected(10,20)
pt.set_coord_private(100,200)
print(pt.__dict__)
print(pt._X, pt._Y) # ошибки нет
#print(pt.__X,pt.__Y) #ошибка есть
print(pt.get_coord_private()) #ошибки нет
print(pt._Point__X, pt._Point__Y) #ошибки нет

pt.set_coord_private(100,'привет')
print(pt.get_coord_private()) #все сработало. Приватная функция сработала как надо
#print(pt.__private_method(1,2))#ошибка есть

'''Также более защищенно можно сделать с помощью библиотеки accessify
Оттуда мы импортируем два декоратора: protected и private'''