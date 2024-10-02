import sqlite3
import requests
from bs4 import BeautifulSoup
from db import Insert
from db import Select
import time

# URL to scrape (you may need to update this)
url = "https://www.kijiji.ca/b-house-for-sale/mississauga-peel-region/c35l1700276?sort=dateDesc&radius=5.0&address=Mississauga%2C+ON+L4Z+2Y8&ll=43.5996912%2C-79.6384557"

# Send a GET request to the website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'xml')

    # Example of how to search for house listings (you'll need to inspect the site to get the right tags/classes)
    listings_price = soup.find_all("p", {"data-testid": "listing-price"})  # This might vary based on actual HTML
    listings_url = soup.find_all("a", {"data-testid":"listing-link"})
    listings_image = soup.find_all("img",{"data-testid":"listing-card-image"})
    insert = Insert(listings_price,listings_url,listings_image)
    insert.insert()
    
    select = Select
    select.select()

