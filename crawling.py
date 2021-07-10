from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
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
            prolevel = item.find("div", {"class":"current"}).text
            protitle = item.find("img")['alt']
            protag = item.find("ul", {"class":"name__tags ttags"})
            superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
            superchat_num = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text

            protag = str(protag)
            exp = re.compile('#\w+')
            protag = exp.findall(protag)

            print("No_{}".format(prolevel))
            print("채널명 = ", protitle)
            print("태그 = ", protag)
            print("슈퍼챗 수입 = ", superchat)
            print("슈퍼챗 개수 = ", superchat_num)
            print("=" * 100)


except Exception as e:
    print("페이지 파싱 에러", e)

finally:
    time.sleep(3)
    print("크롤링을 종료합니다.")
    driver.close()