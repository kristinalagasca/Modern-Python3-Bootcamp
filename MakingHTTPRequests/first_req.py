'''
Using the requests Module
'''

import requests as r

url = 'https://news.ycombinator.com/'
res = r.get(url)

print(f'Your request to {url} came back w/ status code {res.status_code}')
# print(res)
# print(res.ok)
# print(res.headers)
