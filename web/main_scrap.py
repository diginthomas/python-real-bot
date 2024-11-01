import requests
from bs4 import BeautifulSoup
from .db import Insert
from .db import Select


class Main:
    def __init__(self,location,budget):
        self.location = location
        self.budget = budget
        # URL to scrape (you may need to update this)
    def findList(self):
        url = "https://www.kijiji.ca/b-house-for-sale/{self.location}/c35l1700276?sort=dateDesc&radius=5.0&price=0__{self.budget}address={self.location}"

        # Send a GET request to the website
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'xml')

            # Example of how to search for house listings (you'll need to inspect the site to get the right tags/classes)
            listings_price = soup.find_all("p", {"data-testid": "listing-price"})  # This might vary based on actual HTML
            listings_location = soup.find_all("p", {"data-testid": "listing-location"})
            listings_url = soup.find_all("a", {"data-testid":"listing-link"})
            listings_description = soup.find_all("a", {"class":"sc-24a49435-0 eocwml"})
            listings_image = soup.find_all("img",{"data-testid":"listing-card-image"})

            # print(listings_description,listings_image,listings_location,listings_price,listings_url)

            insert = Insert(listings_price,listings_location,listings_description,listings_url,listings_image,self.location,self.budget)
            insert.insert()
            
            select = Select
            select.select()

            # drop = Drop("SCRAP")
            # drop.drop()

            # create = Create("SCRAP")
            # create.create()
