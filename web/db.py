import sqlite3
import time

class Insert:
    def __init__(self,listings_price,listings_location,listings_description,listings_url,listings_image,location,budget,city):
        self.listings_price = listings_price
        self.listings_location = listings_location
        self.listings_description = listings_description
        self.listings_url = listings_url
        self.listings_image = listings_image
        self.location = location
        self.budget = budget
        self.city = city
    def insert(self):
        con = sqlite3.connect(".\web\database\database.db")
        # zip function will make all the list the same size
        # getting the values of price, url, image, location, description and images 
        cityCap = self.city.capitalize()
        for i, l, j, k, z in zip(self.listings_price,self.listings_location,self.listings_description,self.listings_url,self.listings_image):
            print(f"--------------------->{l.text}<------------------------")
            print(f"#####################>{cityCap}<#######################")
            # If the value of i.text contains 'Please Contact' or l.text does not contain the value of the variable 'cityCap' will jump to the next iteration
            if (i.text == 'Please Contact' or cityCap not in l.text):
                continue
            con.execute("""INSERT INTO SCRAP(PRICE,LOCATION,DESCRIPTION,URL,IMAGES,DATE) VALUES (?, ?, ?, ?, ?, ?);""", (float(i.text.replace('$','').replace(',','')),l.text, j.text, k.get('href'), z.get('src'),int(time.time())))
        con.commit()
        con.close()

class Drop:
    def __init__(self,table):
        self.table = table
    def drop(self):
        con = sqlite3.connect(".\web\database\database.db")
        con.execute("""DROP TABLE SCRAP;""")
        con.commit()
        con.close()

class Create:
    def __init__(self,table):
        self.table = table
    def create(self):
        con = sqlite3.connect(".\web\database\database.db")
        con.execute("""create table ?(
                    PRICE number(50,2),
                    LOCATION varchar2(1000),
                    DESCRIPTION varchar2(1000),
                    URL varchar2(10000),
                    IMAGES varchar2(10000),
                    DATE date);""", (self.table))
        con.commit()
        con.close()

class Select:
    def select():
        con = sqlite3.connect(".\web\database\database.db")

        # store all the results of the listining inside of the below list to be called after in the return statement
        results = []

        get_from_table = con.execute("SELECT PRICE,LOCATION,DESCRIPTION,URL,IMAGES,DATE from SCRAP ORDER BY DATE desc LIMIT 5")
        for row in get_from_table:
            print("PRICE = ", row[0])
            print("LOCATION = ", row[1])
            print("DESCRIPTION = ",row[2])
            print("URL = ",row[3])
            print("IMAGES = ",row[4])
            print("DATE = ",row[5])
            print("")

            PRICE = row[0] 
            LOCATION = row[1]
            DESCRIPTION = row[2]
            URL = row[3]
            IMAGES = row[4]
            DATE = row[5]

            yield f"Price: {row[0]}\nLocation: {row[1]}\nDescription: {row[2]}\nURL: {row[3]}\nIMAGES: {row[4]}\nDATE: {row[5]}\n"

            
        con.close
