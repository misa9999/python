from selenium import webdriver
from time import sleep


class FirefoxAuto:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.firefox = webdriver.Firefox()
        self.temp_links = []
        self.eps = []

    def get_links(self):
        with open("links.txt", "r") as links:
            for link in links:
                self.temp_links.append(link.strip())

    def access(self):
        temp = []
        for link in self.temp_links:
            self.firefox.get(link)
            sleep(3)

            for a in self.firefox.find_elements_by_xpath(".//a"):
                temp.append(a.get_attribute("href"))
                self.eps.append(temp[-7])

        for ep in self.eps:
            print(ep)

    def exit_(self):
        self.firefox.quit()


if __name__ == "__main__":
    firefox = FirefoxAuto()
    firefox.get_links()
    firefox.access()

    firefox.exit_()


