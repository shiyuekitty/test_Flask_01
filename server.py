from flask import Flask, request
import flask

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if flask.request.method == "GET":
        return flask.render_template("index.html")
    else:
        pass
        # name = flask.request.form.get("username")
        # password = flask.request.form.get("password")
        # print(name, password)


@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return flask.render_template("about.html")





@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)
