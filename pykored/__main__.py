import os
import asyncio
import pykored.utils as utils
from pykored.downloader import VideoDownloader
from pykored.m3u8_handler import M3U8Handler
from pykored.video_manager import VideoManager
from pykored.segmenter import VideoSegmenter

class Yako:
    def __init__(self, url):
        self.url = url
        self._video_id = None
        self._title = None

    async def __extract(self):
        self._video_id, self._title = await utils.extract_video_id(self.url)
        return None

    @property
    async def title(self):
        if not self._title:
            await self.__extract()

        return self._title
    
    @property
    async def video_id(self):
        if not self._video_id:
            await self.__extract()

        return self._video_id
    
    async def __download_async(self, output_dir='./downloads'):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        await self.__extract()

        title = await self.title
        video_id = await self.video_id
        
        m3u8_content = await M3U8Handler(VideoDownloader).get_m3u8_content(video_id)
        if not m3u8_content:
            print('Failed to fetch M3U8 content.')
            return

        segment_urls = VideoSegmenter(m3u8_content).extract_segment_urls()
        if not segment_urls:
            print('No segments found in the M3U8 file.')
            return

        video_manager = VideoManager(output_dir)
        await video_manager.download_video(segment_urls, title)

    def download(self, output_dir='./downloads'):
        asyncio.run(self.__download_async(output_dir))


def main():
    if len(sys.argv) < 2:
        print("Usage: pykored <URL>")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else './downloads'
    
    yako = Yako(url)
    yako.download(output_dir)
