from flask import Blueprint,Flask,url_for,redirect,render_template,request
import csv
import math

from view.db import crm_database_excutor

main_bp = Blueprint('main', __name__)

crm_db=crm_database_excutor()
print("main.py : ", crm_db)

@main_bp.route('/order')
def order():
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    # with open('database/order.csv','r',encoding='utf-8') as file:
    #         csv_reader=csv.reader(file)
    #         headers=next(csv_reader)
    #         for row in csv_reader:
    #             datas.append(row)

    crm_db.cursor.execute("""
        select id, orderat, storeId, userId
        from "order"
    """)
    headers=["Id","orderAt","storeId","userId"]
    datas=crm_db.cursor.fetchall()

    total_page=math.ceil(len(datas)/per_page)
    start_index=(page-1)*per_page
    end_index=page*per_page

    page_datas=datas[start_index:end_index]

    #paging
    page_size=5
    pages=[p for p in range(0,total_page)]
    pages=[pages[s:s+page_size] for s in range(0, len(pages), page_size)]
    pages_index=request.args.get('pages_index',default=0,type=int)
    last_pages_index=max(len(pages)-1,0)
    
    return render_template("order.html",datas=datas, total_page=total_page,page_datas=page_datas,page=page,headers=headers,pages=pages[pages_index],pages_index=pages_index, last_pages_index=last_pages_index)

@main_bp.route('/orderitem')
def orderitem():    
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    # with open('database/orderitem.csv','r',encoding='utf-8') as file:
    #         csv_reader=csv.reader(file)
    #         headers=next(csv_reader)
    #         for row in csv_reader:
    #             datas.append(row)

    crm_db.cursor.execute("""
        select id, orderId, itemId
        from "orderitem"
    """)
    headers=["Id","orderId","itemId"]
    datas=crm_db.cursor.fetchall()

    total_page=math.ceil(len(datas)/per_page)
    start_index=(page-1)*per_page
    end_index=page*per_page

    page_datas=datas[start_index:end_index]

    #paging
    page_size=5
    pages=[p for p in range(0,total_page)]
    pages=[pages[s:s+page_size] for s in range(0, len(pages), page_size)]
    pages_index=request.args.get('pages_index',default=0,type=int)
    last_pages_index=max(len(pages)-1,0)
    
    return render_template("orderitem.html",datas=datas, total_page=total_page,page_datas=page_datas,page=page,headers=headers,pages=pages[pages_index],pages_index=pages_index, last_pages_index=last_pages_index)


@main_bp.route('/item')
def item():    
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    # with open('database/item.csv','r',encoding='utf-8') as file:
    #         csv_reader=csv.reader(file)
    #         headers=next(csv_reader)
    #         for row in csv_reader:
    #             datas.append(row)

    crm_db.cursor.execute("""
        select id, name, type, unitPrice
        from "item"
    """)
    headers=["Id","Name","Type","unitPrice"]
    datas=crm_db.cursor.fetchall()

    total_page=math.ceil(len(datas)/per_page)
    start_index=(page-1)*per_page
    end_index=page*per_page

    page_datas=datas[start_index:end_index]

    #paging
    page_size=5
    pages=[p for p in range(0,total_page)]
    pages=[pages[s:s+page_size] for s in range(0, len(pages), page_size)]
    pages_index=request.args.get('pages_index',default=0,type=int)
    last_pages_index=max(len(pages)-1,0)
    
    return render_template("item.html",datas=datas, total_page=total_page,page_datas=page_datas,page=page,headers=headers,pages=pages[pages_index],pages_index=pages_index, last_pages_index=last_pages_index)

@main_bp.route('/store')
def store():    
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    # with open('database/store.csv','r',encoding='utf-8') as file:
    #         csv_reader=csv.reader(file)
    #         headers=next(csv_reader)
    #         for row in csv_reader:
    #             datas.append(row)
    # Id,Name,Type, Address
    crm_db.cursor.execute("""
        select id, name, type, Address
        from "store"
    """)
    headers=["Id","Name","Type","Address"]
    datas=crm_db.cursor.fetchall()

    total_page=math.ceil(len(datas)/per_page)
    start_index=(page-1)*per_page
    end_index=page*per_page

    page_datas=datas[start_index:end_index]

    #paging
    page_size=5
    pages=[p for p in range(0,total_page)]
    pages=[pages[s:s+page_size] for s in range(0, len(pages), page_size)]
    pages_index=request.args.get('pages_index',default=0,type=int)
    last_pages_index=max(len(pages)-1,0)
    
    return render_template("store.html",datas=datas, total_page=total_page,page_datas=page_datas,page=page,headers=headers,pages=pages[pages_index],pages_index=pages_index, last_pages_index=last_pages_index)
