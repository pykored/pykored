import sys
import os
import asyncio
import argparse
from pykored.utils import extract_video_id
from pykored.downloader import VideoDownloader
from pykored.m3u8_handler import M3U8Handler
from pykored.video_manager import VideoManager
from pykored.segmenter import VideoSegmenter

profile = os.getenv('USERPROFILE')
path = os.path.join(profile, 'Downloads')

class Yako:
    def __init__(self, url):
        self.url = url
        self._video_id = None
        self._title = None

    async def __extract(self):
        self._video_id, self._title = await extract_video_id(self.url)

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

    async def __download_async(self, output_dir=path):
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
        print(f"Download complete! Video saved in: {output_dir}")

    async def download(self, output_dir=path):
        await self.__download_async(output_dir)


def main():
    while True:
        path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
        print("====== Yako Red Video Downloader ======")
        print("1. Download a video")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "2":
            print("Press Enter to exit...")
            input()
            sys.exit(0)

        elif choice == "1":
            url = input("Enter the video URL: ").strip()
            output_dir = input(f"Enter output directory (press Enter for '{path}'): ").strip()
            if not output_dir:
                output_dir = path
            if not output_dir.startswith(profile):
                output_dir = os.path.join(profile, output_dir)

            yako = Yako(url)
            try:
                asyncio.run(yako.download(output_dir=output_dir))

                input("Press Enter to exit...")
            except Exception as e:
                print(f"Error: {str(e)}")
                input("Press Enter to exit...")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Pykored Video Downloader")
        parser.add_argument("url", help="The URL of the video to download")
        parser.add_argument(
            "--output",
            default='/Downloads',
            help=f"The directory to save the downloaded video (default: /Downloads)",
        )
        args = parser.parse_args()

        yako = Yako(args.url)
        try:
            asyncio.run(yako.download(output_dir=args.output))

            input("Press Enter to exit...")
        except Exception as e:
            print(f"Error: {str(e)}")
            input("An error occurred. Press Enter to exit...")

    else:
        main()
