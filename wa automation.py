# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:30:37 2022

@author: ACER
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.support import expected_conditions as Ec
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

import pyperclip as pc


options = Options()
profile = r"C:\Users\ACER\AppData\Local\Google\Chrome\User Data"
options.add_argument(f"user-data-dir={profile}")
options.add_argument('--profile-directory=Profile 2')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

groups = ["test"]  # ["Home❤"]
message = "Test message from Skytrix AI bot!!"
caption = "AI"


def attach():

    attach_box = '//div[@role="button"][@title="Attach"]'

    attach_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, attach_box)))

    attach_box.click()
    time.sleep(2)

    image_box = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'

    image_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, image_box)))

    image_box.send_keys(r"C:\Users\ACER\Downloads\Blue Yellow Modern Creative Business Agency Corporate Instagram Post.png")

    text_box_img = '//div[@contenteditable="true"][@data-testid="media-caption-input-container"]'

    text_box_img = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, text_box_img)))

    # text_box.send_keys(message)
    pc.copy(caption)
    text_box_img.send_keys(Keys.CONTROL + "v")

    send_btn = '//span[@data-icon="send"]'

    send_btn = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, send_btn)))

    send_btn.click()


for group in groups:

    search_box = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, search_box)))

    search_box.clear()

    pc.copy(group)
    search_box.send_keys(Keys.CONTROL + "v")

    group_title = f'//span[@title="{group}"]'

    group_title = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, group_title)))

    group_title.click()

    time.sleep(1)

    text_box = '//div[@contenteditable="true"][@data-tab="10"]'

    text_box = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, text_box)))

    # text_box.send_keys(message)
    pc.copy(message)
    text_box.send_keys(Keys.CONTROL + "v")
    text_box.send_keys(Keys.ENTER)

    attach()
