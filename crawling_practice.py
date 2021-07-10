from typing import Text
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time
import pandas as pd
import re

driver = webdriver.Chrome('c:/driver/chromedriver.exe')
url = "https://playboard.co" 
driver.get(url)

driver.implicitly_wait(5)

superchat = driver.find_element_by_link_text("슈퍼챗 순위")
superchat.click()
time.sleep(2)
driver.implicitly_wait(2)




try:
    

    print("크롤링 시작")
    

    soup = BeautifulSoup(driver.page_source, "lxml" )


    boxItems = soup.select("#app > div.__window > div > main > div > div.container.container--mfit > table > tbody > .chart__row")
    # boxItems = soup.select("#app > div.__window > div > main > div > div.container.container--mfit > table > tbody > .chart__row")

    # print(boxItems)
    

    for boxItem in boxItems:


        asd = boxItem.text       
        # asd = boxItem.select_one("td.name > a")
        # k = re.sub('<.*?>','',asd
        # print(k)
        if asd != "":
            rank = boxItem.find("div", {"class": "current"}).text
            print("슈퍼챗 순위 : " , rank)

            title = boxItem.find("a")['title']
            title = re.sub('유튜브 채널 분석 보고서','',title)
            print("채널명 : ",title)

            # title = boxItem.find("a > h3").text
            # print("채널명 : ",title)




            superchat = boxItem.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
            print("슈퍼챗 수입 : ", superchat)

            superchat_num = boxItem.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
            print("슈퍼챗 갯수 : ", superchat_num)

            tags = boxItem.find("ul")
            tags = str(tags)
            # p1 = re.compile('#\w+')
            # tags = p1.findall(tags)
            tags = re.findall('#\w+',tags)
            print("태그 목록 : ", tags)


            
            

        
    


except Exception as e:
    print("페이지 파싱 에러", e)
finally:
    time.sleep(3)
    driver.close()





