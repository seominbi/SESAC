#계산기 만들기(calc.py)
#사용자로부터 연산모드 입력 -> 숫자를 두개 입력 받아서 결과 출력
#example)
# python calc.py
# 연산모드를 입력하시오 : plus / minus/ multiply / division
# 숫자1을 입력하시오:
# 숫자2를 입력하시오:
# 결과:
def plus(number1,number2):
    return number1+number2
def minus(number1,number2):
    return number1-number2
def multiply(number1,number2):
    return number1*number2
def division(number1,number2):
    try:
        result=number1/number2
    except ZeroDivisionError:
        print("0으로 나눗셈을 할 수 없습니다.")
        return "NaN"
    return number1/number2

mode=number1=number2=None

def inputNumbers():
    try:
        global number1
        number1=int(input("number1 : "))
        global number2
        number2=int(input("number2 : "))
    except ValueError:
        print("숫자가 아닌 값을 입력했습니다.")
        return True
    return False

def inputMode():
    global mode
    mode = input("연산모드 선택 ( plus / minus / multiply / division ): ")
    mode_options=["plus","minus","multiply","division"]

    if mode == "quit":
        exit(1)
    elif mode not in mode_options:
        print("알 수 없는 모드입니다.")
        return True
    
    return False

def operation(mode, number1, number2):
    if mode=="plus":
        result=plus(number1,number2)
    elif mode=="minus":
        result=minus(number1,number2)
    elif mode=="multiply":
        result=multiply(number1,number2)
    elif mode=="division":
        result=division(number1,number2)

    return result

#main, start point를 알리는 코드
if __name__=="__main__":
    while True:
        while inputMode():
            pass

        while inputNumbers():
            pass

        print("result : ",operation(mode, number1, number2))




#highscore.py
#사용자로부터 정수를 입력받는는다.
#사용자로부터 이름을 입력받는다.
#이 점수가 최고점수면 하이스코어를 기록한다.
#'high' 라고 입력하면 현재까지의 하이스코어와 그 사람이 누군지 출력한다.
#'history'라고 입력하면 그동안 입력한 모든 함수와 사람을 출력한다.
#----------------------------------
#global variable
#----------------------------------
HighScore=[] # item example : {"name": None,"score" : 0}
Historys=[] # item example : {"name": None,"score" : 0}

#----------------------------------
#function
#----------------------------------
def inputScore():
    while True:
        try:
            score = int(input("enter integer : "))
        except ValueError:
            continue
        break

    return score

def inputName():
    name = input("enter nickname : ")
    return name

def addHistory(name, score):
    dic={
        "name": name,
        "score" : score
    }
    Historys.append(dic)

def checkHighScore(name,score):
    dic={
        "name": name,
        "score" : score
    }

    '''
    max=Historys[0]
    for history in Historys:
        if history["score"]>=max["score"]:
            max=history
    
    if dic["score"]>max["score"]:
        HighScore.clear()
        HighScore.append(dic)
    elif dic["score"]==max["score"]:
        HighScore.append(dic)
    '''
    
    if HighScore != []:
        if dic["score"] > HighScore[0]["score"]:
            HighScore.clear()
            HighScore.append(dic)
        elif dic["score"]==HighScore[0]["score"]:
            HighScore.append(dic)
    else:
        HighScore.append(dic)

def printHighScore():
    print(HighScore)

def printHistorys():
    print(Historys)

#-------------------------------
#main function
#-------------------------------
if __name__=="__main__":
    for i in range(0,10):
        score=inputScore()
        name=inputName()
        addHistory(name,score)
        checkHighScore(name,score)
        printHighScore()
        
    printHistorys()


#------------------------------------------------
#file i/o
#------------------------------------------------
#mode : r=read, w=write, a=append
with open("file.txt","r") as file:   #read mode
    names=file.read() #file contents read
    print(names)

with open("file.txt","r") as file:   #read mode
    lines=file.readlines() #file contents read
    print(lines)


contents=[]
for line in lines:
    print(line)
    contents.append(line.strip())   #delete space

print(contents)

#------------------------------------------------

import os

filepath="./data/"
filename='myfile.txt'

os.mkdir(filepath)
...

data="hello, world"
with open(filepath+filename,"a") as file:
    file.write(data)
print("succes file write")

#------------------------------------------------

#csv file - comma seperated value, ','로 값을 구분하는 파일
#import 한글, 엑셀 등도 존재
import csv
data=[
    ("name","age","city"),
    ("john",25,"seoul"),
    ("bill",20,"busan"),
    ("kim",22,"seoul"),
]

with open("user.csv","w",newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
print("csv write done")

with open("user.csv","r",newline="") as file:
    csv_reader=csv.reader(file)
    for row in csv_reader:
        print(row)
print("csv read done")
#------------------------------------------------