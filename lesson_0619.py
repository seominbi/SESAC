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

