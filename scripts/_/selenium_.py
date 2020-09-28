from selenium import webdriver


url = 'https://www.superanimes.org/anime/hunter-x-hunter-2011/10115/baixar'

driver = webdriver.Chrome()
driver.get(url)

opc = driver.find_element_by_xpath('//*[@id="corpo"]/div/div[1]/div[3]/div[2]/div/a')
opc.click()