from selenium import webdriver
from time import sleep


class FirefoxAuto:
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.firefox = webdriver.Firefox()

    def access(self, site):
        self.firefox.get(site)

    def click_sign_in(self):
        try:
            btn_sign_in = self.firefox.find_element_by_link_text("SIGN IN")
            btn_sign_in.click()
        except Exception as error:
            print("error:", error)

    def insert_login(self):
        try:
            input_login = self.firefox.find_element_by_css_selector("#identifierId")
            btn_login = self.firefox.find_element_by_css_selector(".VfPpkd-RLmnJb")

            input_login.send_keys("@gmail.com")
            sleep(3)
            btn_login.click()
        except Exception as error:
            print("error:", error)

    def exit_(self):
        self.firefox.quit()


if __name__ == "__main__":
    firefox = FirefoxAuto()
    firefox.access(
        "https://www.youtube.com/playlist?list=PL_Hkwbp3Lq5YYxrX6hzlsJ633GWd4Npo2"
    )

    firefox.click_sign_in()
    firefox.insert_login()

    # firefox.exit_()
