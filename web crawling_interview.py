#packages

import pandas as pd
from bs4 import BeautifulSoup #url로부터 받아온 html text를 parser하여 원하는 정보 추출
from selenium import webdriver
import urllib.request #requests : web url에 접근 및 html 받아옴
from selenium.webdriver.chrome.options import Options
import time
import re
from selenium.webdriver import Actionchains

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)



#login

#login page

url_log = "https://id.payco.com/oauth2.0/authorize?response_type=code&client_id=3RDvvpbFXPDNA2XkpbZc&serviceProviderCode=FRIENDS&redirect_uri=https%3A%2F%2Fedit%2Eincruit%2Ecom%2Fg%5Fcommon%2Fbizcommon%2Fv2%2Fpayco%2Easp%3F1%3D1%26kl%3Dfalse"
            
html_id = "id" #id입력칸 name
html_pw = "pw" #pw입력칸 name
login_bt = '//*[@id="loginBtn"]' #로그인버튼Xpath

driver.implicitly_wait(3) #웹페이지 전체 정보가 넘어올때까지 기다리기

driver.get(url_log)
login_x_path = login_bt
driver.find_element_by_name('id').send_keys('<bins0617@naver.com>')
driver.find_element_by_name('pw').send_keys('<159159gkgk*>')
driver.find_element_by_xpath(login_x_path).click()



#반복문1

for i in range(347) :
    
    driver.get('https://people.incruit.com/interview/intvtable.asp?page=' + str(i) +'&group1=0&sot=1&p=&occ2=&detcd=')
    driver.implicitly_wait(3)
    
    
    
    #반복문2

    for j in range(20) :

        
        #기업배너클릭

        menu = driver.find_element_by_xpath('//*[@id="divintvtable"]/div[2]/table/tbody/tr[' + str( j + 1) + ']/td[3]/div/a/div')
        menu.click()


        #web crawling

        url = driver.current_url
        req = urllib.request.urlopen(url) #url정보가져옴
        res = req.read() #url에 있는 html data를 바이트 문자열로 반환

        soup = BeautifulSoup(res, 'html.parser') #html정보 파싱
        keywords = soup.find_all('div', span = "detail_info") #로그인버튼 클릭

        itv = itv + keywords #keywords의 data형식 확인해봐야함
        
        
        #뒤로가기

        driver.back()
