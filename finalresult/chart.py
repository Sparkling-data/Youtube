import numpy as np
import pandas as pd
import collections
import re
import json


class googlechart:

    # chart_num은 가져올 데이터의 양을 결정하고 chart_date는 가져올 파일명을 결정함
    def superchat(self,chart_num, chart_date):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date}supercraw.csv")


            chart_num = int(chart_num)
            df = df[0:chart_num]
            # 띄어쓰기 부분을 언더바로 연결해서 html에서 읽을수있게함
            # 원하는 데이터가 숫자가 아니라서 숫자로 바꿔줌  ex) ₩2,154,325 ->2154325
            df['일일_슈퍼챗수입'] = df['일일 슈퍼챗수입'].str.replace('₩', '').str.replace(',', '')
            # ex) ₩2,154,325 ->2154325 예제처럼 바꿔도 str타입이기 때문에 int타입으로 바꿔줘서 차트를 그릴수 있게해줌
            df['일일_슈퍼챗수입'] = df['일일_슈퍼챗수입'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf




    def LiveRank(self,chart_num, chart_date):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date}LiveRank.csv")

            chart_num = int(chart_num)
            df = df[0:chart_num]
            
            df['최고_동시_시청자수'] = df['최고 동시 시정자수'].str.replace('명', '').str.replace(',', '').str.replace('"', '')
            # print(df['최고_동시_시청자수'])
            df['최고_동시_시청자수'] = df['최고_동시_시청자수'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf




    def mostviewvideo(self,chart_num, chart_date):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date}mostviewvideo.csv")

            chart_num = int(chart_num)
            df = df[0:chart_num]
            df['일일조회수'] = df['일일조회수'].str.replace('"', '').str.replace(',', '')
            df['일일조회수'] = df['일일조회수'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf





    def subsoaring(self,chart_num, chart_date):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date}subsoaring.csv")

            chart_num = int(chart_num)
            df = df[0:chart_num]
            df['전체구독자'] = df['전체구독자'].str.replace('\r', '').str.replace('\n', '').str.replace(' ', '').str.replace(',', '')
            df['전체구독자'] = df['전체구독자'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf



    def mostview(self,chart_num, chart_date):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date}mostviewvideo.csv")

            chart_num = int(chart_num)
            df = df[0:chart_num]
            df['일일조회수'] = df['일일조회수'].str.replace(',', '')
            df['일일조회수'] = df['일일조회수'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf




    def mostviewad(self,chart_num, chart_date):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date}mostviewad.csv")

            chart_num = int(chart_num)
            df = df[0:chart_num]
            df['일일_유료컨텐츠조회수'] = df['일일_유료컨텐츠조회수'].str.replace(',', '')
            df['일일_유료컨텐츠조회수'] = df['일일_유료컨텐츠조회수'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf

    def superchat_week(self,chart_num2, chart_date2):
        try:

            df = pd.read_csv(f"./csv_savedata/{chart_date2}supercraw_week.csv")

            chart_num = int(chart_num2)
            df = df[0:chart_num]
            df['주간_슈퍼챗수입'] = df['주간 슈퍼챗수입'].str.replace('₩', '').str.replace(',', '')
            df['주간_슈퍼챗수입'] = df['주간_슈퍼챗수입'].astype('int')
            
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("구글 차트 완료")
        
        return asdf





# if __name__=='__main__':

#     googlechart.superchat()
