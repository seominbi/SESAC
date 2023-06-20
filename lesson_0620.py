#step1) 원하는 글자 세기
#step2) 대소문자를 구분하지 않고 글자 세기
sentence="HeLlO, world!"

def count_char(char):
    cnt=0
    for text in sentence:
        if text.upper()==char.upper():
            cnt+=1
    
    return cnt

c='l'
count=count_char(c)
print(f"글자 {c} 갯수 : {count}")


#0619 hw1 select user function review
users = [
    {"name": "Alice", "age": 35, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Anna", "age": 35, "location": "Jejiu", "car": "BMW"}
]

def matches_criteria(user,condition):
	for key,value in condition.items():
		if user.get(key) != value:
			return False
	return True

def find_user(search_user):
	result=[]
	for user in users:
		if matches_criteria(user,search_user):
			result.append(user)
	return result

#print(find_user(search_user))

#우리가 구현한 하나의 함수를 구동하며, 이 다섯개의 테스트 케이스를 실행한다.
#모두다 올바른 결과값이가 나오면 'pass', 하나라도 실패하면 'fail'을 출력한다.
search_bob1={"name":"Bob"}
search_bob2={"age":30}
search_bob3={"name":"Bob","age":30}
search_bob4={"name":"Bob","age":31}
search_bob5={}

test_cases = [
	{"name":"Bob"},
    {"age":30},
    {"name":"Bob","age":30},
    {"name":"Bob","age":31},
    {}
]
test_results=[1,1,1,0,4]


def test_find_users():
    print(len(find_user(search_bob1)))
    print(len(find_user(search_bob2)))
    print(len(find_user(search_bob3)))
    print(len(find_user(search_bob4)))
    print(len(find_user(search_bob5)))

    #make Dic Key and compare with value
    idx=0
    for case in test_cases:
        case["expection"]=test_results[idx]
        idx+=1
        print(case)
	
        if len(find_user(case)) != case["expection"]:
            print("fail")
            return
    print("pass")

    #compare test case list with test result list
    for i in range(0,len(test_cases)):
        if len(find_user(test_cases[i]))!=test_results[i]:
            print("fail")
            return
    print("pass")

    #enumerate()
    # for index,value in enumerate(test_cases):
    #     if len(find_user(test_cases[index]))!=test_results[index]:
    #         print("fail")
    #         return
    # print("pass")

test_find_users()


#0619 hw3 calender review
import datetime
import math
import random

#module datetime
current_time=datetime.datetime.now #module.class.function
print("현재시간: ",current_time)
specific_time=datetime.datetime(2023,6,20,10,30,00)
print("내가 만든 날짜 : ",specific_time)

#module math
radius=5
area=math.pi * (radius**2) #pi * r제곱
area=math.pi * math.pow(radius,2) #pi * r제곱
print("circle's area : ", area)

#module random
def roll_dice():
    random_number=random.randint(1,6) #range(1,6+1)
    return random_number

for _ in range(0,10):
    print("dice number : ",roll_dice(),end=', ')
print("\n")

#my_list를 무작위로 섞기
my_list=[1,2,3,4,5]
def shuffle():
    new_list=[]
    my_list_capacity=len(my_list)
    for i in range(0, my_list_capacity):
        pick=random.randint(0,my_list_capacity-i-1)
        new_list.append(my_list[pick])
        my_list.remove(my_list[pick])
    return new_list
print("origin list : ", my_list)
print("mixed list : ", shuffle())
print("my_list : ", my_list)
random.shuffle(my_list)
print("shuffle() my_list : ", my_list)
# a = random.sample(range(0,4),5) # 1부터 n까지의 범위중에 k개를 중복없이 뽑겠다.
# print(a)

#----------------------------------------------------------
#module os
import os

#get Current Working Directory
current_dir=os.getcwd() 
print(current_dir)

#Make Directory
new_dir="sesac1234"
os.mkdir(new_dir)   

#Make Dir sesac0,1,2,3,...
for i in range(0,10):
    new_dir_name="sesac"+str(i)
    os.mkdir(new_dir_name)

#Remove Dir(can't remove dir when the file exists in dir)
path="sesac1234"
os.rmdir(path)

path=os.getenv("PATH")
print("윈도우 내부의 환경변수(PATH) 값 출력 : ",path)

#open 파일탐색기 & 계산기
my_commands=["explorer","calc"]
for com in my_commands:
    os.system(com)


#웹에 있는 contents(정보)를 가져오는 모듈
#module requests (외부모듈), 추가 패키지 설치 필요
#pip install / conda install


#가상환경 sesac에 패키지 설치하기
#conda activate sesac
#pip install requests
#pip install requests==2.0.0

#pip 삭제
#pip uninstall requests

#module request
import requests
#네이버 페이지 요청 (GET)
response=requests.get('https://movie.daum.net/main')
print(response)
print(response.status_code)
print(response.url)
print(response.headers)
print(response.text)
print(response.text.find('</h2>'))

contents=response.text
for content in contents.splitlines():
    if "</h2>" in content:
        print(content.strip())



numbers=[1,2,3,4,5]

value=numbers[0]


#------------------------------------------------------------------------

#exception, 예외처리
def get_number(index):
    try:
        #오류 발생 가능성이 있는 코드 블럭
        if (index<len(numbers)):
            return numbers[index]
    except IndexError:
        #오류에 대한 처리 방법
        print("[error]입력값에 대한 인덱스 번호가 잘못되었습니다.")
    except TypeError:
        #오류에 대한 처리 방법
        print("[error]입력값의 유형이 잘못되었습니다.")

print(get_number(0))
print(get_number(5))
print(get_number(4))
print(get_number('a'))

#step1) 입력받은 글자를 숫자로 변환해서 +1을 더해 반환하시오.
#step2) 사용자로부터 입력받아 .. input()
#팁) try 안에는 return 문이 들어있으면 좋지 않다!
def convert_to_integer(string):
    try:
        value=(int(string)+1)
    except: #ValueError
        value="[error] 변환 불가능한 입력값입니다."
    
    return value

print(convert_to_integer("10"))
print(convert_to_integer("-5"))
print(convert_to_integer("a"))

string = input("enter string : ")
print(convert_to_integer(string))