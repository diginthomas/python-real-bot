import requests
from bs4 import BeautifulSoup
from db import Insert
from db import Select
from bot.commands import location
# from db import Drop
# from db import Create

# URL to scrape (you may need to update this)
url = "https://www.kijiji.ca/b-house-for-sale/{location}/c35l1700276?sort=dateDesc&price={min}__{max}"

# Send a GET request to the website
response = requests.get(url)

print(location)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'xml')

    # Example of how to search for house listings (you'll need to inspect the site to get the right tags/classes)
    listings_price = soup.find_all("p", {"data-testid": "listing-price"})  # This might vary based on actual HTML
    listings_url = soup.find_all("a", {"data-testid":"listing-link"})
    listings_description = soup.find_all("a", {"class":"sc-24a49435-0 eocwml"})
    listings_image = soup.find_all("img",{"data-testid":"listing-card-image"})
    listings_date = soup.find("p", {"data-testid": "listing-date"})
    # time_published = listings_date.text
    print(listings_date)

    # insert = Insert(listings_price,listings_description,listings_url,listings_image,listings_date)
    # insert.insert()
    
    # select = Select
    # select.select()

    # drop = Drop("SCRAP")
    # drop.drop()

    # create = Create("SCRAP")
    # create.create()

