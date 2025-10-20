import requests
import time
from fake_useragent import UserAgent
import random

url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=b3c4ffa1-3cee-4c44-9f44-96eeb826657c"

session = requests.Session()

headers = {
    'User-Agent': UserAgent().random,
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com'
}




r = session.get(url)

with open ("File.html","w") as f:
    f.write(r.text)
