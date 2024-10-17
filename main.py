# import requests
# from bs4 import BeautifulSoup
# import csv
# from selenium import webdriver


# # req = requests.Session()
# # response_uz = req.get('https://uzum.uz/') 
# # print(response_uz)
# # response_ru = requests.get('https://www.wildberries.ru/') 
# # explor = requests.get('https://youtube.com')

# dr = webdriver.Chrome()
# dr.get("https://uzum.uz/")
# bs = BeautifulSoup(dr.page_source,"html.parser")

# res = bs.find_all('a', class_="subtitle-item")
# # title = bs.select_one('div.subtitle')
# print(res)


# soup = BeautifulSoup(response_uz.content, 'html.parser') 
# get_items = soup.select_one('product-card-price-info')
# print(soup.text)
