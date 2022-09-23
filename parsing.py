import requests
from bs4 import BeautifulSoup
from time import sleep

"""ЗАПУСКАТЬ ПРИ ПОМОЩИ ФАЙЛА code.py"""

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.1027 Yowser/2.5 Safari/537.36'
}

# def download(url):
#     """Загружаем фото товара в папку image"""
#     resp = requests.get(url, stream=True)
#     r = open('D:\\Python\\Parsing\\image\\' + url.split('/')[-1], 'wb')
#     for value in resp.iter_content(1024*1024):
#         r.write(value)
#     r.close()

def get_url():
    """Проходим по всем страницам и собираем все ссылки на карточки"""
    for count in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for link in data:
            card_url = 'https://scrapingclub.com' + link.find('a').get('href')
            yield card_url


def scraping():
    """Проходим по каждой ссылке на карточку"""
    for card_url in get_url():
        response = requests.get(card_url, headers=HEADERS)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='card mt-4 my-4')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        description = data.find('p', class_='card-text').text
        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
        # download(url_img)
        yield name, price, description, url_img



