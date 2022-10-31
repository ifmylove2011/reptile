from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(driver_path)

# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)


options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(driver_path,chrome_options=options)

driver.get("http://www.baidu.com")
baidu = driver.find_element_by_id("kw")
baidu.send_keys("www")
baidu.send_keys(Keys.RETURN)
print(driver.page_source)