from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


def get_anu_meal():
    url = 'https://www.andong.ac.kr/main/module/foodMenu/index.do?menu_idx=222'

    # 웹 드라이버 실행
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))  # Chrome 웹 드라이버의 경로를 지정하세요.
    driver.get(url)

    # 페이지가 완전히 로드될 때까지 기다림
    time.sleep(2)

    # # 자바스크립트 함수 실행 - 이전날 불러오기
    # driver.execute_script("prevDay();")
    # time.sleep(2)  # 자바스크립트 함수가 완전히 실행되기까지 기다림

    # # 자바스크립트 함수 실행 - 다음날 불러오기
    # driver.execute_script("nextDay();")
    # time.sleep(2)  # 자바스크립트 함수가 완전히 실행되기까지 기다림

    # 페이지의 HTML 가져오기
    ANUmealHTML = driver.page_source

    # BeautifulSoup 객체 생성
    soup_meal = BeautifulSoup(ANUmealHTML, 'html.parser')

    # 'div.cont' 클래스를 가진 요소 선택
    txt_temp = soup_meal.select('div.cont')

    # 선택한 요소의 텍스트 출력
    for div in txt_temp:
        print(div.get_text().strip())  # strip() 메소드로 앞뒤 공백 제거
        print("타입은 :", type(div))

    # 웹 드라이버 종료
    driver.quit()

get_anu_meal()
