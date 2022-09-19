from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("/Users/greeniewu/Dropbox/Mac/Desktop/PythonTesting/Class127/Project127/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    planet_data = []
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("tr",attrs={"class","wikitable sortable jquery-tablesorter"}):
        li_tags = ul_tag.find_all("td")
        temp = []
        for index,li_tag in enumerate(li_tags):
            if index == 0:
                temp.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp.append(li_tag.contents[0])
                except:
                    temp.append("")

        planet_data.append(temp)
            #To go to next page
        browser.find_element(By.XPATH,value = '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            #browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Scraper1.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()

