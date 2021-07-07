import requests as r

url = 'https://icanhazdadjoke.com/'

# This tells the API to return the plain text version of URL
res_t = r.get(url, headers={"Accept": "text/plain"})

# This returns the JSON version of the site
res_j = r.get(url, headers={"Accept": "application/json"})

print(res_t.text)       # returns as string
print(res_j.json())     # returns as JSON

