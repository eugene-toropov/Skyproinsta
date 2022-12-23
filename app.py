from flask import Flask, request, render_template, jsonify  # Импортируем необходимые библиотеки и модули
import utils
import logging

# Создаем логгер, устанавливаем уровень INFO, задаем обработчик, указываем файл для записей,
# Указываем кодировку, указываем формат записи.
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
logger_handler = logging.FileHandler('logs/api.log', encoding='utf-8')
logger_handler.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)


app = Flask(__name__)  # Регистрируем приложение
app.config['JSON_AS_ASCII'] = False  # Указываем параметр конфигурации для кодировки


@app.route('/')
def main_page():
    """Представление главной страницы по маршруту '/'.

    Внутри представления обращаемся к функции, которая
    возвращает список словарей. Полученные данные передаем в шаблон index.html"""
    items = utils.get_posts_all()
    return render_template("index.html", items=items)


@app.route('/posts/<int:post_pk>')
def post_page(post_pk):
    """Представление по маршруту '/posts/<int:post_pk>'

    Представление обращается к функции с аргументом, которая
    возвращает список. Создаем переменные и присваиваем им значения из
    полученных данных, далее все переменные передаем в шаблон 'post.html'"""

    post = utils.get_post_by_pk(post_pk)
    poster_name = post["poster_name"]
    poster_avatar = post["poster_avatar"]
    pic = post["pic"]
    content = post["content"]
    views_count = post["views_count"]
    pk = post["pk"]

    comments = utils.get_comments_by_post_id(post_pk)
    len_comments = len(comments)

    return render_template("post.html",
                           poster_name=poster_name,
                           poster_avatar=poster_avatar,
                           pic=pic,
                           content=content,
                           views_count=views_count,
                           pk=pk,
                           comments=comments,
                           len_comments=len_comments)


@app.route('/search')
def search_word():
    """Представление по маршруту /search

    Из запроса берем строку и присваиваем ее к переменной substr.
    Обращаемся к функции с аргументом substr, получаем список словарей.
    Ограничиваем его размер до 10. Задаем необходимые переменные и
    передаем в шаблон 'search.html'"""
    substr = request.args.get('s', '')
    data = utils.search_for_posts(substr)
    posts = data[:10]
    len_posts = len(posts)
    return render_template("search.html", posts=posts, len_posts=len_posts, substr=substr)


@app.route('/users/<user_name>')
def search_name(user_name):
    """Представление '/users/<user_name>'

    При помощи конструкции try/except обращаемся к функции с аргументом: <user_name>.
    Получаем список, задаем переменные и передаем данные в шаблон 'user-feed.html'.
    Если пользователя не окажется в списке - возвращаем соответствующее сообщение"""
    try:
        posts = utils.get_posts_by_user(user_name)
        username = user_name
        return render_template("user-feed.html", posts=posts, username=username)
    except ValueError:
        return "Пользователь не найден"


@app.route('/api/posts')
def api_all_posts():
    """API представление по маршруту '/api/posts'.

    Обращаемся к функции, получаем список словарей, используем функцию jsonify и
    возвращаем данные. При каждом обращении к маршруту вносим соответствующую запись в лог"""
    logger.info("Запрос /api/posts")
    data = utils.get_posts_from_json()
    return jsonify(data)


@app.route('/api/posts/<int:post_pk>')
def api_post(post_pk):
    """API представление по маршруту '/api/posts/<post_pk>'.

    Обращаемся к функции, получаем словарь, используем функцию jsonify и
    возвращаем данные. При каждом обращении к маршруту вносим соответствующую запись в лог"""
    logger.info(f"Запрос /api/posts/{post_pk}")
    data = utils.get_post_by_pk(post_pk)
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    """Обработчик запросов к несуществующим страницам.

    Возвращает ошибку и статус-код 404"""
    return e, 404


@app.errorhandler(500)
def page_not_found(e):
    """Обработчик ошибок со стороны сервера.

    Возвращает ошибку и статус-код 500"""
    return e, 500


if __name__ == "__main__":  # Условия для запуска приложения
    app.run()
