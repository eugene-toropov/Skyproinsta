import json  # Импортируем необходимые библиотеки, модули и функции.
from app import app
import pytest
from utils import get_post_by_pk, get_posts_all
import random


def test_api_post():
    """Тест-функция для проверки API-представления по маршруту '/api/posts/<post_pk>'

    Создаем переменную-путь path, к которой каждую новую проверку прибавляем переменную rand_int(случайное число)
    в качестве части маршрута представления <post_id>.
    При помощи функции test_client() с указанным путем обращаемся к представлению. Полученные данные
    обрабатываем при помощи команды json.loads(), получаем словарь. Из полученного словаря собираем ключи
    в множество real_keys.
    Обращаемся к функции get_post_by_pk() с аргументом rand_int,
    получаем словарь, из него берем список ключей и помещаем в множество reference_keys.
    Сравниваем полученные из представления ключи(real_keys) с эталонными(reference_keys).
    Сравниваем тип полученных данных из представления с ожидаемым типом.
    В случае провальной проверки возвращаем соответствующие сообщения."""

    rand_int = random.randint(1, 8)
    path = '/api/posts/' + str(rand_int)

    response = app.test_client().get(path)
    data = json.loads(response.data)

    data_from_file = get_post_by_pk(rand_int)

    real_keys = set(data.keys())
    reference_keys = set(data_from_file.keys())

    assert real_keys == reference_keys, "Полученные ключи отличаются от ожидаемых"
    assert type(data) == dict, "Неверный формат данных"


def test_api_all_posts():
    """Тест-функция для проверки API-представления по маршруту '/api/posts'

        При помощи функции test_client() с указанным путем обращаемся к представлению. Полученные данные
        обрабатываем при помощи команды json.loads(), получаем список.
        Обращаемся к функции get_posts_all(), получаем список, при помощи цикла собираем у каждого элемента ключи
        и помещаем в множество reference_keys.
        При помощи цикла for собираем ключи каждого элемента полученых из представления данных в множество real_keys
        и сравниваем их с эталонными(reference_keys).
        Сравниваем тип полученных данных из представления с ожидаемым типом.
        В случае провальной проверки возвращаем соответствующие сообщения."""

    response = app.test_client().get('/api/posts')
    data = json.loads(response.data)

    reference_keys = set()
    items = get_posts_all()
    for item in items:
        reference_keys.update(item.keys())

    for dict_ in data:
        real_keys = set(dict_.keys())
        assert real_keys == reference_keys, "Полученные ключи отличаются от ожидаемых"

    assert type(data) == list, "Неверный формат данных"

