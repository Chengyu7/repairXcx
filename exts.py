import os

from flask_sqlalchemy import SQLAlchemy

# 此时先不传入app
db = SQLAlchemy()

# 项目根目录
basedir = os.path.abspath(os.path.dirname(__file__))

appId = "wx9006526749674695"

appSecret = "9deb198137c5bbe9637c655a8a7a3eab"



