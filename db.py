import sqlite3

class ConnectDB:
    def __init__(self,con):
        self.con = con
    def connect(self):
        self.con = sqlite3.connect(".\database\database.db")
    def commit(self):
        self.con.commit()
    def close(self):
        self.con.close()

class Insert:

    def __init__(self,listings_price,listings_url,listings_image):
        self.listings_price = listings_price
        self.listings_url = listings_url
        self.listings_image = listings_image
    
    def insert(self):
        ConnectDB 
        for i, j, k in zip(self.listings_price,self.listings_url,self.listings_image):
            print(i.text,j.get('href'),j.text,k.get('src'))
            self.cun.execute("""
                INSERT INTO SCRAP(PRICE,URL,DESCRIPTION) VALUES
                (?, ?, ?);""", (1,1,1))

# cur.execute('''DROP TABLE SCRAP''')

# cur.execute('''CREATE TABLE SCRAP
#          (PRICE         INT(50,2)    NOT NULL,
#          URL            VARCHAR2(500)     NOT NULL,
#          DESCRIPTION    VARCHAR2(500));''')

class Select:
    def select(self):
        get_from_table = self.con.execute("SELECT PRICE,URL,DESCRIPTION from SCRAP")
        for row in get_from_table:
            print("PRICE = ", row[0])
            print("URL = ",row[1])
            print("DESCRIPTION = ",row[2])
