from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
# from selenium.webdriver.support.ui import WebDriverWait

class SuperChat():

    def supercraw(self):
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
        # print("-----스크롤 페이지 이동-----")


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
        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # print("태그 = ", tag)
                    # print("일일 슈퍼챗 수입 = ", superchat)
                    # print("일일 슈퍼챗 개수 = ", superchat_num)
                    # print("=" * 100)

        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()

            # pandas로 crawling data exel 저장
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '일일 슈퍼챗수입', '일일 슈퍼챗개수']
            df.to_csv('./savedata/supercraw.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data
    



    def supercraw_week(self):
        main_url = "https://playboard.co/"
        results = []

        driver = webdriver.Chrome("c:/driver/chromedriver.exe")

        driver.get(main_url)
        time.sleep(3)
        driver.implicitly_wait(2)

        superchat = driver.find_element_by_link_text("슈퍼챗 순위")
        superchat.click()
        # 크롤링하는데있어 모든 경로를 보는것은 좋지않은 방식, 할아버지정도만 불러와도 충분함
        driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
        time.sleep(3)
        driver.implicitly_wait(2)
        # print("-----스크롤 페이지 이동-----")


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
        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # print("태그 = ", tag)
                    # print("주간 슈퍼챗 수입 = ", superchat)
                    # print("주간 슈퍼챗 개수 = ", superchat_num)
                    # print("=" * 100)

        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()

            # pandas로 crawling data exel 저장
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '주간 슈퍼챗수입', '주간 슈퍼챗개수']
            df.to_csv('./savedata/supercraw_week.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data









    def LiveRank(self):
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
        # print("-----스크롤 페이지 이동-----")
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
        # print("-----화면 제일 하단 스크롤 로딩 완료----")
        soup = BeautifulSoup(driver.page_source, "lxml" )
        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
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
                    LiveYoutube = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-none up"}).text
                    
                    protag = str(protag)
                    exp = re.compile('#\w+')
                    protag = exp.findall(protag)
                    tag = ", ".join(protag)

                    data = [prolevel, protitle, tag,LiveYoutube]
                    results.append(data)

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)

                    # print("태그 = ", tag)
                    # print("최고 동시 시청자수 = ", LiveYoutube)
                    # print("=" * 100)

        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()

            # pandas로 crawling data exel 저장
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '최고 동시 시정자수']
            df.to_csv('./savedata/LiveRank.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data




    def LiveRank_week(self):
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
        # print("-----스크롤 페이지 이동-----")
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
        # print("-----화면 제일 하단 스크롤 로딩 완료----")
        soup = BeautifulSoup(driver.page_source, "lxml" )
        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
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
                    LiveYoutube = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-none up"}).text
                    
                    protag = str(protag)
                    exp = re.compile('#\w+')
                    protag = exp.findall(protag)
                    tag = ", ".join(protag)

                    data = [prolevel, protitle, tag,LiveYoutube]
                    results.append(data)

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)

                    # print("태그 = ", tag)
                    # print("주간 최고 동시 시청자수 = ", LiveYoutube)
                    # print("=" * 100)

        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()

            # pandas로 crawling data exel 저장
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '주간 최고 동시 시청자수']
            df.to_csv('./savedata/LiveRank_week.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data



    def mostviewvideo(self):
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
        # print("-----스크롤 페이지 이동-----")

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

        # print("-----화면 제일 하단 스크롤 로딩 완료----")


        soup = BeautifulSoup(driver.page_source, "lxml" )
        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
        time.sleep(3)
        # 정보 가져오기
        
        try:
            # 광고는 text가 없어서 광고 없애려고 for문 씀
            for item in boxitem:
                noads = item.text
                
                if noads != "":
                    # prolevel = item.find("div", {"class":"current"}).text
                    # if prolevel == "106":
                    prolevel = item.find("div", {"class":"current"}).text
                    protitle = item.find("img")['alt']

                    protag = item.find("ul", {"class":"name__tags ttags"})
                    views = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                    Like = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"})
                    
                    # Like값중에 None값이 있어서 해결하기위해 넣은코드
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("일일 조회수 = ", views)
                    # print("일일 좋아요 수 = ", Like)
                    # print("=" * 100)

        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '일일조회수', '일일 좋아요 수']
            df.to_csv('./savedata/mostviewvideo.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data
        




    def mostviewvideo_week(self):
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
        # print("-----스크롤 페이지 이동-----")

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

        # print("-----화면 제일 하단 스크롤 로딩 완료----")


        soup = BeautifulSoup(driver.page_source, "lxml" )
        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
        time.sleep(3)
        # 정보 가져오기
        
        try:
            # 광고는 text가 없어서 광고 없애려고 for문 씀
            for item in boxitem:
                noads = item.text
                
                if noads != "":
                    # prolevel = item.find("div", {"class":"current"}).text
                    # if prolevel == "106":
                    prolevel = item.find("div", {"class":"current"}).text
                    protitle = item.find("img")['alt']

                    protag = item.find("ul", {"class":"name__tags ttags"})
                    views = item.find("span", {"class":"fluc-label fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"}).text
                    Like = item.find("span", {"class":"fluc-label fluc-label--mono-color fluc-label--mono-font fluc-label--ko fluc-label--symbol-math up"})
                    
                    # Like값중에 None값이 있어서 해결하기위해 넣은코드
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("주간 조회수 = ", views)
                    # print("주간 좋아요 수 = ", Like)
                    # print("=" * 100)

        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '주간 조회수', '주간 좋아요 수']
            df.to_csv('./savedata/mostviewvideo_week.csv', index = False)
            # print("---------crawling file save 완료------------")           
            data = "크롤링완료"

        return data



    def subsoaring(self):
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
        # print("-----스크롤 페이지 이동-----")


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
        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
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
                    superchat_num = item.find("td", {"class":"score"}).text
                    # superchat_num = item.find("td[2]", {"class":"score"})
                    # print(superchat_num)


                    protag = str(protag)
                    exp = re.compile('#\w+')
                    protag = exp.findall(protag)
                    tag = ", ".join(protag)

                    data = [prolevel, protitle, tag, superchat, superchat_num]
                    results.append(data)

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("일일_신규구독자 = ", superchat)
                    # print("전체구독자 = ", superchat_num)
                    # print("=" * 100)


        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '일일_신규구독자', '전체구독자']
            df.to_csv('./savedata/subsoaring.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data




    def subsoaring_week(self):
        main_url = "https://playboard.co/"
        results = []

        driver = webdriver.Chrome("C:/driver/chromedriver.exe")

        driver.get(main_url)
        time.sleep(3)
        driver.implicitly_wait(2)

        superchat = driver.find_element_by_link_text("구독자 급상승 순위")
        superchat.click()
        time.sleep(3)
        #driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
        driver.find_element_by_css_selector("#app > div.__window > div > main > div > div.cnavi.cnavi > div > div > div > div:nth-child(4) > ul > li:nth-child(2) > span").click()
        time.sleep(3)
        driver.implicitly_wait(2)
        # print("-----스크롤 페이지 이동-----")


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
        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
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
                    superchat_num = item.find("td", {"class":"score"}).text
                    # superchat_num = item.find("td[2]", {"class":"score"})
                    # print(superchat_num)


                    protag = str(protag)
                    exp = re.compile('#\w+')
                    protag = exp.findall(protag)
                    tag = ", ".join(protag)

                    data = [prolevel, protitle, tag, superchat, superchat_num]
                    results.append(data)

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("주간_신규구독자 = ", superchat)
                    # print("전체구독자 = ", superchat_num)
                    # print("=" * 100)


        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '주간_신규구독자', '전체구독자']
            df.to_csv('./savedata/subsoaring_week.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data




    def mostview(self):
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
        # print("-----스크롤 페이지 이동-----")


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



        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
        time.sleep(3)


        # 정보 가져오기
        try:
            # 광고는 text가 없어서 광고 없애려고 for문 씀
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("일일_조회수 = ", superchat)
                    # # print("슈퍼챗 개수 = ", superchat_num)
                    # print("=" * 100)
                    


        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '일일_조회수']
            df.to_csv('./savedata/mostview.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data



    def mostview_week(self):
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
        # print("-----스크롤 페이지 이동-----")


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



        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
        time.sleep(3)


        # 정보 가져오기
        try:
            # 광고는 text가 없어서 광고 없애려고 for문 씀
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("주간_조회수 = ", superchat)
                    # # print("슈퍼챗 개수 = ", superchat_num)
                    # print("=" * 100)


        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()
            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '주간_조회수']
            df.to_csv('./savedata/mostview_week.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data






    def mostviewad(self):
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
        # print("-----스크롤 페이지 이동-----")


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



        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
        time.sleep(3)


        # 정보 가져오기
        try:
            # 광고는 text가 없어서 광고 없애려고 for문 씀
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("일일_유료컨텐츠조회수 = ", superchat)
                    # # print("슈퍼챗 개수 = ", superchat_num)
                    # print("=" * 100)


        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()


            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '일일_유료컨텐츠조회수']
            df.to_csv('./savedata/mostviewad.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data



    def mostviewad_week(self):
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
        # print("-----스크롤 페이지 이동-----")


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



        # print("-----화면 제일 하단 스크롤 로딩 완료----")

        soup = BeautifulSoup(driver.page_source, "lxml" )

        # 정보박스 찾기
        boxitem = soup.select("tbody > .chart__row")
        # # print(boxitem)
        # print("-----스크롤 박스 찾기 완료-----")
        time.sleep(3)


        # 정보 가져오기
        try:
            # 광고는 text가 없어서 광고 없애려고 for문 씀
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

                    # print("No_{}".format(prolevel))
                    # print("채널명 = ", protitle)
                    # for tag in protag:
                    # print("태그 = ", tag)
                    # print("주간_유료컨텐츠조회수 = ", superchat)
                    # # print("슈퍼챗 개수 = ", superchat_num)
                    # print("=" * 100)


        except Exception as e:
            print("페이지 파싱 에러", e)

        finally:
            time.sleep(3)
            # print("크롤링을 종료합니다.")
            driver.close()


            df = pd.DataFrame(results)
            df.columns = ['순위', '채널명', '태그', '주간_유료컨텐츠조회수']
            df.to_csv('./savedata/mostviewad_week.csv', index = False)
            # print("---------crawling file save 완료------------")
            data = "크롤링완료"

        return data



# if __name__=='__main__':
#     #SuperChat.supercraw() 
#     #SuperChat.supercraw_week() 
#     #SuperChat.LiveRank() 
#     #SuperChat.LiveRank_week() 
#     #SuperChat.subsoaring()
#     #SuperChat.subsoaring_week() 
#     #SuperChat.mostview()
#     #SuperChat.mostview_week()
#     #SuperChat.mostviewvideo()
#     #SuperChat.mostviewvideo_week()
#     #SuperChat.mostviewad() 
#     SuperChat.mostviewad_week()
