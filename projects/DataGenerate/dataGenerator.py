import random
import datetime
import csv
import uuid
from abc import ABC, abstractmethod

class DataGenerator(ABC):
    def __init__(self):
        self.datas = []

    def getDatas(self):
        return self.datas

    def input_number(self):
        while True:
            try:
                number=int(input("input number : "))
            except ValueError:
                continue
            break
        return number

    def input_mode(self):
        while True:
            mode=input("input mode (console, csv) : ")
            if(mode!="console" and mode!="csv"):
                continue
            break
        return mode

    def read_file(self,obj,filepath,filename):
        with open(filepath+filename,"r",encoding='utf-8') as file:   #read mode
            lines=file.readlines() #file contents read
            for line in lines:
                obj.append(line.rstrip('\n'))   #delete '\n'

    def write_result(self, mode, filename):
        if mode=="console":
            for data in self.datas:
                print(data)
        elif mode=="csv":
            with open("database\\"+filename,"w",newline="",encoding = 'utf8') as file:
                for data in self.datas:
                    csv_writer=csv.writer(file)
                    csv_writer.writerow(data.values())

    @abstractmethod
    def create_datas(self,number):
        pass

# id, name, gender, age, birthdate, address 출력
class customerDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.names = [] #firstname[]+lastname[]
        self.cities=["강남구 논현동", "강남구 역삼동","강동구 명일동","관악구 신림동","관악구 봉천동",
                     "구로구 가리봉동","동작구 대방동","서대문구 신촌동","송파구 송파동","마포구 마포동"]

        self.firstName=["서","김","이","박","하","강","최","정","한","오"]   #성
        self.lastName=["민준","서준","도윤","예준","시우","하준","주원","지호", 
                       "서윤","서연","지우","하윤","민서","지유","채원","지민"]    #name
        
    def getNames(self):
        return self.names
    def getCities(self):
        return self.cities
    
    def generate_uuid(self):
        id = str(uuid.uuid4())
        return id
    
    def generate_name(self):
        firstName=random.choice(self.firstName)
        lastName=random.choice(self.lastName)
        return firstName+lastName
    
    def generate_gender(self):
        return random.choice(['Male','Female'])
    
    def generate_address(self):
        buildingNumber=random.randint(1,99)
        return random.choice(self.cities)+" "+str(buildingNumber)
    
    def generate_birthdate(self,start_date,end_date):
        # return a random datetime between two datetime objects.
        # ref) https://stackoverflow.com/questions/71440388/generate-random-date-in-iso-date-time-format-yyyy-mm-ddthhmmss-sssxxx
        delta = end_date - start_date     #return format : '%Y%m%d %I:%M %p'
        int_delta = (delta.days * 24 * 60 * 60)     #%Y%m%d를 seconds로 변환
        random_second = random.randrange(int_delta) #랜덤 날짜 생성
        birthdate=start_date + datetime.timedelta(seconds=random_second)
        return birthdate.strftime('%Y-%m-%d')   #랜덤 날짜 리턴

    def generate_age(self,birthdate):
        birth=datetime.datetime.strptime(birthdate,'%Y-%m-%d').date()
        today=datetime.datetime.now()
        age=today.year-birth.year
        return age
    
    def create_datas(self,number):
        for _ in range(number):
            id=self.generate_uuid()

            name = self.generate_name()

            gender=self.generate_gender()
            address=self.generate_address()
            
            now = datetime.datetime.now()
            now_date = now.strftime('%Y-%m-%d')
            start_date = datetime.datetime.strptime('1970-1-1', '%Y-%m-%d')
            end_date = datetime.datetime.strptime(now_date,'%Y-%m-%d')
            birthdate=self.generate_birthdate(start_date,end_date)
            age=self.generate_age(birthdate)

            customer={
                "id":id,
                "name":name,
                "gender":gender,
                "age":age,
                "birthdate":birthdate,
                "address":address
            }

            self.datas.append(customer)

# Id, Name, Type, Address 출력
class storeDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.names = []     #type.txt에서 가게 타입 읽어서 저장
        self.cities = []    #도로명 주소.txt 읽어서 저장

        self.location=["홍대","신촌","송파","잠실","강서","신림"]
        self.type=""

    def getNames(self):
        return self.names
    def getCities(self):
        return self.cities
    def getType(self):
        return self.type

    def generate_uuid(self):
        id = str(uuid.uuid4())
        return id

    def generate_name(self):
        self.type=random.choice(self.names)
        point=random.choice(self.location)+str(random.randint(1,10))+"호점"
        return self.type+' '+point
    
    def generate_address(self):
        buildingNumber=random.randint(1,99)
        city=random.choice(self.cities)
        return city+" "+str(buildingNumber)
    
    def create_datas(self,number):
        for _ in range(number):
            id=self.generate_uuid()

            name = self.generate_name()

            address=self.generate_address()
            type=self.getType()
            
            store={
                "id":id,
                "name":name,
                "type":type,
                "address":address
            }

            self.datas.append(store)


# Id, Name, Type, UnitPrice 출력
class itemDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.items = {
            "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }

    def generate_uuid(self):
        id = str(uuid.uuid4())
        return id

    def create_datas(self,number):
        for _ in range(number):
            id=self.generate_uuid()

            type = random.choice(list(self.items))
            # print(type)
            name=random.choice(list(self.items[type].keys()))
            # print(name)
            price=self.items[type][name]
            # print(price)
            
            item={
                "id":id,
                "type":type,
                "name":name+' '+type,
                "unitPrice":price
            }

            self.datas.append(item)
            # print(item)



# id, orderAt, storeId, userId
class orderDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.storeIds=[]
        self.userIds=[]
    
    def generate_uuid(self):
        id = str(uuid.uuid4())
        return id
    
    def generate_orderAt(self,start_date,end_date):
        # return a random datetime between two datetime objects.
        # ref) https://stackoverflow.com/questions/71440388/generate-random-date-in-iso-date-time-format-yyyy-mm-ddthhmmss-sssxxx
        delta = end_date - start_date     #return format : '%Y%m%d %I:%M %p'
        int_delta = (delta.days * 24 * 60 * 60)     #%Y%m%d를 seconds로 변환
        random_second = random.randrange(int_delta) #랜덤 날짜 생성
        birthdate=start_date + datetime.timedelta(seconds=random_second)
        return birthdate.strftime('%Y-%m-%d')   #랜덤 날짜 리턴
    
    def generate_storeIds(self):
        with open("database\\store.csv","r",newline="", encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                self.storeIds.append(row[0])
    
    def generate_userIds(self):
        with open("database\\user.csv","r",newline="", encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                self.userIds.append(row[0])
    
    def create_datas(self,number):
        self.generate_storeIds()
        self.generate_userIds()

        for _ in range(number):
            id=self.generate_uuid()

            now = datetime.datetime.now()
            now_date = now.strftime('%Y-%m-%d')
            start_date = datetime.datetime.strptime('2023-1-1', '%Y-%m-%d')
            end_date = datetime.datetime.strptime(now_date,'%Y-%m-%d')
            orderdate = self.generate_orderAt(start_date,end_date)

            storeid=random.choice(self.storeIds)
            userid=random.choice(self.userIds)

            order={
                "id":id,
                "orderAt":orderdate,
                "storeId":storeid,
                "userId":userid
            }

            self.datas.append(order)
            print(order)


# id, orderAt, storeId, userId
class orderitemDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.orderIds=[]
        self.itemIds=[]
    
    def generate_uuid(self):
        id = str(uuid.uuid4())
        return id
    
    def generate_orderIds(self):
        with open("database\\order.csv","r",newline="", encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                self.orderIds.append(row[0])
    
    def generate_itemIds(self):
        with open("database\\item.csv","r",newline="", encoding='utf-8') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                self.itemIds.append(row[0])
    
    def create_datas(self,number):
        self.generate_orderIds()
        self.generate_itemIds()

        for _ in range(number):
            id=self.generate_uuid()

            orderid=random.choice(self.orderIds)
            itemid=random.choice(self.itemIds)

            orderitem={
                "id":id,
                "orderId":orderid,
                "itemId":itemid
            }

            self.datas.append(orderitem)

#---------------------------------------------------------------------
# main function
#---------------------------------------------------------------------
if __name__=="__main__":
    select=input("user? store? item? order? orderitem? ")
    if(select=="user"):

        print(">>>>>customer datas<<<<<<")

        #generate CustomerData
        customerGenerator=customerDataGenerator()

        #read name.txt and save data
        filepath="./resource/"
        filename="name.txt"
        customerGenerator.read_file(customerGenerator.getNames(),filepath,filename)

        #input number of data
        #create datas
        number=customerGenerator.input_number()
        customerGenerator.create_datas(number)

        #select mode(console, csv)
        #print result
        mode=customerGenerator.input_mode()
        customerGenerator.write_result(mode,"user.csv")
    

    #---------------------------------------------------------------------
    elif(select=="store"):

        print(">>>>>store datas<<<<<<")

        #generate StoreData
        storeGenerator=storeDataGenerator()

        #read type.txt and save data
        filepath="./resource/"
        filename="type.txt"
        storeGenerator.read_file(storeGenerator.getNames(),filepath,filename)

        #read doroname.txt and save data
        filepath="./resource/"
        filename="doroname.txt"
        storeGenerator.read_file(storeGenerator.getCities(),filepath,filename)

        #input number of data
        number=storeGenerator.input_number()
        storeGenerator.create_datas(number)

        #select mode(console, csv)
        mode=storeGenerator.input_mode()
        storeGenerator.write_result(mode,"store.csv")
        

    #---------------------------------------------------------------------
    elif(select=="item"):

        print(">>>>>item datas<<<<<<")

        #generate itemData
        itemGenerator=itemDataGenerator()

        #input number of data
        number=itemGenerator.input_number()
        itemGenerator.create_datas(number)

        #select mode(console, csv)
        mode=itemGenerator.input_mode()
        itemGenerator.write_result(mode,"item.csv")
    

    #---------------------------------------------------------------------
    elif(select=="order"):

        print(">>>>>order datas<<<<<<")

        #generate orderData
        orderGenerator=orderDataGenerator()

        #input number of data
        number=orderGenerator.input_number()
        orderGenerator.create_datas(number)

        #select mode(console, csv)
        mode=orderGenerator.input_mode()
        orderGenerator.write_result(mode,"order.csv")
    

    #---------------------------------------------------------------------
    elif(select=="orderitem"):

        print(">>>>>orderitem datas<<<<<<")

        #generate orderData
        orderitemGenerator=orderitemDataGenerator()

        #input number of data
        number=orderitemGenerator.input_number()
        orderitemGenerator.create_datas(number)

        #select mode(console, csv)
        mode=orderitemGenerator.input_mode()
        orderitemGenerator.write_result(mode,"orderitem.csv")
