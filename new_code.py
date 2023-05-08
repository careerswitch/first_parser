import requests
from bs4 import BeautifulSoup

url = 'https://www.shopmarketbasket.com'

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup and lxml parser
soup = BeautifulSoup(html_content, 'lxml')

print(soup)

# # Find the location div using the xpath
# location_div = soup.find('div', {'id': 'closest-locations'}).find_all('li')[1].find('div', {'class': 'store-addr'})
#
# # Get the text content of the location div
# location = location_div.text.strip()
#
# # Print the location
# print(soup)
