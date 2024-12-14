import aiohttp
from bs4 import BeautifulSoup

async def fetch_html_content(url):
    headers = {'Referer': 'https://hellocdn4.net/'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                return await response.text()
            else:
                return None

def extract_video_id_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    video_id_tag = soup.find('meta', property='og:image')

    if video_id_tag and 'content' in video_id_tag.attrs:
        video_id = video_id_tag['content'].split('/')[-1].split('.')[0]
        return video_id
    return None

def extract_title_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')

    if title_tag:
        title = title_tag.get_text(strip=True)
        return title
    return 'output'

async def extract_video_id(url):
    html_content = await fetch_html_content(url)

    if html_content:
        return extract_video_id_from_html(html_content), extract_title_from_html(html_content)
    return None, None