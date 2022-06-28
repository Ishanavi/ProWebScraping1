from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/ishanavijain/Desktop/ProWebScraping/venv/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "distance", "mass", "radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr", attrs={"class"}):
        th_tags = tr_tag.find_all("th")
        temp_list = []
        for index, th_tag in enumerate(th_tags):
            if index == 0:
                temp_list.append(th_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(th_tag.contents[0])
                except:
                    temp_list.append("")
        star_data.append(temp_list)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()