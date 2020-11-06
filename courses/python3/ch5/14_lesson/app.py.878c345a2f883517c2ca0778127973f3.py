from selenium import webdriver
from time import sleep


class FirefoxAuto:
    def __init__(self):
        # self.driver_path = "/usr/bin/geckodriver"
        self.options = webdriver.FirefoxOptions()
        # self.options.add_argument("user-data-dir=Profile")
        self.firefox = webdriver.Firefox()

    def click_sign_in(self):
        try:
            btn_sign_in = self.firefox.find_element_by_link_text("Sign in")
            # btn_sign_in = self.firefox.find_element_by_xpath(
            # "/html/body/div[1]/header/div/div[2]/div[2]/a[1]"
            # )
            btn_sign_in.click()
        except Exception as error:
            print(error)

    def insert_login(self):
        try:
            input_login = self.firefox.find_element_by_id("login_field")
            input_password = self.firefox.find_element_by_id("password")
            btn_login = self.firefox.find_element_by_name("commit")

            input_login.send_keys("USER")
            input_password.send_keys("PASSWORD")
            sleep(3)
            btn_login.click()

        except Exception as error:
            print(error)

    def click_profile(self):
        try:
            profile = self.firefox.find_element_by_css_selector(
                ".js-feature-preview-indicator-container"
            )
            profile.click()
        except Exception as error:
            print(error)

    def check_user(self, user):
        profile_link = self.firefox.find_element_by_class_name("user-profile-link")
        profile_link_html = profile_link.get_attribute("innerHTML")
        assert user in profile_link_html

    def click_logout(self):
        try:
            profile = self.firefox.find_element_by_css_selector(
                "button.dropdown-item:nth-child(2)"
            )
            profile.click()
        except Exception as error:
            print(error)

    def access(self, site):
        self.firefox.get(site)

    def exit_(self):
        self.firefox.quit()


if __name__ == "__main__":
    firefox = FirefoxAuto()
    firefox.access("https://github.com/")

    firefox.click_profile()
    firefox.click_logout()

    firefox.click_sign_in()
    firefox.insert_login()

    firefox.click_profile()
    firefox.check_user("USER")

    sleep(3)
    firefox.exit_()
