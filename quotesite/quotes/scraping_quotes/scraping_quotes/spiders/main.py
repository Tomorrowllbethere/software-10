import scrapy
from scrapy.crawler import CrawlerProcess


def run_process(spider_class):
    process = CrawlerProcess()
    process.crawl(spider_class)
    process.start()