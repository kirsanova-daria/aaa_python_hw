from typing import Dict


class Pizza:
    ingrediens_base = ('tomato sause', 'mozzarella')
    ingrediens_extra = {
        'Margherita': ('tomatoes',),
        'Pepperoni': ('pepperoni',),
        'Hawaiian': ('chicken', 'pineapples')}

    def __init__(self, name: str, s='XL') -> None:
        """Инициализирует словарь recipe, где 0 значит отсуствуе ингиридиента,
        1 - наоборот"""
        self.name = name
        self.size = s
        self.recipe = dict()
        for ing in self.ingrediens_base:
            self.recipe[ing] = 1

        for type, ings in self.ingrediens_extra.items():
            if type == self.name:
                for i in ings:
                    self.recipe[i] = 1
            else:
                for i in ings:
                    self.recipe[i] = 0

    def dict(self) -> Dict:
        return self.recipe

    def __eq__(self, other: object) -> bool:
        """Сравнивает пиццы: по названию и размеру"""
        return self.name == other.name and self.size == other.size


class Margherita(Pizza):
    def __init__(self, s: int) -> None:
        super().__init__('Margherita', s)


class Pepperoni(Pizza):
    def __init__(self, s: int) -> None:
        super().__init__('Pepperoni', s)


class Hawaiian(Pizza):
    def __init__(self, s: int) -> None:
        super().__init__('Hawaiian', s)


if __name__ == '__main__':
    m = Margherita('L')
    m1 = Margherita('L')
    p = Pepperoni('XL')
    print(m.dict())
    print(m == m1)
