# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from anjuku.items import AnjukuItem
import time


class AnjuSpider(CrawlSpider):
    name = 'anju'
    allowed_domains = ['sh.zu.anjuke.com']
    start_urls = ['https://sh.zu.anjuke.com/fangyuan/pudong/?from=SearchBar']

    rules = (
        # 列表页面url提取规则
        # Rule(LinkExtractor(allow=r'https://sh\.zu\.anjuke\.com/fangyuan/pudong/p\d+/'), follow=True),
        # 详情页面url提取规则
        Rule(LinkExtractor(allow=r'https://sh\.zu\.anjuke\.com/fangyuan/\d+'), callback='parse_item'),
    )

    def parse_item(self, response):
        # print(response.url)
        # 创建存储数据的容器
        item = AnjukuItem()

        # 抽取数据
        # item['data_source'] = response.url
        # item['timestamp'] = time.time()

        # 从响应中抽取数据
        # item['title'] = response.xpath('//*[@id="content"]/div[2]/div[1]/h3/text()').extract_first()
        # item['village'] = response.xpath('//*[@id="content"]/div[1]/a[5]/text()').extract_first()
        # item['charge'] = response.xpath('//dl[@class="p_phrase cf"]/dd/strong/span/text()').extract_first()
        # item['fashion'] = response.xpath('//div[@class="litem fl"]/dl[4]/dd/text()').extract_first()
        # item['house_type'] = response.xpath('//div[@class="litem fl"]/dl[3]/dd/text()').extract_first()
        # item['address'] = response.xpath('//div[@class="litem fl"]/dl[6]/dd/a/text()').extract()
        # item['fixture'] = response.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/dl[2]/dd/text()').extract_first()
        # item['area'] = response.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/dl[3]/dd/text()').extract_first()
        # item['direction'] = response.xpath('//div[@class="ritem fr"]/dl[4]/dd/text()').extract_first()
        # item['floor'] = response.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/dl[5]/dd/text()').extract_first()
        # item['configure'] = response.xpath('//div[1][@class="pro_links"]/p/span/text()').extract()
        item['desc'] = response.xpath('//*[@id="propContent"]/div/p/text()').extract_first()  #no ce
        print(item)

