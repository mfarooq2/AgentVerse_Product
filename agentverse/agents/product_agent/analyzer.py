class Analyzer:
    def __init__(self):
        self.products_data = {}

    def add_product_data(self, site, product_name, product_price):
        if site not in self.products_data:
            self.products_data[site] = []
        self.products_data[site].append({"name":product_name, "price":product_price})

    def compare_products(self):
        best_product = {"name": "", "price": 0}
        for site, products in self.products_data.items():
            for product in products:
                if product['price']:
                    if best_product['price'] == 0:
                        best_product = product
                    else:
                        if best_product["price"] > product['price']:
                            best_product = product
        return best_product

    def analyze_data(self):
        """Analyzes the product data and provides insights."""
        pass  # Placeholder for now

    def present_data(self):
        """Presents the data in a user-friendly format."""
        pass  # Placeholder for now

    def present_products_data(self):
      for site, products in self.products_data.items():
          print(f"Site: {site}")
          for product in products:
              print(f"Name: {product['name']} - Price {product['price']}")
          print(f"Total products : {len(products)}")
          print("-----------------------")

    def get_all_products(self, name_data = []):
        for product_info in name_data:
            site = product_info['site']
            product_name = product_info['name']
            product_price = product_info['price']
            self.add_product_data(site, product_name, product_price)
            print(f'Site:{site} - Name:{product_name} - Price:{product_price}')

    def present_data(self):
      print("Presenting product comparison:")
      self.present_products_data()
      best_product = self.compare_products()
      print(f"Best product is: Name: {best_product['name']} - Price : {best_product['price']}")
