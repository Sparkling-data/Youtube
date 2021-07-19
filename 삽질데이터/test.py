from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

def populcraw():
    main_url = "https://playboard.co/"

    driver = webdriver.Chrome("c:/driver/chromedriver.exe")

    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)

    superchat = driver.find_element_by_link_text("인기 순위")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
    print("-----스크롤 페이지 이동-----")

    # scroll 쭉 내리기, scroll 기다리는 시간 지정
    SCROLL_PAUSE_TIME = 0.7

    # Get scroll height : 브라우저의 높이를 찾아서 자바스크립트에 저장 후 last_height로 지정
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom : 브라우저 끝까지 스크롤을 내림
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
        # 스크롤 내려갈때까지 기다림
        time.sleep(SCROLL_PAUSE_TIME)
 
        # 스크롤이 끝까지 내려가면 break로 빠져나가고 아니면 while문 무한 반복
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("-----화면 제일 하단 스크롤 로딩 완료----")

    soup = BeautifulSoup(driver.page_source, "lxml" )

    # 정보박스 찾기
    boxitem = soup.select("tbody > .chart__row")
    # print(boxitem)
    print("-----스크롤 박스 찾기 완료-----")
    time.sleep(3)

    # 정보 가져오기
    try:
        # 광고는 text가 없어서 광고 없애려고 for문 씀
        for item in boxitem:
            noads = item.text

            if noads != "":

                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                views = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                like = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"})

                if like is None:
                    like = "-"
                else:
                    like = like.text

                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                
                print("No_{}".format(prolevel))
                print("채널명 = ", protitle)
                print("태그 = ", tag)
                print("일일 시청 수 = ", views)
                print("일일 좋아요 수= ", like)
                print("=" * 100)

    except Exception as e:
        print("페이지 파싱 에러", e)

    finally:
        time.sleep(3)
        print("크롤링을 종료합니다.")
        driver.close()

if __name__=='__main__':
    populcraw()
