#https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

reviews = []
#Opens browser
url = "https://www.niche.com/colleges/bucks-county-community-college/reviews/"#"https://www.niche.com/colleges/penn-state/reviews/"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)

#Gets the number of pages
number_of_pages_reviews = driver.find_elements_by_xpath('//div[@class="pagination__pages__total"]')
actual_nopr = re.sub("[^0-9 ]",'', number_of_pages_reviews[0].text)[2:]

#Goes through pages
reviews += list(map(lambda x: x.text.encode("utf8"),driver.find_elements_by_xpath('//div[@itemprop="reviewBody"]'))) #reviews from the current page
#mapping the code to text: http://book.pythontips.com/en/latest/map_filter.html
#Encode gotten from https://stackoverflow.com/questions/40619675/unicodeencodeerror-ascii-codec-cant-encode-character-u-u2019-in-position-6
for n in range((int(actual_nopr)-1)):
#Extract data: https://www.youtube.com/watch?v=zjo9yFHoUl8
    driver.execute_script("window.scrollTo(0, 1366)")
    next_button = driver.find_element_by_xpath('//li[@class="pagination__next"]') #go to the next page
    next_button.click()
    new_reviews = driver.find_elements_by_xpath('//div[@itemprop="reviewBody"]') #reviews from the current page
    reviews += list(map(lambda x: x.text.encode("utf8"),driver.find_elements_by_xpath('//div[@itemprop="reviewBody"]')))

num_of_review = len(reviews)
for i in range(num_of_review):
    print(reviews[i])

text_data = ' '.join(reviews)
driver.close()

#Write data to a file: https://www.w3schools.com/python/python_file_write.asp
file_creator = open("school_data.txt", "w")
file_creator.write(text_data)
