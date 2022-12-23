from json import JSONDecodeError
import json


def get_posts_from_json():
    try:
        with open("data/posts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        return f"{e} Файл не найден"
    except JSONDecodeError as e:
        return f"{e} Файл не удается преобразовать"


def get_posts_all():
    return get_posts_from_json()


def get_posts_by_user(user_name):

    if user_name == None:
        raise TypeError("Аргумент не найден")

    if type(user_name) != str:
        raise TypeError("Аргумент должен быть строкой")

    poster_names = []
    for post in get_posts_from_json():
        poster_names.append(post['poster_name'].lower())

    if user_name.lower() not in poster_names:
        raise ValueError("Пользователь не найден")

    posts_by_user_name = []
    for post in get_posts_all():
        if post['poster_name'] == user_name:
            posts_by_user_name.append(post)
    return posts_by_user_name


def get_comments_from_json():
    try:
        with open("data/comments.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def get_comments_by_post_id(post_id):

    if post_id <= 0:
        raise ValueError("Аргумент должен быть числом больше 0")

    if post_id == None:
        raise TypeError("Аргумент не найден")

    if type(post_id) != int or type(post_id) == float:
        raise TypeError("Аргумент должен быть целым числом")

    existing_ids = []
    for comment in get_comments_from_json():
        existing_ids.append(comment['post_id'])

    if post_id not in existing_ids:
        raise ValueError("Пост не найден")

    comments_by_post_id = []
    for comment in get_comments_from_json():
        if comment['post_id'] == post_id:
            comments_by_post_id.append(comment)
    return comments_by_post_id


def search_for_posts(word):

    if type(word) != str:
        raise TypeError("Аргумент должен быть строкой")

    if word == None:
        raise TypeError("Аргумент не найден")

    posts_with_word = []
    for post in get_posts_from_json():
        if word.lower() in post['content'].lower():
            posts_with_word.append(post)
    return posts_with_word


def get_post_by_pk(pk):

    if pk <= 0:
        raise ValueError("Аргумент должен быть положительным числом больше 0")

    if pk == None:
        raise TypeError("Аргумент не найден")

    if type(pk) == str or type(pk) == float:
        raise TypeError("Аргумент должен быть целым числом")

    for post in get_posts_from_json():
        if post['pk'] == pk:
            return post


