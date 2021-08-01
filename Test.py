from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class NetpeakTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testTask(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://netpeak.ua/");

        def pool(num):
            tabs = driver.window_handles
            driver.switch_to_window(tabs[num])

        def btnLog(id, keys):
            btn = driver.find_element_by_id(id)
            btn.clear()
            btn.send_keys(keys)
        
        driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]').click()
        time.sleep(1)
        driver.find_element_by_link_text('Команда').click()
        time.sleep(1)
        wait = WebDriverWait(driver,10)
        wait.until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Стать частью команды'))
        ).click()
        pool(1)
        btnGreen = driver.find_element_by_link_text('Я хочу работать в Netpeak')
        btnGreenPush = EC.element_to_be_clickable(btnGreen) #Проверяем можно ли нажать на кнопку "Я хочу работать в Netpeak".
        pool(0)
        driver.find_element_by_class_name('custom-link').click()
        pool(2)
        btnLog('login', 'Boba')
        btnLog('password', 'Aboba')
        btnDis = driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button/span')
        btnDisPush = EC.element_to_be_clickable(btnDis)
        btnAgree = driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/md-checkbox/div[1]').click()
        time.sleep(1)
        btnDis.click()
        bulka = EC.visibility_of_element_located((By.XPATH, '/md-toast/div')) # Находим табличку "Неправильный логин или пароль"
        logRed = driver.find_elements_by_class_name('input-container md-input-invalid') #Находим поля с красной подсвеченные красным цветом
        time.sleep(60)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()