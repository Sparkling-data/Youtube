import numpy as np
import pandas as pd
import collections
import re
import json


class googlechart:

    def superchat(self,chart_num):
        try:

            print("-=---1---------")
            df = pd.read_csv("C:/202105_lab/gitClone/Youtube/crawling/csv_savedata/supercraw.csv")
            print("-=---2---------")
            chart_num = int(chart_num)
            df = df[0:chart_num]
            df['일일_슈퍼챗수입'] = df['일일 슈퍼챗수입'].str.replace('₩', '').str.replace(',', '')
            df['일일_슈퍼챗수입'] = df['일일_슈퍼챗수입'].astype('int')
            print(df)
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("asd")
        
        return asdf

    def superchat(self,chart_num):
        try:

            print("-=---1---------")
            df = pd.read_csv("C:/202105_lab/gitClone/Youtube/crawling/csv_savedata/supercraw.csv")
            print("-=---2---------")
            chart_num = int(chart_num)
            df = df[0:chart_num]
            df['일일_슈퍼챗수입'] = df['일일 슈퍼챗수입'].str.replace('₩', '').str.replace(',', '')
            df['일일_슈퍼챗수입'] = df['일일_슈퍼챗수입'].astype('int')
            print(df)
            asdf = df.to_json(orient = 'records', force_ascii=False)

        except Exception as e:
            print("페이지 파싱에러", e)
            asdf = "범위가 맞지 않습니다"
        finally:
            print("asd")
        
        return asdf





    def livelank(self,num):
        df = pd.read_csv("./crawling/csv_savedata/supercraw.csv")
        df = df.head()
        print(df)


        return 123






# if __name__=='__main__':

#     googlechart.superchat()
