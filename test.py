from bs4 import BeautifulSoup
import requests


# url = 'https://webscraper.io/test-sites/pagination'
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

headers = {
    'User-Agent': 'AWDWebScraper/1.0 (contact: anyandarhesbon@gmail.com)'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

datatype_table = soup.find(class_="wikitable")
body = datatype_table.find('tbody')
rows = body.find_all('tr')[1:]

mutable_types = []
immutable_types = []

for row in rows:
    data =row.find_all('td')
    if data[1].get_text() == 'mutable\n':
        mutable_types.append(data[0].get_text().strip())
    else:
        immutable_types.append(data[0].get_text().strip())

print('Mutable Types: ', mutable_types)
print('Immutable Types: ', immutable_types)
# headings1 = soup.find_all('h2')
# images = soup.find_all('img')
# table = soup.find_all('table')
# print(table)