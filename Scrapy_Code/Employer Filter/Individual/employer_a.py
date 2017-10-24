# -*- coding: utf-8 -*-
import scrapy


class Employer_aSpider(scrapy.Spider):
    name = "employer_a"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/companies/browse-a']

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

