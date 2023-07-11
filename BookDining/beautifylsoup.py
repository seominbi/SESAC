import requests
from bs4 import BeautifulSoup as bs

url='https://www.yes24.com/Product/Search?domain=ALL&query='
search="do it!"
response=requests.get(url+search)
html_text = response.text

html=bs(html_text,'html.parser')

#제목
# values=html.find_all('htmlTag')
values=html.select('a.gd_name')
for value in values:
    title = value.get_text()
    print(title)
