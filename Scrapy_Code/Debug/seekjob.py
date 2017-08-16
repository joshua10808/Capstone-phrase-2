# -*- coding: utf-8 -*-
import scrapy


class SeekjobSpider(scrapy.Spider):
    name = "seekjob"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/jobs-in-information-communication-technology']

    def parse(self, response):
        self.log('I just visted: ' + response.url)
        urls = response.css('a._1OFaluu::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
            
        # follow pagination link
        next_page_url = response.css('a._1XIONbW::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        yield {
            'info': response.css('div.templatetext').extract_first()
            }
