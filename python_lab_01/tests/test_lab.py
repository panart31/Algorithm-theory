from helpers import load_task


distance = load_task('00_distance.py')
circle = load_task('01_circle.py')
operations = load_task('02_operations.py')
movies = load_task('03_favorite_movies.py')
family = load_task('04_my_family.py')
zoo = load_task('05_zoo.py')
songs = load_task('06_songs_list.py')
secret = load_task('07_secret.py')
garden = load_task('08_garden.py')
shopping = load_task('09_shopping.py')
store_mod = load_task('10_store.py')


def test_distances():
    d = distance.distances
    assert 'Moscow' in d
    assert 'London' in d['Moscow']
    assert 'Moscow' not in d['Moscow']
    x1, y1 = distance.sites['Moscow']
    x2, y2 = distance.sites['London']
    assert d['Moscow']['London'] == ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    assert d['Moscow']['London'] == d['London']['Moscow']


def test_circle():
    assert circle.area == 5541.7693
    assert circle.point_1_in is True
    assert circle.point_2_in is False


def test_operations():
    assert operations.result == 25


def test_movies():
    assert movies.first_movie == 'Терминатор'
    assert movies.last_movie == 'Назад в будущее'
    assert movies.second_movie == 'Пятый элемент'
    assert movies.second_from_end == 'Чужие'


def test_family():
    assert len(family.my_family) >= 3
    assert family.father_height == family.my_family_height[0][1]
    assert family.total_height == 178 + 164 + 172


def test_zoo():
    assert zoo.zoo_after_bear == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']
    assert zoo.zoo_after_birds[-3:] == ['rooster', 'ostrich', 'lark']
    assert 'elephant' not in zoo.zoo_after_elephant
    assert zoo.lion_cage == 1
    assert zoo.lark_cage == 7


def test_songs():
    assert songs.three_songs == 14.93
    assert songs.other_three == 13.49


def test_secret():
    assert secret.word1 == 'в'
    assert secret.word2 == 'бане'
    assert secret.word3 == 'веник'
    assert secret.word4 == 'дороже'
    assert secret.word5 == 'денег'


def test_garden():
    assert garden.garden_set == set(garden.garden)
    assert garden.meadow_set == set(garden.meadow)
    assert garden.all_flowers == garden.garden_set | garden.meadow_set
    assert garden.both == garden.garden_set & garden.meadow_set
    assert garden.only_garden == garden.garden_set - garden.meadow_set
    assert garden.only_meadow == garden.meadow_set - garden.garden_set


def test_shopping():
    assert shopping.sweets['печенье'][0]['shop'] == 'пятерочка'
    assert shopping.sweets['печенье'][0]['price'] == 9.99
    assert shopping.sweets['конфеты'][0]['shop'] == 'магнит'
    assert shopping.sweets['карамель'][0]['price'] == 41.99
    assert shopping.sweets['пирожное'][0]['price'] == 59.99
    for name in shopping.sweets:
        assert len(shopping.sweets[name]) == 2


def test_store(capsys):
    store_mod.main()
    text = capsys.readouterr().out
    assert 'Лампа - 27 шт, стоимость 1134 руб' in text
    assert 'Стол - 54 шт, стоимость 27860 руб' in text
    assert 'Диван - 3 шт, стоимость 3550 руб' in text
    assert 'Стул - 105 шт, стоимость 10311 руб' in text
