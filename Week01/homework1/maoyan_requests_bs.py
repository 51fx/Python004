# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://maoyan.com/films?showType=3'
headers = {
           'Cookie': '__mta=107436861.1601039898425.1601046738379.1601047324031.18; uuid_n_v=v1; mojo-uuid=78a9432a7946d3fe11e8578bfbbcd228; _lxsdk_cuid=174c56a16d9c8-08a7695cac15dc-333376b-e1000-174c56a16dac8; mojo-session-id={"id":"5dbd3bd9224681fc76fe7a6cc1bc4afc","time":1601087082464}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601039898,1601087082; uuid=C5C9A170FF9F11EA8A96E5AD964C71710F4F82CA7C0B49058AFE633E8053F4CF; _csrf=c3091f0bdae91a7bf1f994d7107b493c9a80b6f215430a48e38bc5b05afcc013; lt=SoRypZa19eBjRs4DlkC38YWmwIgAAAAArQsAAGm01KjiTtvwrsVbT6yV-l2vQ5xPosJuxHrnveW5dEDBqLWpaHJrBfJ8BpnxJ51CcQ; lt.sig=smNCwv6SHoQAP8wqhNufBWRJxv4; mojo-trace-id=7; _lxsdk=C5C9A170FF9F11EA8A96E5AD964C71710F4F82CA7C0B49058AFE633E8053F4CF; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601087232; __mta=107436861.1601039898425.1601047324031.1601087233915.19; _lxsdk_s=174c83a1004-775-4bc-513%7C%7C11',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
           }

response = requests.get(url, headers=headers)
bs_info = bs(response.text, 'html.parser')
csv_data = []
for tags in bs_info.find_all('dd', limit=10):
    movie_name = tags.find('span', attrs={'class': 'name'}).text
    movie_type = tags.find_all('div', attrs={'class': 'movie-hover-title'})[1].get_text().replace('类型:', '').replace(' ', '').replace('\n', '')
    movie_time = tags.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'}).get_text().replace('上映时间:', '').replace(' ', '').replace('\n', '')
    csv_row = [movie_name, movie_type , movie_time]
    csv_data.append(csv_row)

movies = pd.DataFrame(data=csv_data, columns=["电影名称", "电影类型", "上映时间"])
movies.to_csv('./movie.csv', encoding='utf8', index=False)
