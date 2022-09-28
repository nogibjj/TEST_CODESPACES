import scrapy


class CveSpider(scrapy.Spider):
    name = 'cve'
    allowed_domains = ['cve.mitre.org']
    start_urls = ['http://cve.mitre.org/']

    def parse(self, response):
        pass
