from json import JSONDecodeError  # Импортируем необходимые библиотеки и модули
import json


def get_posts_from_json():
    """Функция загрузки данных из файла.

    Используя конструкцию try/except при помощи оператора with open открываем JSON файл.
    Вызываем исключения если файл не найден или его не удается преобразовать.
    Возвращаем список"""
    try:
        with open("data/posts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        return f"{e} Файл не найден"
    except JSONDecodeError as e:
        return f"{e} Файл не удается преобразовать"


def get_posts_all():
    """Функция возвращения данных с обращением к предыдущей функции.

    Возвращает список словарей"""
    return get_posts_from_json()


def get_posts_by_user(user_name):
    """Функция поиска постов по имени пользователя

    Проверяем тип аргумента и наличие его в списке имен пользователей,
    в случае провальной проверки вызываем исключение с соответствующим сообщением.
    Обращаемся к функции get_posts_all() и при помощи цикла for проходим по полученным данным,
    сравнивая аргумент user_name со значением по ключу "poster_name". При соответствии добавляем
    данные о посте в пустой список и возвращаем список"""

    if type(user_name) != str:
        raise TypeError("Аргумент должен быть строкой")

    poster_names = []
    for post in get_posts_all():
        poster_names.append(post['poster_name'].lower())

    if user_name.lower() not in poster_names:
        raise ValueError("Пользователь не найден")

    posts_by_user_name = []
    for post in get_posts_all():
        if post['poster_name'] == user_name:
            posts_by_user_name.append(post)
    return posts_by_user_name


def get_comments_from_json():
    """Функция загрузки комментариев из JSON файла.

    Используя конструкцию try/except при помощи оператора with open открываем JSON файл.
    Вызываем исключения если файл не найден или его не удается преобразовать.
    Возвращаем список"""
    try:
        with open("data/comments.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def get_comments_by_post_id(post_id):
    """Функция поиска комментариев по аргументу post_id

    Проверяем тип аргумента и наличие в списке существующих id постов,
    в случаем провальной проверки вызываем исключения и возвращаем соответствующие сообщения.
    Обращаемся к функции get_comments_from_json() и при помощи цикла for проходим по полученным данным,
    сравнивая аргумент post_id со значением по ключу "post_id". При соответствии добавляем данные о комментарии
    в пустой список и возвращаем список"""

    if post_id <= 0:
        raise ValueError("Аргумент должен быть числом больше 0")

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
    """Функция поиска поста по аргументу word.

    Проверяем тип аргумента, при провальной проверки вызываем исключение и возвращаем соответствующее сообщение.
    Обращаемся к функции get_posts_from_json() и при помощи цикла for проходим по полученным данным,
    проверяя наличие аргумента word в значении по ключу 'content'. При соответствии добавляем данные о посте
    в пустой список и возвращаем список"""

    if type(word) != str:
        raise TypeError("Аргумент должен быть строкой")

    posts_with_word = []
    for post in get_posts_from_json():
        if word.lower() in post['content'].lower():
            posts_with_word.append(post)
    return posts_with_word


def get_post_by_pk(pk):
    """Функция поиска поста по аргументу pk.

    Проверяем тип аргумента и его значение, в случаем провальной проверки вызываем исключения
    и возвращаем соответствующие сообщения.
    Обращаемся к функции get_posts_from_json() и при помощи цикла for проходим по полученным данным,
    сравнивая аргумент pk со значением по ключу 'pk'. При соответствии возвращаем данные о посте
    в виде словаря"""

    if pk <= 0:
        raise ValueError("Аргумент должен быть положительным числом больше 0")

    if type(pk) == str or type(pk) == float:
        raise TypeError("Аргумент должен быть целым числом")

    for post in get_posts_from_json():
        if post['pk'] == pk:
            return post
