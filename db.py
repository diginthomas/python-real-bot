import sqlite3
con = sqlite3.connect(".\database\database.db")
class Insert:
    def __init__(self,listings_price,listings_url,listings_image):
        self.listings_price = listings_price
        self.listings_url = listings_url
        self.listings_image = listings_image
    def insert(self):
        # zip function will make all the list the same size
        # getting the values of price, url and image 
        for i, j, k in zip(self.listings_price,self.listings_url,self.listings_image):
            print(i.text,j.get('href'),j.text,k.get('src'))
            con.execute("""INSERT INTO SCRAP(PRICE,URL,DESCRIPTION) VALUES (?, ?, ?);""", (i.text, j.get('href'), k.get('src')))
        con.commit()
        con.close()

class Select:
    def select():
        con = sqlite3.connect(".\database\database.db")
        get_from_table = con.execute("SELECT PRICE,URL,DESCRIPTION from SCRAP")
        for row in get_from_table:
            print("PRICE = ", row[0])
            print("URL = ",row[1])
            print("DESCRIPTION = ",row[2])
        con.commit()
        con.close
