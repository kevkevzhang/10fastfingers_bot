# This is a sample Python script.
import time
from selenium import webdriver

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.chrome.webdriver import WebDriver



def type():
    # Use a breakpoint in the code line below to debug your script.
    driver = webdriver.Chrome('/Users/kevinzhang/chromedriver')    # Optional argument, if not specified will search path.
    driver.get('https://10fastfingers.com/typing-test/english/');
    time.sleep(10)  # Let the user actually see something!

    # //*[@id="row1"]/span[1]
    # path = '/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span['
    # path_cat = ']'
    path = '//*[@id="row1"]/span['
    path_cat = ']'
    input = driver.find_element_by_id('inputfield')
    for x in range(1,300):
        fullpath = path + str(x) + path_cat
        search_box = driver.find_element_by_xpath(fullpath)
        input.send_keys(search_box.text)
        print(search_box.text)
        input.send_keys(' ')
        time.sleep(.1)

    time.sleep(100)  # Let the user actually see something!


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    type()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
