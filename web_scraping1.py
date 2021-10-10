from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(r"C:\Users\Ranveer Khokhar\Pro-128\venv\Scripts\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
headers = ["name", "distence", "mass", "radius"]
stars_data = []
def scrape():
    
   
    for i in range(10):
            soup = BeautifulSoup(browser.page_source, "html.parser")
            for tr_tag in soup.find_all("tr"):
                td_tags = tr_tag.find_all("td")
                temp_list = []
                for td_tags in enumerate(td_tags):
                    try:
                        temp_list.append(td_tags.contents[0])
                    except:
                        temp_list.append("")
                        
                stars_data.append(temp_list)
               
           


with open("stars_data.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)


scrape()