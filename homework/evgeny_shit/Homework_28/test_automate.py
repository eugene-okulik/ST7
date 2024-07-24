from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")
driver.implicitly_wait(5)

inp = driver.find_element(By.ID, "id_text_string")
inp.send_keys("some_text")
inp.submit()

# Явное ожидание, пока элемент не станет видимым
wait = WebDriverWait(driver, 10)
tex = wait.until(ec.visibility_of_element_located((By.ID, "result-text")))

result_text = tex.text
print(result_text)

driver.close()
