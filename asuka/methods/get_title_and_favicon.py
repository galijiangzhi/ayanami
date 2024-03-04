import requests
from bs4 import BeautifulSoup

def get_title_and_favicon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string  # 获取网页标题
        favicon = soup.find('link', rel='icon')['href']  # 获取网页图标链接
        return title,favicon
    else:
        return str(response.status_code)