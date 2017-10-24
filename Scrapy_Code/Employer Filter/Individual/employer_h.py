# -*- coding: utf-8 -*-
import scrapy


class Employer_hSpider(scrapy.Spider):
    name = "employer_h"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/companies/browse-h']

    def parse(self, response):
        self.log('I just visted: ' + response.url)
        urls = response.css('a._2Pu4qnm::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'employer_name': response.css('span::text')[27].extract(),
            'employer_info': response.css("div._24rF9oI::text").extract_first(),
            'employer_url': response.url
            }

