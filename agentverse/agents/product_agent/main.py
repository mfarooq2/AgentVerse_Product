from .scraper import Scraper
from .analyzer import Analyzer
import unittest

class TestProductAgent(unittest.TestCase):
    def setUp(self):
        self.amazon_scraper = Scraper("https://www.amazon.com/")
        self.ebay_scraper = Scraper("https://www.ebay.com/")
        self.bestbuy_scraper = Scraper("https://www.bestbuy.com/")
        self.analyzer = Analyzer()

    def test_amazon_scraping(self):
        item = "laptop"
        name, price = self.amazon_scraper.scrape_amazon(item)
        self.assertNotEqual(name, "")
        self.assertNotEqual(price, "")

    def test_ebay_scraping(self):
        item = "computer"
        name, price = self.ebay_scraper.scrape_ebay(item)
        self.assertNotEqual(name, "")
        self.assertNotEqual(price, "")
    
    def test_bestbuy_scraping(self):
        item = "mouse"
        name, price = self.bestbuy_scraper.scrape_bestbuy(item)
        self.assertNotEqual(name, "")
        self.assertNotEqual(price, "")
    
    def test_get_single_product(self):
        item = "laptop"
        url = "https://www.amazon.com/"
        self.amazon_scraper = Scraper(url)
        name, price = self.amazon_scraper.get_single_product(url, item)
        self.assertNotEqual(name, "")
        self.assertNotEqual(price, "")

    def test_compare_products(self):
        products_data = []
        name_data = [
            {'name': "Laptop", 'price': "1200", 'site': "amazon"},
            {'name': "Computer", 'price': "1000", 'site': "ebay"},
            {'name': "Mouse", 'price': "1250", 'site': "bestbuy"},
        ]
        self.analyzer.get_all_products(name_data)
        self.analyzer.present_data()
        self.assertEqual(self.analyzer.compare_products(), {'name':"Computer", 'price':"1000"})
        
if __name__ == '__main__':
    unittest.main()
