import click
from pizza import Pizza
from random import randint
from typing import Callable


def log(pattern='empty') -> Callable:
    def decorator(func) -> Callable:
        def wrapper(name) -> str:
            time = func(name)
            if pattern == 'empty':
                return f'{func.__name__} - {time} c'
            else:
                return pattern.format(name, time)
        return wrapper
    return decorator


@log('Приготовили {} за {}с!')
def bake(pizza: str) -> int:
    """Возвращает время приготовления пиццы в зависимости от заказа"""
    if pizza in ('pepperoni', 'margherita'):
        return randint(5, 15)
    else:
        return randint(7, 17)


@log('🛵 Доставили {} за {}с!')
def delivery_(pizza: str) -> int:
    """Возвращает время доставки заказа"""
    return randint(1, 30)


@log('🏠 Забрали {} за {}с!')
def pickup(pizza: str) -> int:
    """Возвращает время самовывоза"""
    return randint(1, 15)


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    print(bake(pizza))
    if delivery:
        print(delivery_(pizza))
    else:
        print(pickup(pizza))


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for pizza_type in Pizza.ingrediens_extra.keys():
        pizza = Pizza(pizza_type)
        recipe = ", ".join(key for key, value in pizza.recipe.items() if value)
        print(f'- {pizza_type}: {recipe}')


if __name__ == '__main__':
    cli()
