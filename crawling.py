# from _typeshed import NoneType
from selenium import webdriver
from bs4 import BeautifulSoup
import time
# from selenium.webdriver.support.ui import WebDriverWait

main_url = "https://playboard.co/"

driver = webdriver.Chrome("c:/driver/chromedriver.exe")

driver.get(main_url)
time.sleep(3)
driver.implicitly_wait(2)

superchat = driver.find_element_by_link_text("슈퍼챗 순위")
superchat.click()
time.sleep(3)
driver.implicitly_wait(2)
print("-----1-----")

soup = BeautifulSoup(driver.page_source, "lxml" )
print("-----2-----")

# 정보박스 찾기
boxitem = soup.select("tbody > .chart__row")
# print(boxitem)
print("-----3-----")

try:
    for item in boxitem:

        noads = item.text

        if noads != "":
            protitle = item.find("a")['title']
            # img_src = item.find("img")['data-src']

            print("채널명 = ", protitle)
            # print("태그 = ", protag)
            # print("순위 = ", prolevel)
            # print("슈퍼챗 수입 = ", proscore)
            # print("슈퍼챗 개수 = ", proJumsu)
            # print("썸네일=", img_src)
            print("=" * 100)

            time.sleep(5)
            driver.implicitly_wait(5)

except Exception as e:
    print("페이지 파싱 에러", e)

finally:
    time.sleep(3)
    print("크롤링을 종료합니다.")
    driver.close()