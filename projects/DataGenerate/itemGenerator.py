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

    def write_result(self, mode):
        if mode=="console":
            for data in self.datas:
                print(data)
        elif mode=="csv":
            with open("user.csv","w",newline="",encoding = 'utf8') as file:
                for data in self.datas:
                    csv_writer=csv.writer(file)
                    csv_writer.writerow(data.values())

    @abstractmethod
    def create_datas(self,number):
        pass


class itemGenerator:
    def __init__(self):
        type = ""
        menu = ""
        price = ""

        def getType(self):
            return self.type

        def generate_uuid(self):
            item_id = str(uuid.uuid4())
            return user_id