from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from elements_manager import *
from subprocess import check_call
from pystyle import Colorate, Colors, Write
from time import sleep
import threading
import pickle
import until
import random
import requests
import os
import sys
import time

import config as cf


def start(b, url=None):
    x = 0
    while x < 1:
        # b = 0
        while b < cf.AMOUNT_LOOPS:
            options = webdriver.ChromeOptions()
            profile_path = f"user-data-dir={cf.local['userDataDir']}{b}"
            options.add_argument(profile_path)
            options.add_experimental_option(
                "excludeSwitches", ["enable-logging"]
            )

            options.add_extension("Cookie-Editor.crx")

            options.add_experimental_option(
                "prefs",
                {"profile.default_content_setting_values.notifications": 2},
            )

            print("------------------------------------------------------")
            print(f"[Thread {b}] - Running Path: Chrome Profile No.{b}")
            print("------------------------------------------------------")

            service = Service(cf.local["executablePath"])
            bot = webdriver.Chrome(options=options)
            wait = WebDriverWait(bot, 5)
            bot.maximize_window()

            bot.delete_all_cookies()

            print("Clear Cookies Chrome!")
            bot.get("https://www.tiktok.com")
            time.sleep(4)

            bot.delete_all_cookies()


            bot.get("https://www.tiktok.com")
            sleep(3)

            NoCos = input("Masukan Nomor Cookies: ")
            abc = input("Silahkan Login Akun Tiktok Dulu! Klik [ENTER] untuk lanjut! ")
            if abc == "":
                print("Get Cookies Now!")
                sleep(3)       

            # ====================== START GET COOKIES ==================== #

            pickle.dump(
                bot.get_cookies(),
                open(f"Cookies/cookies ({NoCos}).cookies", "wb"),
            )


            bot.get("https://www.tiktok.com")
            time.sleep(3)

            # ====================== END GET COOKIES ==================== #


            bot.quit()

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
