# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.crawler import CrawlerProcess

try:
    os.remove("items.json")
except OSError:
    pass

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract(),
            }
            yield item
        #follow pagination link
        next_page_url=response.css('li.next>a::attr(href)').extract_first()
        if next_page_url:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(QuotesSpider)
    process.start() # the script will block here until the crawling is finished