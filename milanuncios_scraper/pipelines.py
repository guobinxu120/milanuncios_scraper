# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import xlsxwriter
import os, csv
from collections import OrderedDict

class MilanunciosScraperPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        filepath = 'qq3.xlsx'
        if os.path.isfile(filepath):
            os.remove(filepath)
        workbook = xlsxwriter.Workbook(filepath)
        sheet = workbook.add_worksheet('eclairage-exterieur')
        data = spider.models
        # headers = spider.headers
        flag = True
        # headers = []
        print('---------------Writing in file----------------------')
        print('total row: ' + str(len(data)))

        for index, value in enumerate(data):
            if flag:
                for col, val in enumerate(value.keys()):
                    # headers.append(val)
                    sheet.write(index, col, val)
                flag = False
            for col, key in enumerate(value.keys()):
                sheet.write(index + 1, col, value[key])

            print('row :' + str(index))

        workbook.close()
    def process_item(self, item, spider):
        return item
