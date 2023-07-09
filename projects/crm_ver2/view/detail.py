from flask import Blueprint,Flask,url_for,redirect,render_template,request
import csv

detail_bp = Blueprint('detail', __name__)

@detail_bp.route('/<category>/<id>')
def details(category,id):
    details=[]

    if category=="user":
        # print("user/id/details access success")
        html_file="user_details.html"
        with open("./database/user.csv","r",newline="", encoding='utf-8') as user_file:
            user_reader=csv.reader(user_file)
            headers=next(user_reader)
            for row in user_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="order":
        # print("order/id/details access success")
        html_file="order_details.html"
        with open("./database/order.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="orderitem":
        # print("orderitem/id/details access success")
        html_file="orderitem_details.html"
        with open("./database/orderitem.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="item":
        # print("item/id/details access success")
        html_file="item_details.html"
        with open("./database/item.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="store":
        # print("store/id/details access success")
        html_file="store_details.html"
        with open("./database/store.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    
    return render_template(html_file,details=details,headers=headers)
