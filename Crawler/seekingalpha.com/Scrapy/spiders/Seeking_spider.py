import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import json

class SeekingSpiderSpider(scrapy.Spider):
    name = 'Seeking_spider'
    allowed_domains = ['seekingalpha.com']
    start_urls = ['https://seekingalpha.com/login']
    custom_settings = { 'DOWNLOAD_DELAY': 2 }

    loginData = {
        'slugs[]': "",
        'rt': "",
        'user[url_source]': 'https://seekingalpha.com/account/login',
        'user[location_source]': 'orthodox_login',
        'user[email]': 'pipi@onetka.pl',
        'user[password]': 'kickic1975'
    }
     
    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response = response,
            formdata = self.loginData,
            formid = 'orthodox_login',
            callback = self.verify_login
            )

    def verify_login(self, response):
        pass
    #    return self.make_initial_requests()
