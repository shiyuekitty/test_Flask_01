# coding:utf-8

from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp=make_response("success")
    resp.set_cookie("itcast","Pyhton")
    resp.set_cookie("itcast1","Pyhton1")
    resp.set_cookie("Itcast2", "Python1", max_age=3600)
    resp.headers["Set-Cookie"] = "Itcast3=Python3; Expires=Sat, 18-Nov-2017 04:36:04 GMT; Max-Age=3600; Path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    c=request.cookies.get("itcast")
    return c

@app.route("/delete_cookie")
def delete_cookie():
    resp=make_response("del success")
    resp.delete_cookie("itcast1")
    return resp

# if __name__ == '__main__':
    # app.run(debug=True)
