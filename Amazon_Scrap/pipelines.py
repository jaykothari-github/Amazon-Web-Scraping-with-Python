# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class AmazonScrapPipeline:

    def __init__(self):
        self.connect()
        self.create_table()

    def connect(self):
        self.conn = sqlite3.connect('Database.sqlite')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('DROP TABLE IF EXISTS Amazon')
        self.cur.execute("""CREATE TABLE Amazon (
    Title VARCHAR(128),
    price VARCHAR(128),
    img VARCHAR
)""")


    def process_item(self, item, spider):
        
        self.insert_data(item)
        self.conn.commit()

        return item

    def insert_data(self,item):
        self.cur.execute('INSERT INTO Amazon VALUES (?,?,?)',(item['title'],item['price'],item['img']))
