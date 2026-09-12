#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
zoo.insert(1, 'bear')
zoo_after_bear = zoo[:]

# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
zoo.extend(birds)
zoo_after_birds = zoo[:]

# Уберите слона (elephant) из зоопарка
# и выведите список на консоль
zoo.remove('elephant')
zoo_after_elephant = zoo[:]

# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
lion_cage = zoo.index('lion') + 1
lark_cage = zoo.index('lark') + 1


def main():
    print(zoo_after_bear)
    print(zoo_after_birds)
    print(zoo_after_elephant)
    print(lion_cage)
    print(lark_cage)


if __name__ == '__main__':
    main()
