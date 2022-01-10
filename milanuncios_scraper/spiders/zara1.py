# -*- coding: utf-8 -*-
from scrapy import Spider, Request, FormRequest
import json, re, random, requests
from scrapy.utils.project import get_project_settings
from collections import OrderedDict

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class zaraSpider(Spider):
    name = "zara1"
    start_urls = [
                    # 'https://www.milanuncios.com/alquiler-de-apartamentos-en-barcelona/?fromSearch=1&dormd=2&dormh=9'
                  # 'https://www.milanuncios.com/alquiler-de-apartamentos-en-madrid/?fromSearch=1&dormd=2&dormh=9',
                  # 'https://www.milanuncios.com/alquiler-de-apartamentos-en-sevilla/?fromSearch=1&dormd=2&dormh=9'
                  'https://www.milanuncios.com/alquiler-de-apartamentos-en-valencia/?fromSearch=1&dormd=2&dormh=9',
                  # 'https://www.milanuncios.com/alquiler-de-apartamentos-en-tenerife/?fromSearch=1&dormd=2&dormh=9',
                  # 'https://www.milanuncios.com/alquiler-de-apartamentos-en-las_palmas/?fromSearch=1&dormd=2&dormh=9'
                  ]
    # domain1 = 'https://www.lowes.com/'
    models = []
    use_selenium = False
    count = 0
    pageIndex = 1
    totalpage= None
    # custom_settings = {
     #    'COOKIES_ENABLED': False
	# }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback= self.parse, meta={"next_count": 1})

    def parse(self, response):
        urls = response.xpath('//div[@class="aditem"]')
        for div in urls:
            item = OrderedDict()
            item['title'] = div.xpath('.//a[@class="aditem-detail-title"]/text()').extract_first()
            item['price'] = div.xpath('.//div[@class="aditem-price"]/text()').extract_first()
            # item['url'] = response.url
            item['description'] = div.xpath('.//div[@class="tx"]/text()').extract_first()

            # item['size'] = response.xpath('//div[@class="m2 tag-mobile"]/text()').extract_first()
            # item['bedrooms'] = response.xpath('//div[@class="dor tag-mobile"]/text()').extract_first()
            # item['bathrooms'] = response.xpath('//div[@class="ban tag-mobile"]/text()').extract_first()
            # item['price/m'] = response.xpath('//div[@class="pm2 tag-mobile"]/text()').extract_first()

            loctions = div.xpath('.//a[@class="pillDiv vem"]/@href').re('[\d]+')
            if loctions:
                loction = loctions[0]
                url = 'https://www.milanuncios.com/mapa/?id={}'.format(loction)
                yield Request(url, self.get_address, meta={'item': item})
            else:
                item['address'] = ''
                self.models.append(item)
                yield item
        next_url = response.xpath('//a[text()="Siguiente"]/@href').extract_first()
        if next_url:
            yield Request(response.urljoin(next_url), self.parse)
    # def parse_product(self, response):
    #     item = OrderedDict()
    #     item['title'] = response.xpath('//div[@class="pagAnuTituloBox"]/a/text()').extract_first()
    #     item['price'] = response.xpath('//div[@class="pagAnuPrecioTexto"]/text()').extract_first()
    #     item['url'] = response.url
    #     item['description'] = response.xpath('//p[@class="pagAnuCuerpoAnu"]/text()').extract_first()
    #
    #     item['size'] = response.xpath('//div[@class="m2 tag-mobile"]/text()').extract_first()
    #     item['bedrooms'] = response.xpath('//div[@class="dor tag-mobile"]/text()').extract_first()
    #     item['bathrooms'] = response.xpath('//div[@class="ban tag-mobile"]/text()').extract_first()
    #     item['price/m'] = response.xpath('//div[@class="pm2 tag-mobile"]/text()').extract_first()
    #
    #     loctions = response.xpath('//a[@class="map-button"]/@href').re('[\d]+')
    #     if loctions:
    #         loction = loctions[0]
    #         url = 'https://www.milanuncios.com/mapa/?id={}'.format(loction)
    #         yield Request(url, self.get_address, meta={'item':item})
    #     else:
    #         item['address'] = ''
    #         yield item

    def get_address(self, response):
        item = response.meta['item']
        lat = str(response.body).split('center: {lat:')[-1].split(',')[0]
        lng = str(response.body).split('center: {lat:')[-1].split('lng:')[-1].split('}')[0]
        # url = 'https://maps.googleapis.com/maps/api/js/GeocodeService.Search?5m2&1d{}&2d{}&7sUS&9sen-US&callback=_xdc_._p60ppu&key=AIzaSyALrSTy6NpqdhIOUs3IQMfvjh71td2suzY&token=566'.format(lat, lng)
        url = 'http://dev.virtualearth.net/REST/v1/Locations/{},{}?o=json&key=AlOnPDRawAhc9aCdu71DvEKkJ68f9Z217cLRguT-ll-9OFMKqRU5ofdu6NeFd5Rg'.format(lat, lng)

        data = json.loads(requests.get(url).text)
        item['address'] = data['resourceSets'][0]['resources'][0]['address']['formattedAddress']


        print (lat, lng)
        self.models.append(item)
        yield item