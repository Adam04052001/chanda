import random
from abc import ABC, abstractmethod

# Создадим абстрактный класс Анимон с декораторами
class AnimeMon(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name
        self.exp = 0

    @classmethod
    @abstractmethod
    def inc_exp(clas_s):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass


# Создадим класс покемон, который наследуется от Анимона, и 
# зададим в нём базовые функции, включая магические
class Pokemon(AnimeMon):

    def __init__(self, name: str, poketype: str):
        super().__init__(name)
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'

    def exp(self):
        return self.exp

    def inc_exp(self, step_size: int):
        self.exp += step_size

        
# проведём обучение покемона-Анимона
def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)
            
            
# Создадим класс Дигемон, которые будет наследоваться от Анимона
class Digimon(AnimeMon):
    def __init__(self, name: str):
        super().__init__(name)
        
    def exp(self):
        return self.exp

    def inc_exp(self, value: int):
        self.exp += value * 8


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)

    train(bulbasaur)
    print(bulbasaur.exp)

    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
