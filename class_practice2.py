from operator import add
from functools import partial
from abc import ABC, abstractmethod


class ComputerColor(ABC):
    """Abstract class"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass

    
class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    
    def __init__(self, red_level: int, green_level: int, blue_level: int):
        if red_level > 255 or green_level > 255 or blue_level > 255:
            raise ValueError('chanda')
        self.red = red_level
        self.green = green_level
        self.blue = blue_level
        
    def __str__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'
        
    def __eq__(self, other):
        if isinstance(other, Color):
            if self.red == other.red and self.green == other.green and self.blue == other.blue:
                return True
            else:
                return False
        else:
            print('Does not fit')
        
    def __add__(self, other):
        color_mix = Color((self.red + other.red) // 2, (self.blue + other.blue) // 2, (self.green + other.green) // 2)
        return color_mix
        
    def __hash__(self):
        return hash((self.red, self.green, self.blue))
    
    def _contrast(self, c, value):
        cl = (-256) * (1 - c)
        f = (259 * (cl + 259)) / (255 * (259 - cl))
        l = f * (value - 128) + 128
        return int(l)

    def __mul__(self, other):
        if isinstance(other, float):
            contrast = partial(self._contrast, other)
            self.rgb = (self.red, self.green, self.blue)
        return Color(*map(contrast, self.rgb))


    def __rmul__(self, other):
        return self.__mul__(other)
      
if __name__ == '__main__':
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)

    color_list = [orange1, red, green, orange2]
    print(set(color_list))
    print(red * 0.5)
