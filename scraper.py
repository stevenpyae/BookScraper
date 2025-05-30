# scraper.py

# Import the helper functions we defined for parsing and pagination
from utils.html_parser import extract_book_data
import requests               # For making HTTP requests to the website
import pandas as pd           # For converting our data to CSV
import time                   # For adding delay between requests

# Base URL pattern with a placeholder for the page number (1, 2, 3, ...)
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Output location for the final CSV file
OUTPUT_FILE = "output/books.csv"

def fetch_page_html(url: str) -> str:
    """
    Fetches the raw HTML content of a given URL.
    
    Args:
        url (str): The full URL of the page to fetch.
    
    Returns:
        str: Raw HTML content of the response.
    """
    response = requests.get(url)        # Send a GET request to the page
    response.raise_for_status()         # Raise an error if the request failed
    return response.text                # Return the page HTML as a string

def scrape_books(max_pages: int = 5) -> list:
    """
    Loops through the book pages and collects book data from each.
    
    Args:
        max_pages (int): How many pages to scrape (default is 5).
    
    Returns:
        list: A list of dictionaries, each containing data for one book.
    """
    all_books = []                      # This will store all extracted book data

    for page_number in range(1, max_pages + 1):
        url = BASE_URL.format(page_number)  # Build the URL for this page
        print(f"[INFO] Fetching: {url}")
        
        html = fetch_page_html(url)         # Download HTML for the current page
        
        books = extract_book_data(html)     # Parse the HTML to extract book info
        
        all_books.extend(books)             # Add books from this page to our list

        time.sleep(1)                       # Be respectful; wait 1 second per page

    return all_books

def save_to_csv(book_list: list):
    """
    Saves the list of books to a CSV file.
    
    Args:
        book_list (list): List of book data dictionaries.
    """
    df = pd.DataFrame(book_list)           # Convert list of dictionaries to DataFrame
    df.to_csv(OUTPUT_FILE, index=False)    # Export to CSV without the index column
    print(f"[INFO] Saved {len(df)} records to {OUTPUT_FILE}")

def main():
    """
    Main function that controls the flow of the scraping process.
    """
    print("[INFO] Starting scraping process...")
    
    book_data = scrape_books(max_pages=20)  # Scrape up to 20 pages (1000 books max)
    
    save_to_csv(book_data)                  # Save the results to a CSV file

# This ensures the script runs only when executed directly (not on import)
if __name__ == "__main__":
    main()
