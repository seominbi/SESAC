from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import sqlite3

class database_excutor():
    def __init__(self):
        self.conn=sqlite3.connect('database/books.db',check_same_thread=False)
        self.cursor=self.conn.cursor()
    def create_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "books"(
            "isbn" text primary key)
                            
        """)
    def insert_data(self, isbn):
        self.cursor.execute("INSERT INTO books(isbn) VALUES (?)", (isbn,))
        self.conn.commit()
    def print_databse(self):
        self.cursor.execute("""
            select *
            from books
        """)
        print(self.cursor.fetchall())

# query = input('검색할 키워드를 입력하세요: ')
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path= ChromeDriverManager().install())


driver = webdriver.Chrome(service = service, options=chrome_options) 
# url = 'https://www.yes24.com/main/default.aspx'
url = 'https://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=07'
driver.get(url)

driver.implicitly_wait(5)

# driver.find_element(By.CSS_SELECTOR, "#yesFixCorner > dl > dd > ul.yesCornerLi > li:nth-child(1) > a").click()
# driver.implicitly_wait(5)

# driver.find_element(By.CSS_SELECTOR, '#day > a').send_keys('\n')
# print("일별 베스트셀러 클릭")
# driver.implicitly_wait(5)

books=database_excutor()
books.create_database()

book_images = driver.find_elements(By.CSS_SELECTOR, '#category_layout > tbody > tr > td.image > div > a:nth-child(1)')
print(f'book 개수 {len(book_images)}')
count = 1
for i in range(len(book_images)):
    book_images = driver.find_elements(By.CSS_SELECTOR, '#category_layout > tbody > tr > td.image > div > a:nth-child(1)')
    book_images[i].click()
    print(f'count: {count}')
    count+=1
    isbn_element = driver.find_element(By.CSS_SELECTOR,'meta[property="books:isbn"]')
    isbn=isbn_element.get_attribute("content")
    print(isbn)
    books.insert_data(isbn)
    driver.back()
    print("뒤로 가기 성공")
    driver.implicitly_wait(5)

books.print_databse()
print(f"book들 목록 가져옴! 개수:{len(book_images)}")



# description_element = driver.find_element_by_xpath('//meta[@name="description"]')
# description = description_element.get_attribute('content')
# print("Description:", description)

driver.close()