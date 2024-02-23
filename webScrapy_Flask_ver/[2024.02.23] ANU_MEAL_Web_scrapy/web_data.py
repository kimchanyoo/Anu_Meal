from flask import Flask, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options



app = Flask(__name__)
CORS(app)

@app.route('/anu-meal', methods=['GET'])
def get_anu_meal():
    try:
            url = 'https://www.andong.ac.kr/main/module/foodMenu/index.do?menu_idx=222'

            options = Options()
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

            # 웹 드라이버 실행
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # Chrome 웹 드라이버의 경로를 지정하세요.

            driver.get(url)

            # 페이지가 완전히 로드될 때까지 기다림
            time.sleep(2)

            breakfast_temp = driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[2]/dl[1]/dd').text
            lunch_temp = driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[2]/dl[2]/dd').text
            dinner_temp = driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[2]/dl[3]/dd').text
            date_temp = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/span').text
            date = date_temp[:-3]

            breakfast_temp = list(breakfast_temp)
            temp_list = []
            for i in breakfast_temp:
                temp = i.replace("\n", " ")
                temp_list.append(temp)
            breakfast = "".join(temp_list)

            temp_list = []
            for i in lunch_temp:
                temp = i.replace("\n", " ")
                temp_list.append(temp)
            lunch = "".join(temp_list)

            dinner_temp = list(dinner_temp)
            temp_list = []
            for i in dinner_temp:
                temp = i.replace("\n", " ")
                temp_list.append(temp)
            dinner = "".join(temp_list)

            # 웹 드라이버 종료
            driver.quit()

            # 결과를 JSON으로 반환
            return jsonify({
                'date': date,
                'breakfast': breakfast,
                'lunch': lunch,
                'dinner': dinner,
        })
    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
