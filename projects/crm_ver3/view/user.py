from flask import Blueprint,Flask,url_for,redirect,render_template,request
import csv
import math

from view.db import crm_database_excutor

user_bp = Blueprint('user', __name__)

crm_db=crm_database_excutor()
print("user.py : ", crm_db)

@user_bp.route('/')
def home():
    return redirect(url_for("user.user"))

@user_bp.route('/user')
def user():
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    
    datas=[]

    search_name=request.args.get("name")

    page=request.args.get('page',default=1,type=int)
    
    if search_name:
        # with open('./database/user.csv','r',encoding='utf-8') as file:
        #     csv_reader=csv.reader(file)
        #     headers=next(csv_reader)
        #     for row in csv_reader:
        #         if search_name in row[1]:
        #             datas.append(row)

        crm_db.cursor.execute("""
            select id, name,gender,age,birthdate
            from "user"
            where user.name like ?
        """,('%' + search_name + '%',))
        headers=["Id","Name","Gender","Age","Birthdate"]
        datas=crm_db.cursor.fetchall()
    else:
        # with open('./database/user.csv','r',encoding='utf-8') as file:
        #     csv_reader=csv.reader(file)
        #     headers=next(csv_reader)
        #     for row in csv_reader:
        #         datas.append(row)
        crm_db.cursor.execute("""
            select id, name,gender,age,birthdate
            from "user"
        """)
        headers=["Id","Name","Gender","Age","Birthdate"]
        datas=crm_db.cursor.fetchall()

    total_page=math.ceil(len(datas)/per_page)
    start_index=(page-1)*per_page
    end_index=page*per_page

    page_datas=datas[start_index:end_index]

    # paging
    page_size=5
    pages=[p for p in range(0,total_page)]
    pages=[pages[s:s+page_size] for s in range(0, len(pages), page_size)]
    pages_index=request.args.get('pages_index',default=0,type=int)
    last_pages_index=max(len(pages)-1,0)
    
    # 검색결과가 없을 시 paging 에러 해결 !
    if page_datas:
        pages=pages[pages_index]
    else:
        pages=[0]
        
    return render_template("home.html",datas=datas, total_page=total_page,page_datas=page_datas,page=page,headers=headers,search_name=search_name,pages=pages,pages_index=pages_index, last_pages_index=last_pages_index)
