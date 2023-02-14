import time as tm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import os
import undetected_chromedriver as uc
from datetime import *

def email_modify(self,channel,choosen_option,driver,wait):
    next_page=0
    while next_page == 0:
        checking = wait.until(lambda x: x.find_elements(By.ID,"text-input")[-1])
        wait.until(EC.element_to_be_clickable(checking))
        vids = driver.find_elements(By.XPATH, """//*[@id="row-container"]/div[4]/div/div/tp-yt-iron-icon""")
        # vids = wait.until(lambda x: x.find_elements(By.XPATH, """//*[@id="row-container"]/div[4]/div/div/tp-yt-iron-icon""")) 
        if len(vids)<1:
            driver.quit()
            print("영상이 없습니다.")
            self.inform.config(text="영상이 없습니다.")
            return 
        for vid in vids:
            while True:
                try:
                    add_email(vid,choosen_option,channel['email'],driver,wait)
                    break
                except Exception as e: 
                    print(e,"오류남")
                    return
        next_list=wait.until(EC.element_to_be_clickable((By.ID,"navigate-after")))
        if next_list.get_attribute("aria-disabled") == 'false':
            next_list.click()
            tm.sleep(2)
        elif next_list.get_attribute("aria-disabled") == 'true':
            next_page=1
    print("끝")
    self.inform.config(text="추가 완료")
    tm.sleep(30)
    driver.quit()

def initialize():
    driver = uc.Chrome()
    driver.implicitly_wait(10) 
    wait = WebDriverWait(driver, 180)
    return driver,wait

def save_check():
    try:
        f=open("save.txt",'r')
        data=f.read().split(",")
        print(date.fromtimestamp(data[1]))
        return float(data[1])
    except Exception as e:
        f=open("save.txt",'w')
        f.write("이메일@이메일.com,0000")
        return float(data[1])

def setting(location,last_time,choosed_option,day):
    channels=[]
    files=[i for i in os.listdir(location) if i!='.DS_Store']
    files=[i for i in files if i[0]!="."]
    for i in files: 
        file_title=i.split(".")[0].split(",")
        channel_day=file_title[-1].split("&")
        file={
            "file_dir":location+"/"+i, 
            "name":file_title[0],
            "tag":file_title[1],
            "mtime":os.path.getmtime(location+"/"+i),
            "email":sorted([i.lower() for i in pd.read_csv(location+"/"+i,).이메일])
        }
        if choosed_option.lower()=="private":
            if last_time<file['mtime']:
                channels.append(file)
        elif choosed_option.lower()=="unlisted":
            if day in channel_day:
                channels.append(file)

    return channels


def buttons(key,driver,wait):
    if key == "check":
        check = wait.until(lambda x: x.find_elements(By.XPATH, """//*[@id="notify-via-email-checkbox"]""")[-1])
        wait.until(EC.element_to_be_clickable(check))
        check.click()
    elif key == "option":
        option = wait.until(lambda x: x.find_elements(By.ID,"private-radio-button")[-1])
        wait.until(EC.element_to_be_clickable(option))
        option.click()
    elif key == "setting":
        setting = wait.until(lambda x: x.find_elements(By.XPATH,"""//*[@id="privacy-radios"]/div/ytcp-button/div""")[-1])
        wait.until(EC.element_to_be_clickable(setting))
        setting.click()
    elif key == "done":
        done = wait.until(lambda x: x.find_elements(By.XPATH,"""//*[@id="done-button"]/div""")[-1])
        wait.until(EC.element_to_be_clickable(done))
        done.click()
    elif key == "save":
        save = wait.until(lambda x: x.find_elements(By.XPATH,"""//*[@id="save-button"]/div""")[-1])
        wait.until(EC.element_to_be_clickable(save))
        save.click()
    elif key == "reset_email":
        reset_email = wait.until(lambda x: x.find_elements(By.XPATH,"""//*[@id="clear-button"]/tp-yt-iron-icon""")[-1])
        wait.until(EC.element_to_be_clickable(reset_email))
        reset_email.click()
    elif key == "text_input":
        text_input = wait.until(lambda x:x.find_elements(By.ID,"text_input")[-1])
        wait.until(EC.element_to_be_clickable(text_input))
        text_input.click()

def login(user_id,user_pw,driver,wait):
    driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.find_element(By.XPATH,"""//*[@id="identifierId"]""").send_keys(user_id)
    driver.find_element(By.XPATH,"""//*[@id="identifierId"]""").send_keys(Keys.RETURN)
    wait.until(EC.element_to_be_clickable((By.XPATH,"""//*[@id="password"]/div[1]/div/div[1]/input""")))
    driver.find_element(By.XPATH,"""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(user_pw)
    driver.find_element(By.XPATH,"""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(Keys.RETURN)
    wait.until(EC.url_contains("https://myaccount.google.com/?utm_source=sign_in_no_continue&pli=1"))
    wait.until(EC.url_contains("https://myaccount.google.com/?utm_source=sign_in_no_continue&pli=1"))
    driver.get("https://www.youtube.com/?gl=KR&tab=k1")
    wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="channel-title"]""")))
    driver.find_elements(By.XPATH,"""//*[@id="channel-title"]""")[0].click()

def select_channel(name,tag,option,driver,wait):
    driver.get("https://www.youtube.com/channel_switcher")
    channels = wait.until(lambda x: x.find_elements(By.ID,"channel-title"))
    channel=[i for i in channels if i.text == name]
    channel[0].click()
    driver.get(f"https://studio.youtube.com/channel/{tag}/videos/live?filter=%5B%7B%22name%22%3A%22VISIBILITY%22%2C%22value%22%3A%5B%22{option.upper()}%22%5D%7D%5D&sort=%7B%22columnType%22%3A%22live_date%22%2C%22sortOrder%22%3A%22ASCENDING%22%7D")
    

def add_email(vid,option,email,driver,wait):
    wait.until(EC.element_to_be_clickable(vid))
    vid.click()
    if option.lower() == "unlisted":
        buttons("option",driver,wait)
    buttons("setting",driver,wait)
    video_email=sorted([i.text.lower() for i in driver.find_elements(By.ID,"outer")[-1].find_elements(By.ID,"chip-text")])
    if video_email == email:
        cancel = wait.until(lambda x:x.find_elements(By.XPATH,"""//*[@id="cancel-button"]/div"""))
        cancel[-1].click()
        cancel[-2].click()
        return
    if len(video_email)>0:
        buttons("reset_email",driver,wait)
    for j in email:
        driver.find_elements(By.XPATH,"""//*[@id="text-input"]""")[-1].send_keys(j,Keys.SPACE)
    buttons("check",driver,wait)
    buttons("done",driver,wait)
    buttons("save",driver,wait)

