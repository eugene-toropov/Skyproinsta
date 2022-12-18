from flask import Flask, request, render_template, send_from_directory
import utils

app = Flask(__name__)


@app.route('/')
def main_page():
    items = utils.get_posts_from_json()
    return render_template("index.html", items=items)


@app.route('/posts/<int:post_pk>')
def post_page(post_pk):

    post = utils.get_post_by_pk(post_pk)
    poster_name = post["poster_name"]
    poster_avatar = post["poster_avatar"]
    pic = post["pic"]
    content = post["content"]
    views_count = post["views_count"]

    comments = utils.get_comments_by_post_id(post_pk)
    len_comments = len(comments)

    return render_template("post.html",
                           poster_name=poster_name,
                           poster_avatar=poster_avatar,
                           pic=pic,
                           content=content,
                           views_count=views_count,
                           comments=comments,
                           len_comments=len_comments)


app.run()
