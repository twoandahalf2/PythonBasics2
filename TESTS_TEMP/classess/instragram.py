from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class GaryVee:

    username = 'vladimirkolev'
    password = 'Danev123$'
    hashtags = ['travel', 'explore', 'Amsterdam']
    links= []

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.login()
        self.hustle()

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)
        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(1)
        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(30)

    def hustle(self):
        self.getTopPost()

    def getTopPost(self):
        for hashtag in self.hashtags:
            self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
            time.sleep(2)
            links= self.browser.find_element_by_tag_name('a')
            print(links)
            condition = (lambda link_s: '.com/p/' in link_s.get_attribute('href'))
            valid_links = list(filter(condition, links))
            for i in range(0,2):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)


garyvee = GaryVee()