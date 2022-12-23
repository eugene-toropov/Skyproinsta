import pytest  # Импортируем необходимые модули и функции
from utils import get_posts_from_json, get_post_by_pk, get_comments_from_json, get_posts_by_user,\
    get_comments_by_post_id, get_posts_all, search_for_posts


def test_get_posts_from_json():
    """Тест функции get_posts_from_json().

    Обращаемся к функции и проверяем тип полученных данных"""
    data = get_posts_from_json()
    assert type(data) == list, "Полученные данные - не список"


def test_get_posts_all():
    """Тест функции get_posts_all().

    Обращаемся к функции и проверяем тип полученных данных"""
    data = get_posts_all()
    assert type(data) == list, "Полученные данные - не список"


def test_get_posts_by_user():
    """Тест функции get_posts_by_user().

    Обращаемся к функции по аргументу, проверяем тип полученных данных"""
    data = get_posts_by_user('larry')
    assert type(data) == list, "Полученные данные - не список"


def test_get_posts_by_user_value_error():
    """Тест функции get_posts_by_user().

    Обращаемся к функции с неправильным аргументом. Проверяем, что функция возвращает ошибку ValueError"""
    with pytest.raises(ValueError):
        get_posts_by_user('aaaa')


def test_get_posts_by_user_type_error():
    """Тест функции get_posts_by_user().

    Обращаемся к функции с аргументом неправильного типа. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        get_posts_by_user(2)


def test_get_posts_by_user_type_error_for_none():
    """Тест функции get_posts_by_user().

    Обращаемся к функции без аргумента. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        get_posts_by_user()


def test_get_comments_from_json():
    """Тест функции get_comments_from_json().

    Обращаемся к функции и проверяем тип полученных данных."""
    data = get_comments_from_json()
    assert type(data) == list, "Полученные данные - не список"


def test_get_comments_by_post_id():
    """Тест функции get_comments_by_post_id().

    Обращаемся к функции по аргументу, сравниваем тип полученных данных"""
    data = get_comments_by_post_id(2)
    assert type(data) == list, "Полученные данные - не список"


def test_get_comments_by_post_id_type_error():
    """Тест функции get_comments_by_post_id().

    Обращаемся к функции с аргументом неправильного типа. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        get_comments_by_post_id('3')


def test_get_comments_by_post_id_type_error_for_none():
    """Тест функции get_comments_by_post_id().

    Обращаемся к функции без аргумента. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        get_comments_by_post_id()


def test_get_comments_by_post_id_value_error():
    """Тест функции get_comments_by_post_id().

    Обращаемся к функции с аргументом неправильного значения. Проверяем, что функция возвращает ошибку ValueError"""
    with pytest.raises(ValueError):
        get_comments_by_post_id(33333333)


def test_search_for_posts():
    """Тест функции search_for_posts().

    Обращаемся к функции с аргументом. Проверяем тип полученных данных"""
    data = search_for_posts("еда")
    assert type(data) == list, "Полученные данные - не список"


def test_search_for_posts_type_error():
    """Тест функции search_for_posts().

    Обращаемся к функции с аргументом неправильного типа. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        search_for_posts(2)


def test_search_for_posts_type_error_for_none():
    """Тест функции search_for_posts().

    Обращаемся к функции без аргумента. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        search_for_posts()


def test_get_post_by_pk():
    """Тест функции get_post_by_pk().

    Обращаемся к функции с аргументом. Проверяем тип полученных данных"""
    data = get_post_by_pk(2)
    assert type(data) == dict, "Полученные данные - не список"


def test_get_post_by_pk_type_error():
    """Тест функции get_post_by_pk().

    Обращаемся к функции с аргументом неправильного типа. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        get_post_by_pk("2")


def test_get_post_by_pk_type_error_for_none():
    """Тест функции get_post_by_pk().

    Обращаемся к функции без аргумента. Проверяем, что функция возвращает ошибку TypeError"""
    with pytest.raises(TypeError):
        get_post_by_pk()


def test_get_post_by_pk_value_error():
    """Тест функции get_post_by_pk().

    Обращаемся к функции с аргументом неправильного значения. Проверяем, что функция возвращает ошибку ValueError"""
    with pytest.raises(ValueError):
        get_post_by_pk(0)

