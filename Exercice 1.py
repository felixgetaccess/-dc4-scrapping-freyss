import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(link.get('href'))