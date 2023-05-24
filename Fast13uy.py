from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import os

# Launch the Firefox browser driver
options = webdriver.ChromeOptions()

# Ignore unnecessary logs
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(chrome_options=options)

# Maximize the browser window



# Login to Taobao by providing username and password
def login():
    # Open Taobao website
    driver.get("https://www.taobao.com")

    # Find the text and click on the login link
    if driver.find_element(By.LINK_TEXT, "亲，请登录"):
        driver.find_element(By.LINK_TEXT, "亲，请登录").click()

    print("Please complete the QR code scan within 20 seconds")
    time.sleep(20)


def buy(buytime):
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(1)
    driver.maximize_window()
    # Click on the select all button in the shopping cart
    if driver.find_element(By.ID, "J_SelectAll1"):
        driver.find_element(By.ID, "J_SelectAll1").click()
    time.sleep(3)
    now = datetime.datetime.now()
    print('Login successful:', now.strftime('%Y-%m-%d %H:%M:%S.%f'))
    if isinstance(buytime, str):
        buytime = datetime.datetime.strptime(buytime, '%Y-%m-%d %H:%M:%S.%f')
    while True:
        now = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), '%Y-%m-%d %H:%M:%S.%f')
        if now >= buytime:
            try:
                # Click on the checkout button
                if driver.find_element(By.ID, "J_Go"):
                    driver.find_element(By.ID, "J_Go").click()
                    print("Checkout successful")
                    print("Checkout time (after clicking the button, before entering the order submission page):", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                    break
            except:
                # print("not found J_GO.")
                pass
        # print(now)
        time.sleep(0.01)
    submit(buytime)


def buy_reborn(buytime):
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(0.5)
    if driver.find_element(By.ID, "J_SelectAll1"):
        driver.find_element(By.ID, "J_SelectAll1").click()
    else:
        buy_reborn(buytime)
    time.sleep(0.5)
    now = datetime.datetime.now()
    print('Login successful:', now.strftime('%Y-%m-%d %H:%M:%S.%f'))
    if isinstance(buytime, str):
        buytime = datetime.datetime.strptime(buytime, '%Y-%m-%d %H:%M:%S.%f')
    while True:
        now = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), '%Y-%m-%d %H:%M:%S.%f')
        if now >= buytime:
            try:
                # Click on the checkout button
                if driver.find_element(By.ID, "J_Go"):
                    driver.find_element(By.ID, "J_Go").click()
                    print("Checkout successful")
                    print("Checkout time (after clicking the button, before entering the order submission page):", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                    break
            except:
                # print("not found J_GO.")
                pass
        # print(now)
        time.sleep(0.01)
    submit(buytime)


def submit(buytime):
    while True:
        try:
            if driver.find_element(By.LINK_TEXT, '提交订单'):
                driver.find_element(By.LINK_TEXT, '提交订单').click()
                now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                print("Successful purchase time: %s" % now1)
                break
        except:
            print("Trying to submit the order again")
            try:
                can_not_buy_element = driver.find_element(By.XPATH, "//*[contains(text(), '以下宝贝已不能购买，请通过')]")
                print("Find sign. Repeating...")
                # driver.back()
                driver.back()
                break
            except:
                time.sleep(0.01)
    buy_reborn(buytime)


if __name__ == "__main__":
    buytime = input("input the target time, format like '2023-05-24 10:02:01.000000':")
    # Login
    login()
    # Set the purchase time
    buy(buytime)
    os.system('pause')
