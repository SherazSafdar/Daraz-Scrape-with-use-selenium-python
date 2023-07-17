from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a dictionary to store product details
products_dict = {}

# Initialize the webdriver
driver = webdriver.Firefox()

# Navigate to the Daraz website
driver.get("https://www.daraz.pk/#hp-flash-sale")

# Wait for the page to load
time.sleep(2)

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Scroll multiple times to load more products (if required)
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find the product elements
product_elements = driver.find_elements("class name", "c1_t2i")

# Iterate over each product element and extract the details
for product_element in product_elements:
    product_name = product_element.find_element("class name", "c16H9d").text
    product_price = product_element.find_element("class name", "c13VH6").text
    products_dict[product_name] = product_price

# Print the dictionary containing the product details
print(products_dict)

# Close the browser
driver.quit()

