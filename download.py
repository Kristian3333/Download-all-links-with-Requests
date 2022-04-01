import requests 
from requests_html import HTMLSession
import urllib.request as ur
from lxml import html
from bs4 import BeautifulSoup
from secrets import password, email

login_url='https://www.chessmasterschool.com/login/index.php'
secure_url=' https://www.chessmasterschool.com/clients/main.php'

headers = {
    'authority': 'www.chessmasterschool.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://www.chessmasterschool.com',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.chessmasterschool.com/',
    'accept-language': 'en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6',
    'cookie': 'PHPSESSID=6861e3b9b337e36cde59777728d70104',
    'sec-gpc': '1',
}

data = {
  'login': email,
  'parola': password
}

response= requests.post(login_url, headers=headers, data=data, allow_redirects=True) 
print(response)


with requests.Session() as s:
    response= s.post(login_url, headers=headers, data=data)
    # print the html returned or something more intelligent to see if it's a successful login page.
    r=s.get(secure_url)
    r=s.get('https://www.chessmasterschool.com/clients/puzzles/main-puzzles.php#clienttop')
    print(r.text)
    webpage = html.fromstring(r.content)
    print(webpage.xpath('//a/@href'))
    # An authorised request.
 
