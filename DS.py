from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

videoFileName = "Videolist.txt"

videoFile = open(videoFileName)
listVideo = videoFile.readlines()

videoIndex = 0

browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get("https://www.y2mate.com/vi12/youtube-mp3")

link = browser.find_element_by_id("txt-url")
link.send_keys(listVideo[videoIndex])
sleep(1)

dowload = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/div[2]/button[1]")
dowload.click()
sleep(1)

dowloadmp3 = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/a")
dowloadmp3.click()
