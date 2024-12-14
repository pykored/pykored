from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pykored',
    version='0.1.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'aiohttp',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'pykored=pykored.__main__:main', 
        ],
    },
)
