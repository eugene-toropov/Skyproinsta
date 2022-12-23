import pytest
from utils import get_posts_from_json, get_post_by_pk, get_comments_from_json, get_posts_by_user,\
    get_comments_by_post_id, get_posts_all, search_for_posts


def test_get_posts_from_json():
    data = get_posts_from_json()
    assert type(data) == list, "Полученные данные - не список"


def test_get_posts_all():
    data = get_posts_all()
    assert type(data) == list, "Полученные данные - не список"


def test_get_posts_by_user():
    data = get_posts_by_user('larry')
    assert type(data) == list, "Полученные данные - не список"


def test_get_posts_by_user_value_error():
    with pytest.raises(ValueError):
        get_posts_by_user('aaaa')


def test_get_posts_by_user_type_error():
    with pytest.raises(TypeError):
        get_posts_by_user(2)


def test_get_posts_by_user_type_error_for_none():
    with pytest.raises(TypeError):
        get_posts_by_user()


def test_get_comments_from_json():
    data = get_comments_from_json()
    assert type(data) == list, "Полученные данные - не список"


def test_get_comments_by_post_id():
    data = get_comments_by_post_id(2)
    assert type(data) == list, "Полученные данные - не список"


def test_get_comments_by_post_id_type_error():
    with pytest.raises(TypeError):
        get_comments_by_post_id('3')


def test_get_comments_by_post_id_type_error_for_none():
    with pytest.raises(TypeError):
        get_comments_by_post_id()


def test_get_comments_by_post_id_value_error():
    with pytest.raises(ValueError):
        get_comments_by_post_id(33333333)


def test_get_comments_by_post_id_value_error_for_0():
    with pytest.raises(ValueError):
        get_comments_by_post_id(0)


def test_search_for_posts():
    data = search_for_posts("еда")
    assert type(data) == list, "Полученные данные - не список"


def test_search_for_posts_type_error():
    with pytest.raises(TypeError):
        search_for_posts(2)


def test_search_for_posts_type_error_for_none():
    with pytest.raises(TypeError):
        search_for_posts()


def test_get_post_by_pk():
    data = get_post_by_pk(2)
    assert type(data) == dict, "Полученные данные - не список"


def test_get_post_by_pk_type_error():
    with pytest.raises(TypeError):
        get_post_by_pk("2")


def test_get_post_by_pk_type_error_for_none():
    with pytest.raises(TypeError):
        get_post_by_pk()


def test_get_post_by_pk_value_error():
    with pytest.raises(ValueError):
        get_post_by_pk(0)
