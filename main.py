import requests as req
from bs4 import BeautifulSoup


url = 'https://rapidapi.com/collection/list-of-free-apis'
raw_page = req.get(url)

soup = BeautifulSoup(raw_page.text, 'html.parser')
detected_data = soup.find_all('div', {'class': 'body1 bold ApiName'})

for data in detected_data:
    data = str(data).split('<div class="body1 bold ApiName" data-v-7d5fa360="">')[1]
    data = data.split('</div>')[0]
    print(data)