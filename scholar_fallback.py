from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_scholar(query):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://scholar.google.com/scholar?q={query}")
    time.sleep(3)

    papers = []
    results = driver.find_elements(By.CLASS_NAME, "gs_r")[:3]

    for r in results:
        title = r.find_element(By.TAG_NAME, "h3").text
        link = r.find_element(By.TAG_NAME, "a").get_attribute("href")
        papers.append({"title": title, "link": link})

    driver.quit()
    return papers
