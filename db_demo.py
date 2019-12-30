from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URL = "mysql://root:password@1ocalhost/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

db = SQLAlchemy(app)


# 继承数据库模型
class Role(db.Model):
    """用户身份表"""
    # 定义表名
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        return "<Role object:name=%s %s>" % (self.name,self.id)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email=db.Column(db.String(32),unique=True)
    password=db.Column(db.String(32))
    # 设置外检
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return "<User :%s %s %s %s>" %s(self.name,self.id,self.email,self.password)
@app.route('/')
def insex():
    return "hello world!"

if __name__ == '__main__':
    # 创建表
    # db.create_all()
    # #删除表
    # db.drop_all()
    app.run(debug=True)
