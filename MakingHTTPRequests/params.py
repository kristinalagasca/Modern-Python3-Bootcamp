import requests as r

url = 'https://icanhazdadjoke.com/search'

res = r.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

data = res.json()
print(data['results'])
