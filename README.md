<h1 align='center'>:movie_camera: Youtube 트렌드 분석 :movie_camera:</p>
<br>
<h2> :date: Period</p>
<h4> 2021/07/10(토) - 2021/07/18(일)
<br><br>
<h2> :dancers: Team</p>
<h4> <a href = "https://github.com/dlwlsdudo1"><h6>이진영</a></details>&nbsp;,&nbsp;
<a href = "https://github.com/sujeong-jang-creator">장수정</a></details>&nbsp;,&nbsp;
<a href = "https://github.com/rnaqpddl123">정주영B </a></details>
<br><br>
<h2> :eyes: 주제선정</p>
<h4> - COVID-19로 인해 바깥으로 나가지 못하고 각자 집에서 YOUTUBE를 많이 보고있다. </p>
<h4> - 문득 내가 보고있는 YOUTUBE 채널은 하루 수입이 얼마나 되는지 궁금해졌다. </p>
<h4> - 그러면서, 채널 정보까지 한눈에 볼 수 있는 사이트가 생긴다면 좋을 거 생각을 했다. </p>
<br>  
<h2> :card_index: Process</h2>
<h4> 1. Crawling </p>
&nbsp;&nbsp;&nbsp; - https://playboard.co/ 페이지 크롤링</p>
&nbsp;&nbsp;&nbsp; - LiveRank, MostView, MostView, MostViewVideo, Subsoaring, SuperCraw 크롤링</p>
&nbsp;&nbsp;&nbsp; - 위 6개분야 chart 주간 크롤링</p>
<h4> 2. Saving </p>
&nbsp;&nbsp;&nbsp; - excel file 저장</p>
&nbsp;&nbsp;&nbsp; - csv file 저장</p>
<h4> 3. Connecting </p>
&nbsp;&nbsp;&nbsp; - Flask 이용 app.py 제작</p>
&nbsp;&nbsp;&nbsp; - Html 연결</p>
<h4> 4. Visualization </p>
&nbsp;&nbsp;&nbsp; - Html, CSS 제작 및 수정</p>
&nbsp;&nbsp;&nbsp; - Github 정리 및 README 제작</p>
<h4> 5. Application </p>
&nbsp;&nbsp;&nbsp; - button crawling 제작</p>
&nbsp;&nbsp;&nbsp; - auto crawling 제작</p>
<br>
<h2> :weary: 어려웠던점 </p>
<h4><details><summary> 1. Crawling 경로 지정 </p></summary>
<h4>&nbsp;&nbsp;&nbsp; 참고사이트 : https://www.selenium.dev/documentation/ko/webdriver/locating_elements/
<br><br>
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/find%EC%98%88%EC%8B%9C.JPG" />
<br>
<h4>&nbsp;&nbsp;&nbsp; : find 종류별 사용을 잘 알지 못하여 어려움을 겪었다. 그러나 지금은 어느정도 사용 가능하다!! </p></details>
<br>

<h4><details><summary> 2. Crawling 도중 공백 처리 </p></summary>
<br>
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/none%EC%B2%98%EB%A6%AC.jpg" />
<br>
<h4>&nbsp;&nbsp;&nbsp; :  Crawling 도중 공백이 나오면 정지 된다. 공백을 처리하는데 많은 시간을 들였다. </p></details>
<br>
  
<h4><details><summary> 3. 광고 처리 </p></summary>
<br>
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/%EA%B4%91%EA%B3%A0.JPG" />
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/text%EC%84%A4%EB%AA%851.jpg" />
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/text%EC%84%A4%EB%AA%852.jpg" /></details> 
<br>

<h4><details><summary> 4. 스크롤 내림 </p></summary> 
<br>
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/%EB%A1%9C%EB%94%A9%EC%84%A4%EB%AA%85.jpg" />
<img src="https://github.com/Sparkling-data/Youtube/blob/86ef2fe8a3d512acc215b966ba85fcfa5bcb164f/images/text%EC%84%A4%EB%AA%852.jpg" /></details>
<br>
