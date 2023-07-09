import csv
import math
from flask import Flask,url_for,redirect,render_template,request

from view.user import user_bp
from view.main import main_bp
from view.detail import detail_bp

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(user_bp)
app.register_blueprint(main_bp)
app.register_blueprint(detail_bp)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

