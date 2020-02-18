from flask import Flask, request
import flask
from _cookie import set_cookie, delete_cookie, get_cookie

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        return flask.render_template("index.html")
    else:
        pass
        # name = flask.request.form.get("username")
        # password = flask.request.form.get("password")
        # print(name, password)


@app.route('/about', methods=["GET", "POST"])
def about():
    user_agent = request.headers.get('User-Agent')
    return flask.render_template("about.html")




@app.route('/register', methods=['GET', 'POST'])  # 解析post数据
def register():
    if request.method == 'GET':
        return flask.render_template('login.html')
    else:
        uname = request.form['username']
        email = request.form['email']
        uurl = request.form['url']
        upwd = request.form['password']
        # savetosql(uname, email, uurl, upwd)
        return flask.render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404


if __name__ == '__main__':
    app.add_url_rule(rule="/", endpoint="index")
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)
