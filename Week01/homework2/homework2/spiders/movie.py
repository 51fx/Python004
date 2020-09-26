# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import Homework2Item


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析页面
        movie_name_list = Selector(response=response).xpath('//dd/div[1]/div[2]/a/div/div[1]/span[1]/text()').extract()
        movie_type_list = Selector(response=response).xpath('//dd/div[1]/div[2]/a/div/div[2]/text()').extract()
        movie_time_list = Selector(response=response).xpath('//dd/div[1]/div[2]/a/div/div[4]/text()').extract()

        # 去除换行、空格
        movie_type_list = eval(str(movie_type_list).replace(' ', '').replace('\\n', ''))
        movie_time_list = eval(str(movie_time_list).replace(' ', '').replace('\\n', ''))
        for ele in movie_type_list:
            if len(ele) == 0:
                 movie_type_list.remove(ele)
                 movie_time_list.remove(ele)

        items = []
        for index in range(10):
            item = Homework2Item(movie_name=movie_name_list[index], movie_type=movie_type_list[index], movie_time=movie_time_list[index])
            items.append(item)
        return items

