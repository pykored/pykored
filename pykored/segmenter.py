import re

class VideoSegmenter:
    def __init__(self, m3u8_content):
        self.m3u8_content = m3u8_content

    def extract_segment_urls(self):
        segment_urls = re.findall(r'#EXTINF:[\d\.]+,\s*(https?://[^\s]+)', self.m3u8_content)
        return segment_urls