
from selenium import webdriver
from selenium.webdriver.common import keys
from bs4 import BeautifulSoup
import time

Chrome = webdriver.Chrome('/Users/apple/Downloads/chromedriver')
Chrome.get('https://soundcloud.com/negzzzz/sets/negar')
Chrome.maximize_window()

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = Chrome.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    Chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = Chrome.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = Chrome.page_source

html_list = html.split('trackItem__trackTitle sc-link-dark sc-font-light')

print('len is:',len(html_list))


track_list = []
for item in html_list[1:]:
    str = ''
    for char in item[2:]:       
        if char is not '<':
            str += char
        else:
            break
    track_list.append(str)

print(track_list)

