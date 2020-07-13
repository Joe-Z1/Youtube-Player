from selenium import webdriver
from time import sleep


class YoutubeBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def OpenPage(self):
        self.driver.get(
            "https://www.youtube.com/watch?v=BDf4fvubExc&list=RDBDf4fvubExc&index=1")

    def SkipButton(self):
        skip = self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[26]/div[2]/div[1]/a[2]").click()

    def PlayButton(self):
        play = self.driver.find_element_by_xpath(
            "//*[@id='movie_player']/div[29]/div[2]/div[1]/button").click()

    def PreviousButton(self):
        previous = self.driver.find_element_by_xpath(
            "//*[@id='movie_player']/div[29]/div[2]/div[1]/a[1]").click()

    def SkipAd(self):
        Skipad = self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div").click()

    def Current(self):
        current = self.driver.find_element_by_xpath(
            "//*[@id='container']/h1/yt-formatted-string")


bot = YoutubeBot()
bot.OpenPage()
