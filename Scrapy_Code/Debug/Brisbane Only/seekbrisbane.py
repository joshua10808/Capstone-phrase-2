# -*- coding: utf-8 -*-
import scrapy


class SeekbrisbaneSpider(scrapy.Spider):
    name = "seekbrisbane"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/jobs-in-information-communication-technology/in-All-Brisbane-QLD']

    def parse(self, response):
        self.log('I just visted: ' + response.url)
        urls = response.css('a._1EkZJQ7::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

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

    def parse_details(self, response):
        yield {
            'description': response.css('div.templatetext').extract_first(),
            'more_jobs_url': response.css('a._1-im0Ib::attr(href)').extract_first(),
            }
