from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class DataScraper:
    def __init__(self, url):
        self.url = url

    def scrape_data(self):
        response = requests.get(self.url, verify=False)
        soup = BeautifulSoup(response.content, "html.parser")
        body = soup.find("table", class_="tdcj_table")
        rows = body.find_all("tr")
        return rows