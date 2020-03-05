import sys
from selenium import webdriver


def studyOnUdemy():

    driver = webdriver.Chrome('./Selenium/chromedriver')
    driver.get('https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F')

    email_input = driver.find_element_by_xpath('//*[@id="email--1"]')
    email_input.send_keys(EMAIL)

    password_input = driver.find_element_by_xpath('//*[@id="id_password"]')
    password_input.send_keys(PASSWORD)

    log_in_button = driver.find_element_by_xpath('//*[@id="submit-id-submit"]')
    log_in_button.click()

    driver.get('https://www.udemy.com/home/my-courses/')

wanna_learn = str(input('Do you want to lean something new? (y / n)'))
if wanna_learn[0] == 'y' or wanna_learn[0] == 'Y':
    EMAIL = str(input('Email Adress: '))
    PASSWORD = str(input('Password: '))
    studyOnUdemy()

else:
    print('Ok... You are lazy')
