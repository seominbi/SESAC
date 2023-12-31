from flask import Blueprint,Flask,url_for,redirect,render_template,request
import csv

from view.db import crm_database_excutor

detail_bp = Blueprint('detail', __name__)

crm_db=crm_database_excutor()
print("detail.py : ", crm_db)

@detail_bp.route('/user/<id>')
def user_detail(id):
    details=[]
    options=[]

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
        
    return render_template(html_file,details=details,options=options,headers=headers,key=id)

@detail_bp.route('/order/<id>')
def order_detail(id):
    details=[]
    options=[]

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

    return render_template(html_file,details=details,options=options,headers=headers,key=id)

@detail_bp.route('/orderitem/<id>')
def orderitem_detail(id):
    details=[]
    options=[]

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
    return render_template(html_file,details=details,options=options,headers=headers,key=id)

@detail_bp.route('/item/<id>')
def item_detail(id):
    details=[]
    options=[]

    # print("item/id/details access success")
    html_file="item_details.html"
    # with open("./database/item.csv","r",newline="", encoding='utf-8') as order_file:
    #     order_reader=csv.reader(order_file)
    #     headers=next(order_reader)
    #     for row in order_reader:
    #         if row[0]==id:
    #             details.append(row)
    #             break

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

    return render_template(html_file,details=details,options=options,headers=headers,key=id)

@detail_bp.route('/store/<id>')
def store_detail(id):
    details=[]
    options=[]
    ranks=[]

    month=request.args.get('month')
    if month:
        print('if ',month)
        crm_db.cursor.execute("""
            select strftime('%Y-%m-%d',"order".orderat) as date, sum(item.unitprice), count(*)
            from "order", store, orderitem, item
            where "order".storeid = ? and "order".id = orderitem.orderid and orderitem.itemid=item.id and
                strftime('%Y-%m',"order".orderat) = ?
            group by date
        """,(id,month,))
        options.append(('Month','Revenue','Count'))
        result=crm_db.cursor.fetchall()
        for row in result:
            options.append(row)

        crm_db.cursor.execute("""
            select 'order'.userId, user.name, count(*) as frequency
            from "order"
            join user on 'order'.userId = user.id
            where "order".storeid = ? and strftime('%Y-%m',"order".orderat) = ?
            group by 'order'.userId
            order by frequency desc, name asc
            limit 10
        """,(id,month,))
        ranks.append(('userId','Name','Frequency'))
        result=crm_db.cursor.fetchall()
        for row in result:
            ranks.append(row)
    else:
        #None
        print('else ', month)
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

        crm_db.cursor.execute("""
            select 'order'.userId, user.name, count(*) as frequency
            from "order"
            join user on 'order'.userId = user.id
            where "order".storeid = ?
            group by 'order'.userId
            order by frequency desc, name asc
            limit 10
        """,(id,))
        ranks.append(('userId','Name','Frequency'))
        result=crm_db.cursor.fetchall()
        for row in result:
            ranks.append(row)

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


    
    return render_template(html_file,details=details,options=options,ranks=ranks,headers=headers,key=id,month=month)
