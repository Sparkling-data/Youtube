from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import schedule
# from selenium.webdriver.support.ui import WebDriverWait


def supercraw():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("슈퍼챗 순위")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
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
    soup = BeautifulSoup(driver.page_source, "lxml" )
    # 정보박스 찾기
    boxitem = soup.select("tbody > .chart__row")
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
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                superchat_num = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat, superchat_num]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        # pandas로 crawling data csv 저장
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '일일 슈퍼챗수입', '일일 슈퍼챗개수']
        df.to_csv('./savedata/supercraw.csv', index = False)
        
    

def supercraw_week():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("슈퍼챗 순위")
    superchat.click()
    driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
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
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat, superchat_num]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '주간 슈퍼챗수입', '주간 슈퍼챗개수']
        df.to_csv('./savedata/supercraw_week.csv', index = False)
        
    
def LiveRank():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("라이브 시청자 순위")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                LiveYoutube = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-none up"}).text
                
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag,LiveYoutube]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '최고 동시 시정자수']
        df.to_csv('./savedata/LiveRank.csv', index = False)
        
    
def LiveRank_week():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("라이브 시청자 순위")
    superchat.click()
    driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                LiveYoutube = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-none up"}).text
                
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag,LiveYoutube]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '주간 최고 동시 시청자수']
        df.to_csv('./savedata/LiveRank_week.csv', index = False)

        
    
def mostviewvideo():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("인기 순위")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    
    try:
        
        for item in boxitem:
            noads = item.text
            
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                views = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                Like = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"})
                

                if Like is None:
                    Like = "-"
                else:
                    Like = Like.text
                protag = str(protag)      
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, views, Like]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '일일조회수', '일일 좋아요 수']
        df.to_csv('./savedata/mostviewvideo.csv', index = False)
        # print("---------crawling file save 완료------------")
        
    
    
def mostviewvideo_week():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("인기 순위")
    superchat.click()
    driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    
    try:
        
        for item in boxitem:
            noads = item.text
            
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                views = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                Like = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"})
                
                if Like is None:
                    Like = "-"
                else:
                    Like = Like.text
                protag = str(protag)      
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, views, Like]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '주간 조회수', '주간 좋아요 수']
        df.to_csv('./savedata/mostviewvideo_week.csv', index = False)
def subsoaring():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("C:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("구독자 급상승 순위")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                superchat_num = item.find("td", {"class":"score"}).text

                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat, superchat_num]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '일일_신규구독자', '전체구독자']
        df.to_csv('./savedata/subsoaring.csv', index = False)
        
    
def subsoaring_week():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("C:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("구독자 급상승 순위")
    superchat.click()
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"name__tags ttags"})
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                superchat_num = item.find("td", {"class":"score"}).text
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat, superchat_num]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '주간_신규구독자', '전체구독자']
        df.to_csv('./savedata/subsoaring_week.csv', index = False)
    
def mostview():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("최다 조회 영상")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"title__tags ttags"})
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat]
                results.append(data)

    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '일일_조회수']
        df.to_csv('./savedata/mostview.csv', index = False)
        
    
def mostview_week():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("최다 조회 영상")
    superchat.click()
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"title__tags ttags"})
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '주간_조회수']
        df.to_csv('./savedata/mostview_week.csv', index = False)
        
    
def mostviewad():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("최다 조회 광고")
    superchat.click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"title__tags ttags"})
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '일일_유료컨텐츠조회수']
        df.to_csv('./savedata/mostviewad.csv', index = False)
def mostviewad_week():
    main_url = "https://playboard.co/"
    results = []
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)
    superchat = driver.find_element_by_link_text("최다 조회 광고")
    superchat.click()
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div.cnavi__wrapper > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.implicitly_wait(2)
    
    
    SCROLL_PAUSE_TIME = 0.7
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "lxml" )
    
    boxitem = soup.select("tbody > .chart__row")
    time.sleep(3)
    
    try:
        
        for item in boxitem:
            noads = item.text
            if noads != "":
                prolevel = item.find("div", {"class":"current"}).text
                protitle = item.find("img")['alt']
                protag = item.find("ul", {"class":"title__tags ttags"})
                superchat = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                protag = str(protag)
                exp = re.compile('#\w+')
                protag = exp.findall(protag)
                tag = ", ".join(protag)
                data = [prolevel, protitle, tag, superchat]
                results.append(data)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
        df = pd.DataFrame(results)
        df.columns = ['순위', '채널명', '태그', '주간_유료컨텐츠조회수']
        df.to_csv('./savedata/mostviewad_week.csv', index = False)
        

# 매일 11시 00분부터 일간통계 크롤링시작하기
schedule.every().day.at("11:00").do(supercraw)
schedule.every().day.at("11:01").do(LiveRank)
schedule.every().day.at("11:02").do(mostviewvideo)
schedule.every().day.at("11:03").do(subsoaring)
schedule.every().day.at("11:04").do(mostview)
schedule.every().day.at("11:05").do(mostviewad)

# 매주 월요일 11시 10분부터 주간통계 크롤링시작하기

schedule.every().monday.at("11:10").do(supercraw_week)
schedule.every().monday.at("11:11").do(LiveRank_week)
schedule.every().monday.at("11:12").do(mostviewvideo_week)
schedule.every().monday.at("11:13").do(subsoaring_week)
schedule.every().monday.at("11:14").do(mostview_week)
schedule.every().monday.at("11:15").do(mostviewad_week)


while True:
    # schedule 쓴거 시간맞으면 실행
    schedule.run_pending()
    #30초마다
    time.sleep(30)