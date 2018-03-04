import requests, json
from requests.exceptions import ProxyError, Timeout, ConnectionError

url = 'https://norbaeocystin.github.io'
proxy=[
'122.72.18.35:80',
'139.224.80.139:3128',
'190.7.112.18:3128',
'120.79.133.212:8088'
    ]

    
def velocity(proxy_list = proxies):
    velocities = {}
    for item in proxy:
        try:
            proxies = {'https': item,}
            res = requests.get(url, proxies=proxies, timeout=2)
            t = res.elapsed.total_seconds()
            velocities[item]=t
        except (ProxyError, Timeout, ConnectionError ):
            pass
    return velocities
