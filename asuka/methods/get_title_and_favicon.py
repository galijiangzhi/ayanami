import requests
from bs4 import BeautifulSoup
import chardet

def get_title_and_favicon(url):
    print(f"开始处理{url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.content
        encoding = chardet.detect(html_content)['encoding']  # 检测网页编码
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding=encoding)  # 使用检测到的编码解析网页内容
        title = soup.title.string  # 获取网页标题
        favicon = soup.find('link', rel='icon')['href']  # 获取网页图标链接
        if f"//" not in favicon:
            # print(f"{favicon} 中不含有协议")
            favicon = url + favicon
        if "svg" not in favicon:
            return title,favicon
        else:
            if "http://" not in favicon:
                favicon = favicon.replace("//","https://")
                # print(f"修改之后的favicon为{favicon}")
            svg = requests.get(favicon)
            # print(svg.text)
            return title,favicon

    else:
        return str(response.status_code)