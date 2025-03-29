import requests
from bs4 import BeautifulSoup
import sys

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else "No title found"
        print(f"\nTitle: {title}\n")
        
        # Extract all paragraphs
        paragraphs = soup.find_all('p')
        print("Paragraphs:")
        for i, p in enumerate(paragraphs, 1):
            print(f"{i}. {p.get_text().strip()}")
        
        # Extract all links
        links = soup.find_all('a')
        print("\nLinks:")
        for i, link in enumerate(links, 1):
            href = link.get('href')
            text = link.get_text().strip()
            if href and text:
                print(f"{i}. {text} -> {href}")
        
        return True
        
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python web_scraper.py <url>")
        print("Example: python web_scraper.py https://example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    scrape_website(url) 