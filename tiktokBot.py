from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM 
from selenium.webdriver.common.keys import Keys
import config as cf
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import threading
import pickle
import time
import until 
import random
import requests 
import os
import keyboard 
from webdriver_manager.chrome import ChromeDriverManager 
from elements_manager import *
from subprocess import check_call
from os import system, get_terminal_size
from pystyle import Colorate, Colors, Write 
import multiprocessing


def start(b, url=None):
    x = 0
    while x < 1:
        # b = 0
        while b < (cf.AMOUNT_LOOPS):
            c = b
            while c < (cf.AMOUNT_COOKIES):
                options = webdriver.ChromeOptions()
                profile_path = f"user-data-dir={cf.local['userDataDir']}{b}"
                options.add_argument(profile_path)
                options.add_experimental_option(
                    "excludeSwitches", ["enable-logging"]
                )
                options.add_extension("Cookie-Editor.crx")

                options.add_experimental_option(
                    "prefs",
                    {
                        "profile.default_content_setting_values.notifications": 2
                    },
                )

                print("")
                print(f"[Thread {b}] - Running Path: Chrome Profile No.{b}")
                time.sleep(3)

                service = Service(cf.local["executablePath"])
                bot = webdriver.Chrome(options=options)
                wait = WebDriverWait(bot, 5)
                actions = ActionChains(bot)
                bot.maximize_window()

                bot.get("https://www.tiktok.com/")
                actions.send_keys(Keys.ENTER)
                actions.perform()
                time.sleep(3)

                url = "https://www.tiktok.com/" if url is None else url

                # ====================== START GET COOKIES ==================== #

                bot.delete_all_cookies()
                bot.get(url)

                cookies = pickle.load(
                    open(f"Cookies/cookies ({c}).cookies", "rb")
                )

                for cookie in cookies:
                    bot.add_cookie(cookie)

                print(f"[Thread {b}] - Load Cookies No.{c}")

                bot.get(url)
                time.sleep(3)

                print(f"[Thread {b}] - Get Cookies Now! No.{c}")
                time.sleep(3)

                pickle.dump(
                    bot.get_cookies(),
                    open(f"Cookies/cookies ({c}).cookies", "wb"),
                )

                # ====================== END GET COOKIES ==================== #

                v = 1
                while v < 2:
                    ImgDir = cf.DataImg["imgDataDir"]
                    ImgName = cf.DataImg["imgName"]
                    ImgFormat = cf.DataImg["imgFormat"]
                    random_videos = random.randint(1, 2)
                    dataVideos = f"{ImgDir}{ImgName}({random_videos}){ImgFormat}"
                    print(f"[Thread {b}] - Posting Music No.{random_videos}")
                    time.sleep(3)

                    bot.get("https://www.tiktok.com/creator-center/upload?from=creator_center")
                    time.sleep(6)

                    try:
                        # ===========> Upload Videos
                        # There is an iframe on the page...
                        iframe = bot.find_element(By.CSS_SELECTOR, "iframe")
                        bot.switch_to.frame(iframe)

                        # Wait until page loads...
                        time.sleep(15)

                        # Select the input file and send the filename...
                        upload = bot.find_element(
                            By.CSS_SELECTOR, 'input[type="file"]'
                        )
                        upload.send_keys(str(dataVideos))
                        time.sleep(40)

                        try:

                            # Select the button Post...
                            bot.find_element(
                                By.XPATH,
                                "//button[contains(.,'Post')]",
                            ).click()
                            time.sleep(25)

                            print(
                                f"[Thread {b}] - [Cookies No.{c}] -> Video No.{v} DONE! & Please Wait.."
                            )

                            time.sleep(15)

                        except:
                            print(
                                f"[Thread {b}] - Posting Failed! & Please Wait.."
                            )

                    except:
                        print(f"[Thread {b}] - ERROR!, Posting Gagal..")

                    v += 1

                bot.delete_all_cookies()
                bot.get(url)

                bot.quit()
                c += cf.AMOUNT_THREAD

            b += 0

        x += 0


def main():
    profiles = []

    for i in range(cf.AMOUNT_THREAD):
        profiles += [threading.Thread(target=start, args=[i])]

    for i in profiles:
        i.start()


if __name__ == "__main__":
    main()
