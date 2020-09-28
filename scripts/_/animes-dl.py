from selenium import webdriver


class SuperAnimes:
	def __init__(self, driver):
		self.driver = driver
		self.url = 'https://www.superanimes.org/anime/hunter-x-hunter-2011/10115/baixar'

	def navigate(self):
		self.driver.get(self.url)


go = webdriver.Chrome()
sa = SuperAnimes(go)
sa.navigate()
