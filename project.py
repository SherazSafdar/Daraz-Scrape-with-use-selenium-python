from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create a list to store product details
products_list = []

# Create a dictionary to store product details
products_dict = {}

# Initialize the webdriver
driver = webdriver.Firefox()

# Navigate to the Daraz website
driver.get("https://www.daraz.pk/wow/i/pk/landingpage/flash-sale")

# Wait for the page to load
time.sleep(2)

# Define the scroll increment (in pixels)(speed)
scroll_increment = 250

# Get the initial scroll position
scroll_position = driver.execute_script("return window.pageYOffset;")

# Get the initial page height
page_height = driver.execute_script("return document.documentElement.scrollHeight")

# Scroll down the page slowly
while True:
    # Scroll down by the scroll increment
    driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
    time.sleep(0.5)

    # Update the scroll position
    scroll_position += scroll_increment

    # Check if the scroll position has reached the bottom of the page
    if scroll_position >= page_height:
        break

    # Check the new page height
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    # If the new page height is greater, update the page height
    if new_page_height > page_height:
        page_height = new_page_height




# Find the product elements
products = driver.find_elements(By.XPATH, '//*[@id="campaign-1689620400000"]/div/a')
# product_elements = driver.find_elements(By.CSS_SELECTOR, ".item-list-content a")

# Iterate over each product element and extract the details
for product in products:
    product_name = product.find_element("class name", "sale-title").text
    product_price = product.find_element("class name", "sale-price").text
    product_originprice = product.find_element("class name", "origin-price-value").text
    product_discount = product.find_element("class name", "discount").text
# Store product information in the dictionary
    products_dict[product_name] = {
        "price": product_price,
        "origin_price": product_originprice,
        "discount": product_discount}
    
     # Append the product details dictionary to the products_list
    products_list.append(products_dict)

# Print the dictionary containing the product details
print(products_dict)

# Close the browser
driver.quit()

