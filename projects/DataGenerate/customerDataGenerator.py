# ver 3.0
# 생성하는 개수를 동적으로 입력받고, 원하는 출력 타입 (console, csv) 에 따라 결과물을 출력하시오.
# 이름을 한국 이름으로 (성/이름), 그리고 주소도 한국 도로명 주소 형태로 생성하시오.

import random
import datetime
import csv

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
            lines = file.readlines() #file contents read
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
    

class customerDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        self.firstName=["서","김","이","박","하","강","최","정","한","오"]   #성
        self.lastName=["민준","서준","도윤","예준","시우","하준","주원","지호", 
                       "서윤","서연","지우","하윤","민서","지유","채원","지민"]    #name
        
        self.cities=["강남구 논현동", "강남구 역삼동","강동구 명일동","관악구 신림동","관악구 봉천동",
                     "구로구 가리봉동","동작구 대방동","서대문구 신촌동","송파구 송파동","마포구 마포동"]

    def generate_name(self):
        firstName=random.choice(self.firstName)
        lastName=random.choice(self.lastName)
        return firstName+lastName
    
    def generate_address(self):
        buildingNumber=random.randint(1,99)
        return random.choice(self.cities)+" "+str(buildingNumber)
    
#---------------------------------------------------------------------
# main function
#---------------------------------------------------------------------
if __name__=="__main__":
    customerGenerator=customerDataGenerator()

    #read name.txt and save data
    filepath="./resource/"
    filename="name.txt"
    customerGenerator.read_file(customerGenerator.getNames(),filepath,filename)

    # read city.txt and save data
    # filepath="./resource/"
    # filename="city.txt"
    # customerGenerator.read_file(customerGenerator.getCities(),filepath,filename)


    #input number of user info
    number=customerGenerator.input_number()
    customerGenerator.create_users_info(number)

    #select mode(console, csv)
    mode=customerGenerator.input_mode()
    customerGenerator.write_result(mode)

