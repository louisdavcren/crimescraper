from bs4 import BeautifulSoup # Beautiful Soup
import requests               # Handles requests
import mechanize              # Mechanize calls JS functions

# MECHANIZE TEST
br = mechanize.Browser()
br.open("http://data.police.uk")
response = br.response()

print(response.geturl())
print(response.info())
print(response.read())

# Softcoded the website URL
url = input("Enter a website:")

r = requests.get("http://" + url)

data = r.text
# Parser's through
soup = BeautifulSoup(data, features="html.parser")

date_from = soup.find_all(id="id_date_from")
print(date_from)

#for link in soup.find_all('a'):
#    print(link.get('href'))