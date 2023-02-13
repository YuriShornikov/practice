import json

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()

HOST = 'https://habr.com/ru/all/'

# print(get_headers())

resp = requests.get(HOST, headers=get_headers())
habr_text = resp.text


soup = BeautifulSoup(habr_text, features='lxml')

article_list = soup.find('div', class_='tm-articles-list')
articles = article_list.find_all('article')
# print(len(articles))
# print(article_list)
parsed = []
for art in articles:
#     # time_art = art.find('time')
    header = art.find('h2')
    # print(header)
    #
    # time_parsed = time_art['datetime']
    header_parsed = header.text
    print(header_parsed)
    #
    # a_art = header.find('a')
    # print(a_art)
    # link_related = a_art['href']
    # link_absolute = f'https://habr.com{link_related}'
    #
    # resp = requests.get(link_absolute, headers=get_headers())
    # habr_art = BeautifulSoup(resp.text, features='lxml')
    # habr_art_tag = habr_art.find('div', id='post-content-body')
    # habr_art_text = habr_art_tag.text
    #
    # item = {
    #     'time': time_parsed,
    #     'header': header_parsed,
    #     'link': link_absolute,
    #     'text': habr_art_text
    # }
    # parsed.append(item)
    # print(parsed)

# with open('habr.json', 'w', encoding="utf-8") as f:
#     json.dump(parsed, f, indent=5)
#
#     print(habr_art_text)