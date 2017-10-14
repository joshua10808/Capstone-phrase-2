# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

class NetworkingSpider(scrapy.Spider):
    name = "networking"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/jobs-in-information-communication-technology/in-All-Brisbane-QLD?subclassification=6289%2C6293%2C6300']

    def parse(self, response):
        self.log('I just visted: ' + response.url)

        for info in response.css('article.e5uyowV'):
            item = {
                'job_name': info.css('a._1EkZJQ7 > span::text').extract_first(),
                'outline': info.css('span.bl7UwXp > span::text').extract_first(),
                'info_url': info.css('a._1EkZJQ7::attr(href)').extract_first(),
                'company': info.css('span[data-automation=jobAdvertiser]::text').extract_first(),
                }
            yield item
            
        # follow pagination link
        next_page_url = response.css('a._1XIONbW::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
