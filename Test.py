from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

class NetpeakTest():
    def pool(self, num):
        tabs = driver.window_handles
        driver.switch_to_window(tabs[num])

    def btnLog(self, id, keys):
        btn = driver.find_element_by_id(id)
        btn.clear()
        btn.send_keys(keys)

def main():
    netp = NetpeakTest()

    driver.maximize_window()
    driver.get("https://netpeak.ua/")
    driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]').click()
    driver.find_element_by_link_text('Команда').click()
    driver.find_element_by_partial_link_text('Стать частью команды').click()
    netp.pool(1)
    btnGreen = driver.find_element_by_link_text('Я хочу работать в Netpeak')
    btnGreenPush = EC.element_to_be_clickable(btnGreen)
    netp.pool(0)
    driver.find_element_by_class_name('custom-link').click()
    netp.pool(2)
    netp.btnLog('login', 'Boba')
    netp.btnLog('password', 'Aboba')
    btnDis = driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button/span')
    btnDisPush = EC.element_to_be_clickable(btnDis)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/md-checkbox/div[1]').click()
    btnDis.click()
    bulka = EC.visibility_of_element_located((By.XPATH, '/md-toast/div'))
    logRed = driver.find_elements_by_class_name('input-container md-input-invalid')

if __name__ == "__main__":
    main()