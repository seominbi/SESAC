from flask import Blueprint,Flask,url_for,redirect,render_template,request
import csv

from view.db import crm_database_excutor

detail_bp = Blueprint('detail', __name__)

crm_db=crm_database_excutor()
print("detail.py : ", crm_db)

@detail_bp.route('/<category>/<id>')
def details(category,id):
    details=[]
    options=[]

    if category=="user":
        # print("user/id/details access success")
        html_file="user_details.html"
        # with open("./database/user.csv","r",newline="", encoding='utf-8') as user_file:
        #     user_reader=csv.reader(user_file)
        #     headers=next(user_reader)
        #     for row in user_reader:
        #         if row[0]==id:
        #             details.append(row)
        #             break
        
        crm_db.cursor.execute("""
            select name,gender,age,birthdate,address
            from "user"
            where user.id = ?
        """,(id,))
        headers=["Name","Gender","Age","Birthdate","Address"]
        details=crm_db.cursor.fetchall()

        crm_db.cursor.execute("""
            select o.id, o.orderAt, o.storeId
            from 'order' o 
            where o.userId = ?
        """,(id,))

        options.append(('orderId','purchaseDate','purchasedLocation'))

        result=crm_db.cursor.fetchall()
        for row in result:
            options.append(row)
        
    elif category=="order":
        # print("order/id/details access success")
        html_file="order_details.html"
        # with open("./database/order.csv","r",newline="", encoding='utf-8') as order_file:
        #     order_reader=csv.reader(order_file)
        #     headers=next(order_reader)
        #     for row in order_reader:
        #         if row[0]==id:
        #             details.append(row)
        #             break

        crm_db.cursor.execute("""
            select oi.id, oi.orderId, oi.itemId, i.name AS itemName
            from "orderitem" oi
            join item i ON oi.itemId = i.id
            where oi.orderId = ?
        """,(id,))
        headers=["id","orderId","itemId","itemName"]
        details=crm_db.cursor.fetchall()
        print(details)

    elif category=="orderitem":
        # print("orderitem/id/details access success")
        html_file="orderitem_details.html"
        # with open("./database/orderitem.csv","r",newline="", encoding='utf-8') as order_file:
        #     order_reader=csv.reader(order_file)
        #     headers=next(order_reader)
        #     for row in order_reader:
        #         if row[1]==id or row[2]==id:
        #             details.append(row)
        #             break
        crm_db.cursor.execute("""
            select o.id, o.orderAt, o.storeId, o.userId
            from "order" o
            where o.id = ?
        """,(id,))
        headers=["id","orderAt","storeId","userId"]
        details=crm_db.cursor.fetchall()
        print(details)
            
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

        crm_db.cursor.execute("""
            select i.name, i.unitPrice
            from item i
            where i.id = ?
        """,(id,))
        headers=["Name","unitPrice"]
        details=crm_db.cursor.fetchall()

        crm_db.cursor.execute("""
            select strftime('%Y-%m',"order".orderat) as month, sum(item.unitprice), count(*)
            from item, orderitem, "order"
            where item.id = ? and orderitem.itemId = item.id and orderitem.orderid="order".id
            group by month
        """,(id,))
        options.append(('Month','TotalRevenue','ItemCount'))
        result=crm_db.cursor.fetchall()
        for row in result:
            options.append(row)

    elif category=="store":
        # print("store/id/details access success")
        html_file="store_details.html"
        # with open("./database/store.csv","r",newline="", encoding='utf-8') as order_file:
        #     order_reader=csv.reader(order_file)
        #     headers=next(order_reader)
        #     for row in order_reader:
        #         if row[0]==id:
        #             details.append(row)
        #             break
        
        crm_db.cursor.execute("""
            select Name,Type,Address
            from "store"
            where store.id = ?
        """,(id,))
        headers=["Name","Type","Address"]
        details=crm_db.cursor.fetchall()

        crm_db.cursor.execute("""
            select strftime('%Y-%m',"order".orderat) as month, sum(item.unitprice), count(*)
            from "order", store, orderitem, item
            where "order".storeid = ? and "order".id = orderitem.orderid and orderitem.itemid=item.id
            group by month
        """,(id,))

        options.append(('Month','Revenue','Count'))
        result=crm_db.cursor.fetchall()
        for row in result:
            options.append(row)
    
    return render_template(html_file,details=details,options=options,headers=headers,key=id)
