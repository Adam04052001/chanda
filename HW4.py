import json
from keyword import iskeyword


# Для начала создадим класс, которую преобразвует формат JSON
# в удобный для нас питоновский словарь.
class ObjectTransformer():
    def __init__(self, mapping):
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = ObjectTransformer(value)
            else:
                self.__dict__[key] = value


# Создадис класс, который будет отвечать за смену цвета
# Его атрибутаеми будет звет фона (бэкграунд), и цвет текста.
class ColorizeMixin:
    def __init__(self, text_color=32, bg_color=40):
        self.text_color = text_color
        self.bg_color = bg_color
        
# Определим функцию,
# которая будет показывать строчное представление кода, 
# конечным пользователям
    def __str__(self):
        return f'\033[{self.text_color};{self.bg_color}m {self.__repr__()}'


class Advert(ColorizeMixin, ObjectTransformer):
    def __init__(self, mapping):
        ColorizeMixin.__init__(self)
        mapping_transformed = ObjectTransformer(mapping).__dict__
        if 'title' not in mapping_transformed:
            raise ValueError('Field "title" is required.')
        if 'price' in mapping_transformed:
            self.price = mapping_transformed['price']
        self.__dict__.update(mapping_transformed)

    def __repr__(self):
        return f'{self.title} | {self._price} ₽'
    
# Как нас и просили реализуем функцию репр, 
# которая будет показывать строковое предстваление объекта для разработчика.        
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('Price сannot be negetive.')
        self._price = new_price


'

     
