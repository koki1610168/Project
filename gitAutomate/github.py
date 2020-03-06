from selenium import webdriver
import os
import sys

repositoryName = str(sys.argv[1])

path = '/Users/hachimannoboruju/Documents/Python/Project/'
EMAIL = 'k.yahata1610168@gmail.com'
PASSWORD = '08220810Ak'
driver = webdriver.Chrome('/Users/hachimannoboruju/Documents/Python/Project/Selenium/chromedriver')

def createGitRepo():
    os.makedirs(path + repositoryName)
    driver.get('https://github.com/login')
    driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(EMAIL)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
    driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]').click()
    driver.get('https://github.com/new')
    driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(repositoryName)
    driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/button')

if __name__ == '__main__':
    createGitRepo()