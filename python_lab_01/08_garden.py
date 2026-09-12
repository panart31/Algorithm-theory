#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# Выведите на консоль все виды цветов
all_flowers = garden_set | meadow_set

# Выведите на консоль те, которые растут и там и там
both = garden_set & meadow_set

# Выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = garden_set - meadow_set

# Выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = meadow_set - garden_set


def main():
    print(all_flowers)
    print(both)
    print(only_garden)
    print(only_meadow)


if __name__ == '__main__':
    main()
