#tuple
def get_name_and_age():
    return "Seo",23

if __name__=="__main__":
    name,age=get_name_and_age()
    print(name)
    print(age)

#list
shopping_list=["apple","banana","orange"]
print(shopping_list)
shopping_list.append("graph") #add list item
print(shopping_list)
shopping_list.remove("banana") #remove list item
print(shopping_list)

#dictionary (key-value, "key":"value")
student={
    "name":"minb",
    "age":20,
    "university":"soongsil"
}
print("name : ", student["name"])
print("age : ", student["age"])
print("university : ", student["university"])

#----------------------
#if, elif
#input()

#--------------------
#example problems

#홀수리스트와 짝수 리스트를 만들어서 목록에 추가하시오.
numbers=[1,2,3,4,5]
even_numbers=[]
odd_numbers=[]
for num in numbers:
    if num %2==0:
        print(num,"is even")
        even_numbers.append(num)
    else:
        print(num,"is odd")
        odd_numbers.append(num)
print("even : ", even_numbers)
print("odd : ", odd_numbers)

#아래 목록에서 90점 이상인 학생을 출력하시오
student_grades={"john" : 85,"emily":92,"michael":78,"sophia":95}
for name, score in student_grades.items():
    if score>=90:
        print(f"{name} : {score}")

#----------------------------------------------------------------
#foriter
def nested_loop():
    n=100
    count=0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    count+=1
    return count

result=nested_loop()
print(result)

#리스트 컴프리헨션(list comprehension)
squares=[]
for x in range(1,11):
    squares.append(x ** 2) #add x제곱 into list
print(squares)

squares=[x ** 2 for x in range(1,11)] #add x제곱 into list
print(squares)

#리스트 컴프리헨션(list comprehension)으로 1부터 20까지의 짝수들로 리스트 생성하시오.
even_numbers=[]
#even_numbers=[y]
even_numbers=[y for y in range(1,21)]
even_numbers=[y for y in range(1,21) if y%2==0]
print(even_numbers)

#리스트 컴프리헨션(list comprehension)으로 문자열의 각 글자를 순회하면서 대문자로 바꾸시오.
word="hello"
upper_letters=[]
upper_letters=[c.upper() for c in word]
print(upper_letters)

#문자열 길이가 3이하인 단어들만 선택하기
words=["apple","banana","cherry","dragonfruit","egg"]
short_words=[]
short_words=[word for word in words if(len(word)<=3)]
print(short_words)

#STEP1) 이름을 입력 받아 사용자 정보(dictionary)를 반납하시오.
#STEP2) 이름과 나이 등을 입력 받아서 ....
users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

def find_users(target):
    result=[]
    for u in users:
        if u["name"]==target["name"] and u["age"]==target["age"]:
            result.append(u)
    return result

def enter_name():
    name = input("enter name : ")
    print(find_users(name))

#enter_name()

target={
    "name":"Bob",
    "age":30
}
print(find_users(target))


#STEP1)사용자로부터 문자(문장)을 입력받아 대문자로 변환하시오.
#STEP2)사용자로부터 문자(문장)에서 대문자는 소문자로, 소문자는 대문자로 변환하시오.
def conver_case(text):
    result=""
    for t in text:
        if t.isupper():
            result+=t.lower()
        else:
            result+=t.upper()
    return result

text=input("enter : ")
print(conver_case(text))


#입력받은 인자의 리스트 중에서 가장 큰 숫자를 반납하시오.
def find_max(numbers):
    max=numbers[0]
    for num in numbers:
        if num>max:
            max=num

    return max

numbers=[15,3,7,2,9,1,4,10]
print("max : ",find_max(numbers))



#리스트의 중복을 제거하시오.
numbers=[1,2,3,4,3,2,1,5,6,7,6,5]

def remove_duplicate(numbers):
    unique_list=[]
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list


unique_list=remove_duplicate(numbers)
print(numbers)
print(unique_list)

numbers=[1,2,3,4,3,2,1,5,6,7,6,5]
unique_list=set(numbers)
print(unique_list)

#공백으로 구분된 문자열을 입력받아서 max를 구하시오.
def find_max1(user_input):
    list=[]
    for cur in user_input.split():
        list.append(int(cur))
    return max(list)

def find_max2(user_input):
    list=[int(cur) for cur in user_input.split()]
    return max(list)

user_input=input("enter : ")
max_number=find_max2(user_input)
print(max_number)



#name, birthdate, gender, address 데이터 생성/출력/파일로 저장
#ex) jane, 1990-01-03, male, 50, new york

'''과제'''
#search_user={} 안에 있는 조건이 모두 매칭하는 사용자를 찾아내시오.
users = [
    {"name": "Alice", "age": 35, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Anna", "age": 35, "location": "Jejiu", "car": "BMW"}
]
search_user={"age" : 35, "car":"BMW"}
def find_user(search_user):
    keys=search_user.keys()
    result=[]
    for u in users:
        cnt=0
        for key in keys:
            if u[key]==search_user[key]:
                cnt+=1
        if len(keys)==cnt:
            result.append(u)

    return result

print(find_user(search_user))