import os, sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

sys.path.append(os.pardir)

import pandas as pd

file_name = 'mbti.xlsx'
df = pd.read_excel(file_name)
names = df['이름']
names_list = []
for i in names[649:]:
    names_list.append(i)
keywords = names_list
number = 3

driver = webdriver.Chrome()
driver.get(f'https://www.google.com/imghp')
for keyword in keywords:
    query = keyword

    elem = driver.find_element("name", "q")
    elem.clear()
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 0.3
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height
        break

    img_elements = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    imgs = []

    count = 1

    for idx, img in enumerate(img_elements):
        print(f"{query} : {idx + 1}/{len(img_elements)} proceed...")
        try:
            img.click()
            time.sleep(0.5)
            img_element = driver.find_element(By.XPATH,
                                              f'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
            img_src = img_element.get_attribute('src')
            img_alt = img_element.get_attribute('alt')
            imgs.append({
                'alt': img_alt,
                'src': img_src
            })

        except:
            print(f'err in {idx}')
            pass

        count += 1
        if count > number:
            break

    save_path = f'C:\img'
    import os
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    total_N = len(imgs)
    for idx, one in enumerate(imgs):
        src = one['src']
        alt = one['alt']
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(src, f"{save_path}\{query}_{idx}.png")
        except:
            pass
        print(idx, alt)

driver.close()