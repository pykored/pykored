import os
import shutil
from pykored.downloader import VideoDownloader

class VideoManager:
    def __init__(self, output_mp4_dir):
        self.output_mp4_dir = output_mp4_dir
        self.downloader = VideoDownloader(output_dir='./video_segments')

    async def download_video(self, segment_urls, title):
        output_filename = f'{title}.mp4'
        await self.downloader.download_segments_with_asyncio(segment_urls)
        self.downloader.merge_ts_files(output_filename)
        output_mp4_path = os.path.join(self.output_mp4_dir, output_filename)
        os.rename(os.path.join(self.downloader.output_dir, output_filename), output_mp4_path)
        self.delete_video_segments_folder(self.downloader.output_dir)

    def delete_video_segments_folder(self, output_dir):
        if os.path.exists(output_dir):
            for file in os.listdir(output_dir):
                file_path = os.path.join(output_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            shutil.rmtree(output_dir)
        else:
            print(f'{output_dir} does not exist.')
