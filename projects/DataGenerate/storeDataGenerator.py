# ver 1.0
# 새로운 타입인 상점(store) 데이터를 생성하시오. (독립적인 코드로 구성)
# 상점의 이름, 타입(커피샵 유형), 주소를 생성하시오.

import random
import datetime
import csv
import uuid

class DataGenerator:
    def __init__(self):
        self.names = []
        self.cities = []
        self.datas = []
    
    def getNames(self):
        return self.names
    def getCities(self):
        return self.cities
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

    def generate_name(self):
        return random.choice(self.names)

    def generate_gender(self):
        return random.choice(['Male','Female'])

    def generate_birthdate(self,start_date,end_date):
        # return a random datetime between two datetime objects.
        # ref) https://stackoverflow.com/questions/71440388/generate-random-date-in-iso-date-time-format-yyyy-mm-ddthhmmss-sssxxx
        delta = end_date - start_date     #return format : '%Y%m%d %I:%M %p'
        int_delta = (delta.days * 24 * 60 * 60)     #%Y%m%d를 seconds로 변환
        random_second = random.randrange(int_delta) #랜덤 날짜 생성
        birthdate=start_date + datetime.timedelta(seconds=random_second)
        return birthdate.strftime('%Y-%m-%d')   #랜덤 날짜 리턴

    def generate_address(self):
        return str(random.randint(1,99))+' '+random.choice(self.cities)

    def generate_age(self,birthdate):
        birth=datetime.datetime.strptime(birthdate,'%Y-%m-%d').date()
        today=datetime.datetime.now()
        age=today.year-birth.year
        return age


    def write_result(self, mode):
        if mode=="console":
            for data in self.datas:
                print(data)
        elif mode=="csv":
            with open("user.csv","w",newline="",encoding = 'utf8') as file:
                for data in self.datas:
                    csv_writer=csv.writer(file)
                    csv_writer.writerow(data.values())

    def create_users_info(self,number):
        for _ in range(number):
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
                "name":name,
                "gender":gender,
                "birthdate":birthdate,
                "address":address,
                "age":age
            }

            self.datas.append(customer)
    

class storeDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.location=["홍대","신촌","송파","잠실","강서","신림"]
        self.type=""

    def getType(self):
        return self.type

    def generate_uuid(self):
        user_id = str(uuid.uuid4())
        return user_id

    def generate_name(self):
        self.type=random.choice(self.names)
        point=random.choice(self.location)+str(random.randint(1,10))+"호점"
        return self.type+' '+point
    
    def generate_address(self):
        buildingNumber=random.randint(1,99)
        city=random.choice(self.cities)
        return city+" "+str(buildingNumber)
    
    def create_users_info(self,number):
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


#---------------------------------------------------------------------
# main function
#---------------------------------------------------------------------
if __name__=="__main__":
    storeGenerator=storeDataGenerator()

    #read type.txt and save data
    filepath="./resource/"
    filename="type.txt"
    storeGenerator.read_file(storeGenerator.getNames(),filepath,filename)

    #read doroname.txt and save data
    filepath="./resource/"
    filename="doroname.txt"
    storeGenerator.read_file(storeGenerator.getCities(),filepath,filename)


    #input number of user info
    number=storeGenerator.input_number()
    storeGenerator.create_users_info(number)

    #select mode(console, csv)
    mode=storeGenerator.input_mode()
    storeGenerator.write_result(mode)


