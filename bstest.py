from bs4 import BeautifulSoup
import requests
import mechanize

# MECHANIZE TEST
br = mechanize.Browser()
br.open("http://data.police.uk")
response = br.response()

print(response.geturl())
print(response.info())
print(response.read())

url = input("Enter a website:")

r = requests.get("http://" + url)

data = r.text

soup = BeautifulSoup(data, features="html.parser")

date_from = soup.find_all(id="id_date_from")
print(date_from)

#for link in soup.find_all('a'):
#    print(link.get('href'))