import json


def get_posts_from_json():
    with open("data/posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_posts_all():
    return get_posts_from_json()


def get_posts_by_user(user_name):

    poster_names = []
    for post in get_posts_from_json():
        poster_names.append(post['poster_name'])

    if user_name in poster_names:
        posts_by_user_name = []
        for post in get_posts_all():
            if post['poster_name'] == user_name:
                posts_by_user_name.append(post)
        return posts_by_user_name

    raise ValueError("Пользователь не найден")


def get_comments_from_json():
    with open("data/comments.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_comments_by_post_id(post_id):

    existing_ids = []
    for comment in get_comments_from_json():
        existing_ids.append(comment['post_id'])

    if post_id in existing_ids:
        comments_by_post_id = []
        for comment in get_comments_from_json():
            if comment['post_id'] == post_id:
                comments_by_post_id.append(comment)
        return comments_by_post_id

    raise ValueError("Пост не найден")


def search_for_posts(word):
    posts_with_word = []
    for post in get_posts_from_json():
        if word.lower() in post['content'].lower():
            posts_with_word.append(post)
    return posts_with_word


def get_post_by_pk(pk):
    for post in get_posts_from_json():
        if post['pk'] == pk:
            return post

