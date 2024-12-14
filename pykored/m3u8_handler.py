from pykored.downloader import VideoDownloader

class M3U8Handler:
    def __init__(self, fetcher: VideoDownloader):
        self.fetcher = fetcher

    async def get_m3u8_content(self, video_id):
        m3u8_urls = [
            f'https://yadongplay1.net/page/{video_id}.html',
            f'https://yadongplay1.net/jgpt/{video_id}',
            f'https://yadongplay1.net/guru/{video_id}'
        ]
        for url in m3u8_urls:
            m3u8_content = await self.fetcher.fetch_m3u8_content(url)
            if m3u8_content:
                return m3u8_content
        return None
