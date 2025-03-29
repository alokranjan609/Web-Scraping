# Web Scraping Tool

A simple Python web scraping tool that uses BeautifulSoup to extract content from web pages.

## Features

- Extracts page title
- Extracts all paragraphs
- Extracts all links with their text and URLs
- Handles errors gracefully

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with a URL as an argument:

```bash
python web_scraper.py https://example.com
```

## Example Output

The script will display:
- The page title
- All paragraphs found on the page
- All links with their text and URLs

## Requirements

- Python 3.x
- beautifulsoup4
- requests