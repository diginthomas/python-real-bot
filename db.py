import sqlite3
import time

con = sqlite3.connect(".\database\database.db")
class Insert:
    def __init__(self,listings_price,listings_description,listings_url,listings_image):
        self.listings_price = listings_price
        self.listings_description = listings_description
        self.listings_url = listings_url
        self.listings_image = listings_image
    def insert(self):
        # zip function will make all the list the same size
        # getting the values of price, url and image 
        for i, j, k, z in zip(self.listings_price,self.listings_description,self.listings_url,self.listings_image):
            if (i.text == 'Please Contact'):
                continue
            con.execute("""INSERT INTO SCRAP(PRICE,DESCRIPTION,URL,IMAGES,DATE) VALUES (?, ?, ?, ?, ?);""", (float(i.text.replace('$','').replace(',','')), j.text, k.get('href'), z.get('src'),int(time.time())))
        con.commit()
        con.close()

class Drop:
    def __init__(self,table):
        self.table = table
    def drop(self):
        con = sqlite3.connect(".\database\database.db")
        con.execute("""DROP TABLE SCRAP;""")
        con.commit()
        con.close()

class Create:
    def __init__(self,table):
        self.table = table
    def create(self):
        con = sqlite3.connect(".\database\database.db")
        con.execute("""create table ?(
                    PRICE number(100,2),
                    DESCRIPTION varchar2(1000),
                    URL varchar2(10000),
                    IMAGES varchar2(10000));""", (self.table))
        con.commit()
        con.close()

class Select:
    def select():
        con = sqlite3.connect(".\database\database.db")
        # Here we can use SELECT or BETWEEN statemet to find the price that the user want? 
        get_from_table = con.execute("SELECT PRICE,DESCRIPTION,URL,IMAGES,DATE from SCRAP ORDER BY DATE DESC")
        for row in get_from_table:
            print("PRICE = ", row[0])
            print("DESCRIPTION = ",row[1])
            print("URL = ",row[2])
            print("IMAGES = ",row[3])
            print("DATE = ",row[4])
        con.close
