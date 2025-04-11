# 293 : Automation/Testing
# - is way to automate process of testing software
# TODO: [Selenium]
# - is tool that automates browsers
# TODO: [Selenium with Python]
# - https://selenium-python.readthedocs.io/

# > pip install selenium
# > pip install webdriver-manager

import time

# TODO: GitHub Copilot ---------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_service = Service(ChromeDriverManager().install())
chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
chrome_browser.maximize_window()
# print(chrome_browser)

# Open a website
# chrome_browser.get('https://www.example.com')
# chrome_browser.get('https://pypi.org/project/selenium/')
# chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
chrome_browser.get("https://www.seleniumeasy.com/lander")
chrome_browser.implicitly_wait(2)
# time.sleep(2)

# Print the title of the page
print(chrome_browser.title)  # TODO: !!! empty title

# check if the title of the page is correct
id_getButtonBoxLink = chrome_browser.find_element(By.ID, "getButtonBoxLink")
print(id_getButtonBoxLink.text)
# print(id_getButtonBoxLink.get_attribute('innerHTML'))
# print('Get This Domain' in id_getButtonBoxLink.text)
assert (
    "Get This Domain" in id_getButtonBoxLink.text
)  # TODO: False throws AssertionError
assert (
    "Get This Domain" in chrome_browser.page_source
)  # TODO: True does not throw AssertionError

# print text of the element
class_trustarcBannerBody = chrome_browser.find_element(
    By.CLASS_NAME, "trustarc-banner-body"
)
print(class_trustarcBannerBody.text)

# print class of the element
id_topBanner = chrome_browser.find_element(By.ID, "topBanner")
print(id_topBanner.get_attribute("class"))

# click on the button
# id_getButtonBoxLink.click()

# TODO: get input and type text into it
# user_message = chrome_browser.find_element(By.ID, 'user-message')
# user_message.clear()
# user_message.send_keys('TEST MESSAGE')
# TODO: press button and check output message (text in element)

# TODo: find element by CSS selector
# show_message_button = chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')

# Close the browser
# chrome_browser.close()              # close current window
chrome_browser.quit()  # close all windows, all sessions


# TODO: Udemy UPDATED ----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service = Service(executable_path='./chromedriver')
# chrome_browser = webdriver.Chrome(service=service)

# button = chrome_browser.find_element_by_class_name('btn-default')
# button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# chrome_browser = webdriver.Chrome()
# chrome_browser.maximize_window()
# chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
# # This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()
# user_message = chrome_browser.find_element(By.ID, 'user-message')
# user_message.clear()
# user_message.send_keys('I AM EXTRA COOOOL')
# time.sleep(2)
# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# show_message_button.click()
# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text


# TODO: original code from saura -----------------------------------------------
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug 28 09:59:41 2020
#
# @author: saura
# """
# # from selenium import webdriver
# from selenium import webdriver
# edge_browser = webdriver.Edge('./msedgedriver.exe')
# # by default it searches the driver file in the path of Windows folder in the C drive
#
# # print(edge_browser)
# edge_browser.maximize_window()
# edge_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
#
# # print('Selenium Easy Demo' in edge_browser.title)
# # # we are checking here whether we are on the same page or not, if yes, it will return true
#
# assert 'Selenium Easy Demo' in edge_browser.title
# # # if the above is not true, assert will error out, otherwise code will continue
#
# show_message_button = edge_browser.find_element_by_class_name("btn-default")
# # the above command basically grabs this
# # <button type="button" onclick="showInput();" class="btn btn-default">Show Message</button>
#
# # we can find that button by CSS selector as well, using the below command
# # show_message_button = edge_browser.find_element_by_css_selector('#get-input > .btn')
#
#
# # print(button_text)
# # print(show_message_button.get_attribute('innerHTML'))
#
# assert 'Show Message' in edge_browser.page_source
#
# user_message = edge_browser.find_element_by_id("user-message")
# user_message.clear()    # to clear any previous message
# user_message.send_keys("Hello there!")     # selenium is typing the message
#
# show_message_button.click()     # selenium is clicking the button
#
# output_message = edge_browser.find_element_by_id('display')
#
# print('Hello there!' in output_message.text)
# print(output_message.get_attribute('innerHTML'))
#
# assert 'Hello there!' in output_message.text
#
# edge_browser.close()
# # edge_browser.quit()    # or we can use this
#
# '''
# sometimes the .close() , or .quit() method doesn't work. Because of some backgroud updates, etc.
# and each .close() closes one instance only. so in case more than 1 instance of the browser is opened by the
# program, we need to pass multiple .close()
#
# many websites identify the use of selenium and blocks the activity. "Verify you are not a robot" checkbox.
# so there is a way around that, we use 'Waits' so do things slowly, so the server thinks that this is being
# done by a human.
# '''
