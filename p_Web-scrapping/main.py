import requests

from bs4 import BeautifulSoup

template = '''
<div class="ip" id="d_clip_button" style="cursor: pointer;">
                                    <span>83.220.239.219</span>

                                    <i class="ip-icon-shape btn-copy"></i>
                                </div>
'''

HOST = 'https://2ip.ru'

resp = requests.get(HOST)
resp_text = resp.text
# print(resp_text)

soup = BeautifulSoup(resp_text, features='lxml')

d_clip_button = soup.find(id='d_clip_button')
# print(d_clip_button)

span = d_clip_button.find('span')
ip = span.text
print(f'Your ip adress {ip}')
# print(span)