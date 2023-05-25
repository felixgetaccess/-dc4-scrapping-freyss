from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
countries = soup.find_all("div", class_="col-md-4 country")

for country in countries:
    country_name = country.find("h3").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()
    population = country.find("span", class_="country-population").text.strip()
    area = country.find("span", class_="country-area").text.strip()

    print("Pays:", country_name)
    print("Capitale:", capital)
    print("Population:", population)
    print("Superficie (km²):", area)
    print("--------")
