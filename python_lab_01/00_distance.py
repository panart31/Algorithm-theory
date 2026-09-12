#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

for city1 in sites:
    distances[city1] = {}
    for city2 in sites:
        if city1 != city2:
            x1 = sites[city1][0]
            y1 = sites[city1][1]
            x2 = sites[city2][0]
            y2 = sites[city2][1]
            distances[city1][city2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def main():
    print(distances)


if __name__ == '__main__':
    main()
