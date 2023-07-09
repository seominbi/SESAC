from flask import Flask,url_for,redirect,render_template,request
import csv
import math

app=Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for("user"))

@app.route('/user')
def user():
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    
    datas=[]

    search_name=request.args.get("name")

    page=request.args.get('page',default=1,type=int)
    
    if search_name:
        with open('static/user.csv','r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            headers=next(csv_reader)
            for row in csv_reader:
                if search_name in row[1]:
                    datas.append(row)
    else:
        with open('static/user.csv','r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            headers=next(csv_reader)
            for row in csv_reader:
                datas.append(row)

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
    
    #검색결과가 없을 시 paging 에러 해결 !
    if page_datas:
        pages=pages[pages_index]
    else:
        pages=[0]
        
    return render_template("home.html",datas=datas, total_page=total_page,page_datas=page_datas,page=page,headers=headers,search_name=search_name,pages=pages,pages_index=pages_index, last_pages_index=last_pages_index)


@app.route('/<category>/<id>')
def details(category,id):
    details=[]

    if category=="user":
        # print("user/id/details access success")
        html_file="user_details.html"
        with open("./static/user.csv","r",newline="", encoding='utf-8') as user_file:
            user_reader=csv.reader(user_file)
            headers=next(user_reader)
            for row in user_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="order":
        # print("order/id/details access success")
        html_file="order_details.html"
        with open("./static/order.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="orderitem":
        # print("orderitem/id/details access success")
        html_file="orderitem_details.html"
        with open("./static/orderitem.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="item":
        # print("item/id/details access success")
        html_file="item_details.html"
        with open("./static/item.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    elif category=="store":
        # print("store/id/details access success")
        html_file="store_details.html"
        with open("./static/store.csv","r",newline="", encoding='utf-8') as order_file:
            order_reader=csv.reader(order_file)
            headers=next(order_reader)
            for row in order_reader:
                if row[0]==id:
                    details.append(row)
                    break
    
    return render_template(html_file,details=details,headers=headers)

@app.route('/order')
def order():
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    with open('static/order.csv','r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            headers=next(csv_reader)
            for row in csv_reader:
                datas.append(row)

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

@app.route('/orderitem')
def orderitem():    
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    with open('static/orderitem.csv','r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            headers=next(csv_reader)
            for row in csv_reader:
                datas.append(row)

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


@app.route('/item')
def item():    
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    with open('static/item.csv','r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            headers=next(csv_reader)
            for row in csv_reader:
                datas.append(row)

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

@app.route('/store')
def store():    
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1
    page=request.args.get('page',default=1,type=int)

    datas=[]

    with open('static/store.csv','r',encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            headers=next(csv_reader)
            for row in csv_reader:
                datas.append(row)

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


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)