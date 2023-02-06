class Bag:
    def __init__(self, btype, manuf):
        self.__btype, self.__manuf = "Неизвестно", "Неизвестно"
        self.set_btype(btype)
        self.set_manuf(manuf)
    
    def info_bag(self):
        print(f'Тип сумки: {self.__btype}\n'
              f'Производитель: {self.__manuf}')
              
    def get_btype(self):
        return self.__btype

    def set_btype(self, val):
        if self.is_val(val):
            self.__btype = val
        else:
            print("ACHTUNG!!!")
    
    def get_manuf(self):
        return self.__manuf

    def set_manuf(self, val):
        if self.is_val(val):
            self.__manuf = val
        else:
            print("ACHTUNG!!!")
            
    @staticmethod
    def is_val(val):
        return isinstance(val, str) and not val.isdigit() and len(val) > 0

print("-"*10, "Инициализация данных ","-"*10)        
bag = Bag("Чемодан", "Англия")
bag.info_bag()
print("-"*10, "Проверка неверных данных ","-"*10)
bag.set_btype(666)
bag.set_manuf("")
print("-"*10, "Инициализация и вывод новых данных ","-"*10)
bag.set_btype("Рюкзак")
bag.set_manuf("Китай")
# print(bag.get_btype())
# print(bag.get_manuf())
bag.info_bag()
    
