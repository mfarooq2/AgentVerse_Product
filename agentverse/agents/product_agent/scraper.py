import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.name = ""
        self.price = ""
        self.source = None
        self.soup = None

    def scrape_amazon(self, item):
      self.url = "https://www.amazon.com/s?k="
      self.source = requests.get(self.url+item, headers=self.headers)
      self.soup = BeautifulSoup(self.source.content, 'html.parser')
      name_tag = self.soup.find("h2", {"class":"a-size-base"})
      price_tag = self.soup.find("span", {'class': 'a-price-whole'})
      if name_tag:
        self.name = name_tag.text.strip()
      if price_tag:
        self.price = price_tag.text.strip()
      return self.name, self.price

    def get_product_info(self, tag):
        try:
            name_tag = self.soup.find("h2", {'class': "a-size-base"})
            if name_tag:
                self.name = name_tag.text.strip()
            price_tag = self.soup.find("span", {'class': 'a-price-whole'})
            if price_tag:
                self.price = price_tag.text.strip()
        except Exception as e:
            print(f'Error: {e}')
        return self.name, self.price
    
    def get_single_product(self, url="", item=""):
      try:
        self.source = requests.get(url, headers=self.headers)
        self.soup = BeautifulSoup(self.source.content, 'html.parser')
        return self.get_product_info(self.soup.find("span", {'class': 'a-price-whole'}))
      except Exception as e:
        print(f'Error: {e}')
        return "", ""
    
    def scrape_ebay(self, item):
      self.url = "https://www.ebay.com/sch/ebayadvsearch?_nkw="
      self.source = requests.get(self.url+item, headers=self.headers)
      self.soup = BeautifulSoup(self.source.content, 'html.parser')
      name_tag = self.soup.find("h3", {'itemprop': "name"})
      if name_tag:
        self.name = name_tag.text.strip()

      price_tag = self.soup.find("span", {'itemprop': 'price'})
      if price_tag:
        self.price = price_tag.text.strip()
      return self.name, self.price

    def scrape_bestbuy(self, item):
      self.url = "https://www.bestbuy.com/s?k="
      self.source = requests.get(self.url+item, headers=self.headers)
      self.soup = BeautifulSoup(self.source.content, 'html.parser')
      name_tag = self.soup.find("span", {'class': "product-title"})
      if name_tag:
        self.name = name_tag.text.strip()
      price_tag = self.soup.find("span", {'class': 'price'})
      if price_tag:
        self.price = price_tag.text.strip()
      return self.name, self.price

    def get_product_info(self, tag):
        try:
            if tag.name == "h2" and tag['class'][0] == 'a-size-base':
                self.name = tag.text.strip()
            price_tag = self.soup.find("span", {'class': 'price'})
            if price_tag:
                self.price = price_tag.text.strip()
        except Exception as e:
            print(f'Error: {e}')
        return self.name, self.price
