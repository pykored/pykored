# Pykored

## Overview
The `pykored` module is a Python-based tool for downloading video from [yako red](https://yakored1.net).

### Features:
- Extract video ID and title from a webpage.
- Fetch M3U8 playlist and parse segment URLs.
- Download video segments asynchronously.
- Merge video segments into a single MP4 file.
- Supports custom output directories.

## Installation

1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd pykored
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The module provides a main class `Yako` for downloading videos.

### Example

```python
from pykored import Yako

# Initialize Yako with the video URL
url = "https://yakored1.net/top/all/video/999999-example-page"
yako = Yako(url)

# Download the video to the default './downloads' directory
yako.download()

# Download the video to a custom directory
yako.download(output_dir='./custom_directory')
```

## File Structure

```
pykored/
├── __init__.py        
├── __main__.py          
├── downloader.py       
├── m3u8_handler.py      
├── segmenter.py
├── utils.py             
├── video_manager.py    
└── requirements.txt
```

## How It Works

1. **Initialization**: The `Yako` class is initialized with a video URL.
2. **Fetching Video Information**: Extracts the video ID and title from the provided URL.
3. **Fetching M3U8 Content**: Retrieves the M3U8 playlist file associated with the video.
4. **Segment Download**: Downloads all the video segments listed in the M3U8 file asynchronously.
5. **Segment Merge**: Combines the downloaded segments into a single MP4 file.

## Dependencies

- Python 3.8+
- aiohttp
- beautifulsoup4

Install the dependencies using:
```bash
pip install -r requirements.txt
```

## Notes

- Ensure the provided video URL is compatible with the tool’s extraction logic.
- The output directory will be created automatically if it does not exist.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

