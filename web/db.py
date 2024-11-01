import sqlite3
import time

<<<<<<< HEAD
con = sqlite3.connect(".\database\database.db")
class Insert:
    def __init__(self,listings_price,listings_description,listings_url,listings_image):
=======
# con = sqlite3.connect(".\web\database\database.db")
class Insert:
    def __init__(self,listings_price,listings_location,listings_description,listings_url,listings_image,location,budget):
>>>>>>> d7c5fe52c6be1eb370fca57b430bf7fbbb82e972
        self.listings_price = listings_price
        self.listings_location = listings_location
        self.listings_description = listings_description
        self.listings_url = listings_url
        self.listings_image = listings_image
<<<<<<< HEAD
=======
        self.location = location
        self.budget = budget
>>>>>>> d7c5fe52c6be1eb370fca57b430bf7fbbb82e972
    def insert(self):
        con = sqlite3.connect(".\web\database\database.db")
        # zip function will make all the list the same size
        # getting the values of price, url and image 
<<<<<<< HEAD
        for i, j, k, z in zip(self.listings_price,self.listings_description,self.listings_url,self.listings_image):
            if (i.text == 'Please Contact'):
                continue
            con.execute("""INSERT INTO SCRAP(PRICE,DESCRIPTION,URL,IMAGES,DATE) VALUES (?, ?, ?, ?, ?);""", (float(i.text.replace('$','').replace(',','')), j.text, k.get('href'), z.get('src'),int(time.time())))
=======
        for i, l, j, k, z in zip(self.listings_price,self.listings_location,self.listings_description,self.listings_url,self.listings_image):
            if (i.text == 'Please Contact' or l.text != self.location):
                continue
            con.execute("""INSERT INTO SCRAP(PRICE,LOCATION,DESCRIPTION,URL,IMAGES,DATE) VALUES (?, ?, ?, ?, ?, ?);""", (float(i.text.replace('$','').replace(',','')),l.text, j.text, k.get('href'), z.get('src'),int(time.time())))
>>>>>>> d7c5fe52c6be1eb370fca57b430bf7fbbb82e972
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
        # Here we can use SELECT or BETWEEN statemet to find the price that the user want? 
<<<<<<< HEAD
<<<<<<< HEAD:db.py
        get_from_table = con.execute("SELECT PRICE,DESCRIPTION,URL,IMAGES,DATE from SCRAP GROUP BY DATE ORDER BY DATE DESC")

=======
        get_from_table = con.execute("SELECT PRICE,DESCRIPTION,URL,IMAGES,DATE from SCRAP")
>>>>>>> f1b23b6eaecb9e6be4be71ae17a674f76a398e33:web/db.py
        for row in get_from_table:
            # print("PRICE = ", row[0])
            # print("DESCRIPTION = ",row[1])
            # print("URL = ",row[2])
            # print("IMAGES = ",row[3])
            print("DATE = ",row)
            print("")
=======
        get_from_table = con.execute("SELECT PRICE,LOCATION,DESCRIPTION,URL,IMAGES,DATE from SCRAP")
        for row in get_from_table:
            print("PRICE = ", row[0])
            print("LOCATION = ", row[1])
            print("DESCRIPTION = ",row[2])
            print("URL = ",row[3])
            print("IMAGES = ",row[4])
            print("DATE = ",row[5])
>>>>>>> d7c5fe52c6be1eb370fca57b430bf7fbbb82e972
        con.close
