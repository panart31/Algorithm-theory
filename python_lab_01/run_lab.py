# -*- coding: utf-8 -*-

import os
import runpy

folder = os.path.dirname(os.path.abspath(__file__))

files = [
    '00_distance.py',
    '01_circle.py',
    '02_operations.py',
    '03_favorite_movies.py',
    '04_my_family.py',
    '05_zoo.py',
    '06_songs_list.py',
    '07_secret.py',
    '08_garden.py',
    '09_shopping.py',
    '10_store.py',
]


def main():
    for name in files:
        print('-----', name, '-----')
        runpy.run_path(os.path.join(folder, name), run_name='__main__')
        print()


if __name__ == '__main__':
    main()
