# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv

class AmazonPipeline:
    def open_spider(self, spider):
        self.file = open('amazon.csv', 'w', newline='',encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(('product_name','price','ratings','rank_text'))

    def close_spider(self, spider):
        self.file.close()


    def process_item(self, item, spider):
        #Clean data
        prices = [p.strip() for p in item['price'] if p.strip()]
        names = [n.strip() for n in item['product_name'] if n.strip() and n.strip().lower()!= 'best sellers']
        ratings = [rat.strip() for rat in item['ratings'] if rat.strip()]
        ranks = [r.strip() for r in item['rank_text'] if r.strip()]

        length = min(len(prices),len(names), len(ratings), len(ranks))
        for i in range(length):
            self.writer.writerow([prices[i],names[i],ratings[i],ranks[i]])

        return item

        return item
