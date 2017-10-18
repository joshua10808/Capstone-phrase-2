# -*- coding: utf-8 -*-
import scrapy


class FullEmployerSpider(scrapy.Spider):
    name = "full_employer"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/companies/browse-a',
                  'https://www.seek.com.au/companies/browse-b',
                  'https://www.seek.com.au/companies/browse-c',
                  'https://www.seek.com.au/companies/browse-d',
                  'https://www.seek.com.au/companies/browse-e',
                  'https://www.seek.com.au/companies/browse-f',
                  'https://www.seek.com.au/companies/browse-g',
                  'https://www.seek.com.au/companies/browse-h',
                  'https://www.seek.com.au/companies/browse-i',
                  'https://www.seek.com.au/companies/browse-j',
                  'https://www.seek.com.au/companies/browse-k',
                  'https://www.seek.com.au/companies/browse-l',
                  'https://www.seek.com.au/companies/browse-m',
                  'https://www.seek.com.au/companies/browse-n',
                  'https://www.seek.com.au/companies/browse-o',
                  'https://www.seek.com.au/companies/browse-p',
                  'https://www.seek.com.au/companies/browse-q',
                  'https://www.seek.com.au/companies/browse-r',
                  'https://www.seek.com.au/companies/browse-s',
                  'https://www.seek.com.au/companies/browse-t',
                  'https://www.seek.com.au/companies/browse-u',
                  'https://www.seek.com.au/companies/browse-v',
                  'https://www.seek.com.au/companies/browse-w',
                  'https://www.seek.com.au/companies/browse-x',
                  'https://www.seek.com.au/companies/browse-y',
                  'https://www.seek.com.au/companies/browse-z',
                  'https://www.seek.com.au/companies/browse-0']

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

