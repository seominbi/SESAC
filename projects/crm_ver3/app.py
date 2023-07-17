import csv
import math
from flask import Flask,url_for,redirect,render_template,request

from view.user import user_bp
from view.main import main_bp
from view.detail import detail_bp

from view.db import crm_database_excutor

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(user_bp)
app.register_blueprint(main_bp)
app.register_blueprint(detail_bp)

crm_db=crm_database_excutor()
crm_db.create_table()
crm_db.user_csv_to_db()
crm_db.item_csv_to_db()
crm_db.store_csv_to_db()
crm_db.order_csv_to_db()
crm_db.orderitem_csv_to_db()
print("app.py : ", crm_db)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

