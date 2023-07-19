from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버 실행, 크롬드라이버로 원하는 url로 접속
url = 'https://www.yes24.com/main/default.aspx'
driver = webdriver.Chrome() 
driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
# driver.implicitly_wait(10)

#step4.검색창에 키워드 입력 후 엔터
search_box=driver.find_element(By.CSS_SELECTOR, 'input.iptTxt.iptTxtAd')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

#step5.책 제목 읽기
# book_title=driver.find_element(By.CSS_SELECTOR,"a.gd_name")
# print(book_title.text)

book_titles=driver.find_elements(By.CSS_SELECTOR,"a.gd_name")
for e in book_titles:
    print(e.text)

#step6. 이미지 저장할 폴더 생성 및 저장
import os
path_folder = 'D:\Desktop\yes24'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

from urllib.request import urlretrieve
book_imgs=driver.find_elements(By.TAG_NAME,"img")
for e in book_imgs:
    href = e.get_attribute('src')
    if "goods" in href and "L":
        href_segment=href.split('/')
        filename=href_segment[4]
        urlretrieve(href, path_folder + "\\" + filename+".png")


#step5.이미지 읽기
# book_img=driver.find_element(By.TAG_NAME,"img")
# href = book_img.get_attribute('src')
# print(href)

#모든 윈도우 닫기 <-> driver.close()는 하나만 닫기
driver.quit()
print("download done.")

#step5.뉴스 탭 클릭
# driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
# time.sleep(2)