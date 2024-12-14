import aiohttp
import asyncio
import os
import shutil

class VideoDownloader:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    @staticmethod
    async def fetch_m3u8_content(url):
        headers = {'Referer': 'https://hellocdn4.net/'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return None

    async def download_segment(self, session, url, filename):
        if url.endswith('.shtml'):
            actual_url = await self.get_actual_video_url(session, url)
            if actual_url:
                url = actual_url
        
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
            else:
                print(f'Failed to download segment from {url}, status code: {response.status}')

    async def download_segments_with_asyncio(self, segment_urls):
        os.makedirs(self.output_dir, exist_ok=True)

        async with aiohttp.ClientSession() as session:
            tasks = []
            for i, segment_url in enumerate(segment_urls):
                segment_filename = os.path.join(self.output_dir, f'segment_{i:03d}.ts')
                tasks.append(self.download_segment(session, segment_url, segment_filename))

            await asyncio.gather(*tasks)

    async def get_actual_video_url(self, session, shtml_url):
        async with session.get(shtml_url) as response:
            if response.status == 200:
                return str(response.url)
            return None

    def merge_ts_files(self, output_filename):
        ts_files = [f for f in os.listdir(self.output_dir) if f.endswith('.ts')]
        ts_files.sort()

        output_path = os.path.join(self.output_dir, output_filename)

        with open(output_path, 'wb') as output_file:
            for ts_file in ts_files:
                ts_file_path = os.path.join(self.output_dir, ts_file)
                with open(ts_file_path, 'rb') as f:
                    shutil.copyfileobj(f, output_file)
