from selenium import webdriver

from selenium.webdriver.common.keys import Keys

#driver = webdriver.chrome(executable_path ="/Users/sdeshnoo/desktop")
# To get executable path: `which chromedriver` 
driver = webdriver.Chrome(executable_path = "/usr/local/bin/chromedriver")

driver.get('HTTP://www.python.org')

assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("VANITHA")
elem.send_keys(Keys.RETURN)

assert "No result found VANITH" not in driver.page_source