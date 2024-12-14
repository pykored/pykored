import argparse
from pykored import Yako

def main():
    parser = argparse.ArgumentParser(description="Pykored: A tool for downloading videos from YakoRed")
    parser.add_argument('url', type=str, help='URL of the video to download')
    parser.add_argument('--output-dir', type=str, default='./downloads', help='Directory to save the downloaded video')

    args = parser.parse_args()

    yako = Yako(args.url)

    yako.download(output_dir=args.output_dir)
    print(f"Video downloaded to {args.output_dir}")

if __name__ == '__main__':
    main()
