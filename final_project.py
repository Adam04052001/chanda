from random import randint
import time
import click

# Для начала зададим ингридиенты каждого пиццы для размера L
# Размер Xl будет на 30% больше нашей пиццы размера L,
# а потому в нем будет на 30% больше каждого ингридиента.

Margherita_L = {'tomato sauce': 1, 'mozzarella': 1,'tomatoes': 1}
Pepperoni_L = {'tomato sauce': 1, 'mozzarella': 1, 'pepperoni': 1}
Hawaiian_L = {'tomato sauce': 1, 'mozzarella': 1, 'chicken': 1, 'pineapples': 1}



# Можем задать пиццу размера XL словарями, либо же написать функцию преобразования
# Margherita_xL = {'tomato sauce': 1.3, 'mozzarella': 1.3,'tomatoes': 1.3}
# Pepperoni_xL = {'tomato sauce': 1.3, 'mozzarella': 1.3, 'pepperoni': 1.3}
# Hawaiian_xL = {'tomato sauce': 1.3, 'mozzarella': 1.3, 'chicken': 1.3, 'pineapples': 1.3}
def xl_size(recipe_L):
    recipe_xL = recipe_L.copy()
    for ingridient in recipe_xL:
        recipe_xL[ingridient] *= 1.3
    return recipe_xL


class Pizza():
    def __init__(self, ingridient: dict = {}, size: str = 'L'):
        if size.upper() in ('L', 'XL'):
            self.size = size.upper()
        else:
            raise ValueError(f'Size {size} is not available')
        if size == 'L':
            self.ingridient = ingridient
        elif size == 'XL': 
            self.ingridient = make_xl_recipe(ingridient)

    def dict(self):
        """
        Функция возвращает рецепт пиццы ввиде словаря
        """
        return self.ingridient

    def __eq__(self, other):
        """
        Проверяет пиццы на равенство. Пиццы равны, если у них полностью равные рецепты
        """
        return self.ingridient == other.ingridient


class Margherita(Pizza):
    def __init__(self, ingridient: dict = MARGHERICA_RECIPE, size: str = 'L'):
        super().__init__(ingridient, size)


class Pepperoni(Pizza):
    def __init__(self, ingridient: dict = PEPPERONI_RECIPE, size: str = 'L'):
        super().__init__(ingridient, size)


class Hawaiian(Pizza):
    def __init__(self, ingridient: dict = HAWAIIAN_RECIPE, size: str = 'L'):
        super().__init__(ingridient, size)
        

menu = {'Margherita 🧀': Margherita_L, 'Pepperoni 🍕': Pepperoni_L ,'Hawaiian 🍍': Hawaiian_L}

@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery_flg', default = False, is_flag = True)
@click.option('--big_flg', default = False, is_flag = True)
@click.argument('pizza', nargs = 1)
def order(pizza: str, delivery_flg: bool, big_flg: bool):
    """Готовит и доставляет пиццу"""
    if big_flg:
        size = 'XL'
    else:
        size = 'L'
    if pizza == 'pepperoni':
        order_pizza = Pepperoni(size = size)
    elif pizza == 'margherita':
        order_pizza = Margherita(size = size)
    elif pizza == 'hawaiian':
        order_pizza = Hawaiian(size = size)
    bake(order_pizza)
    if delivery_flg:
        delivery(order_pizza)
    else:
        pickup(order_pizza)

