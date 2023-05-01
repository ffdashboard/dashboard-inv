#!/usr/bin/env python
# coding: utf-8

# In[1]:


null=None
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import streamlit as st
#import html
#from dash_html_components import Div_, Img, H3, A
#from dash import html
import json
null=None
from PIL import Image
from pytube import Search
import time


# In[7]:





# In[ ]:


#howard marks
driver1=webdriver.Chrome()
url1="https://www.oaktreecapital.com/insights"
driver1.get(url1)
inv1="Howard Marks"
driver1.maximize_window()
link1=driver1.find_element(By.XPATH,'/html/body/div[1]/main/div[1]/div/div/ul[2]/li[1]/div/div[2]/div[1]/a').get_attribute("href")
img1 = driver1.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/ul[2]/li[1]/div/div[2]/div[1]/a/div/img').get_attribute("src")
text1= driver1.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/ul[2]/li[1]/div/div[2]/div[1]/a/div/img').get_attribute("alt")
driver1.close()
#ray dilio(bridgewater)
url2="https://www.bridgewater.com/research-and-insights"
driver2=webdriver.Chrome()
driver2.get(url2)
inv2="Ray Dilio"
link2=driver2.find_element(By.XPATH,'/html/body/div[2]/main/div[4]/ps-list-showmore/div/div[2]/ps-masonry-list/div[1]/ps-promo/div/div[1]/a').get_attribute("href")
img2 = driver2.find_element(By.XPATH, '/html/body/div[2]/main/div[4]/ps-list-showmore/div/div[2]/ps-masonry-list/div[1]/ps-promo/div/div[1]/a/source[2]').get_attribute("srcset")
text2= driver2.find_element(By.XPATH, '/html/body/div[2]/main/div[4]/ps-list-showmore/div/div[2]/ps-masonry-list/div[1]/ps-promo/div/div[1]/a').get_attribute("aria-label")
driver2.close()
#realvision
url3="https://www.realvision.com/shows/real-visionaries-alex-gurevich"
driver3=webdriver.Chrome()
driver3.get(url3)
inv3="RealVision"
link3=driver3.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div[2]/div/div[1]/div/div[2]/a').get_attribute("href")
img3 = driver3.find_element(By.XPATH, '//*[@id="main"]/section/div/div[2]/a/div/picture/source[1]').get_attribute("srcset")
text3= driver3.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/main/div/section[2]/div[2]/div/div[1]/div/div[2]/a/h3').text
driver3.close()
#macrohive
url4="https://macrohive.com/all/hive-videos/the-week-ahead/"
driver4=webdriver.Chrome()
driver4.get(url4)
inv4="Macro Hive"
link4=driver4.find_element(By.XPATH,'/html/body/main/div/section/article/a').get_attribute("href")
img4 = driver4.find_element(By.XPATH, '/html/body/main/div/section/article/a/figure/img').get_attribute("src")
text4= driver4.find_element(By.XPATH, '/html/body/main/div/section/article/a/figure/img').text
driver4.close()
#curveadvisor
url5="https://curveadvisor.substack.com/"
driver5=webdriver.Chrome()
driver5.get(url5)
inv5="Curve Advisor"
link5=driver5.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div[2]/a[1]').get_attribute("href")
img5 = driver5.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/picture/img').get_attribute("src")
text5= driver5.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[2]/a[1]').text
driver5.close()



# In[ ]:


def display_insight(link, img, text,inv):
            st.write(inv)
            st.image(img,caption= text)
            st.markdown(link, unsafe_allow_html=True)


# In[ ]:


while True:
    driver1=webdriver.Chrome()
    url1="https://www.oaktreecapital.com/insights"
    driver1.get(url1)
    inv1="Howard Marks"
    driver1.maximize_window()
    link1=driver1.find_element(By.XPATH,'/html/body/div[1]/main/div[1]/div/div/ul[2]/li[1]/div/div[2]/div[1]/a').get_attribute("href")
    img1 = driver1.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/ul[2]/li[1]/div/div[2]/div[1]/a/div/img').get_attribute("src")
    text1= driver1.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/ul[2]/li[1]/div/div[2]/div[1]/a/div/img').get_attribute("alt")
    driver1.close()
    #ray dilio(bridgewater)
    url2="https://www.bridgewater.com/research-and-insights"
    driver2=webdriver.Chrome()
    driver2.get(url2)
    inv2="Ray Dilio"
    link2=driver2.find_element(By.XPATH,'/html/body/div[2]/main/div[4]/ps-list-showmore/div/div[2]/ps-masonry-list/div[1]/ps-promo/div/div[1]/a').get_attribute("href")
    img2 = driver2.find_element(By.XPATH, '/html/body/div[2]/main/div[4]/ps-list-showmore/div/div[2]/ps-masonry-list/div[1]/ps-promo/div/div[1]/a/source[2]').get_attribute("srcset")
    text2= driver2.find_element(By.XPATH, '/html/body/div[2]/main/div[4]/ps-list-showmore/div/div[2]/ps-masonry-list/div[1]/ps-promo/div/div[1]/a').get_attribute("aria-label")
    driver2.close()
    #realvision
    url3="https://www.realvision.com/shows/real-visionaries-alex-gurevich"
    driver3=webdriver.Chrome()
    driver3.get(url3)
    inv3="RealVision"
    link3=driver3.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div[2]/div/div[1]/div/div[2]/a').get_attribute("href")
    img3 = driver3.find_element(By.XPATH, '//*[@id="main"]/section/div/div[2]/a/div/picture/source[1]').get_attribute("srcset")
    text3= driver3.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/main/div/section[2]/div[2]/div/div[1]/div/div[2]/a/h3').text
    driver3.close()
    #macrohive
    url4="https://macrohive.com/all/hive-videos/the-week-ahead/"
    driver4=webdriver.Chrome()
    driver4.get(url4)
    inv4="Macro Hive"
    link4=driver4.find_element(By.XPATH,'/html/body/main/div/section/article/a').get_attribute("href")
    img4 = driver4.find_element(By.XPATH, '/html/body/main/div/section/article/a/figure/img').get_attribute("src")
    text4= driver4.find_element(By.XPATH, '/html/body/main/div/section/article/a/figure/img').text
    driver4.close()
    #curveadvisor
    url5="https://curveadvisor.substack.com/"
    driver5=webdriver.Chrome()
    driver5.get(url5)
    inv5="Curve Advisor"
    link5=driver5.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div[2]/a[1]').get_attribute("href")
    img5 = driver5.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/picture/img').get_attribute("src")
    text5= driver5.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[2]/a[1]').text
    driver5.close()


    display_insight(link1,img1,text1,inv1) 
    display_insight(link2,img2,text2,inv2)
    display_insight(link3,img3,text3,inv3)
    display_insight(link4,img4,text4,inv4) 
    display_insight(link5,img5,text5,inv5) 
    s = Search('jim bianco')
    results = s.results
    inv6="Jim Bianco"
    results = sorted(results, key=lambda v: v.publish_date, reverse=True)
    for result in results:
        video = result
        display_insight(video.watch_url,video.thumbnail_url,video.title,inv6)
    time.sleep(900)  


# In[ ]:





# In[ ]:





# In[ ]:




