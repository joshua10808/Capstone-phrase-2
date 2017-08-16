# -*- coding: utf-8 -*-
import scrapy


class SeekinfoSpider(scrapy.Spider):
    name = "seekinfo"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/jobs-in-information-communication-technology']

    def parse(self, response):
        self.log('I just visted: ' + response.url)

        for info in response.css('div.oFneB7F'):
            item = {
                'job_name': info.css('a._1OFaluu > span::text').extract_first(),
                'company': info.css('p.HR3XFoW > span::text')[1].extract(),
                'outline': info.css('p._2GUG24P > span::text').extract_first(),
                'location': info.css('a._1_qWEhr::text').extract_first(),
                }
            yield item
        # follow pagination link
        next_page_url = response.css('a._1XIONbW::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
