from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# options = Options()
# options.add_argument('start-maximized')
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()
# driver.maximize_window()
driver.set_window_size(300, 300)
driver.get('https://www.google.com/')
driver.quit()
