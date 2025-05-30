# This module provides functions to parse HTML content and extract book data.
# utils/html_parser.py

from bs4 import BeautifulSoup

def extract_book_data(html: str) -> list: #html 
    """
    Parses the HTML of a page to extract information about all books on that page.
    
    Args:
        html (str): The raw HTML content of the page.
    
    Returns:
        list: A list of dictionaries, each representing one book.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # Each book is inside an <article> tag with class "product_pod"
    books = soup.select("article.product_pod")
    extracted_data = []

    for book in books:
        # Extract the title from the <a> tag's "title" attribute
        title = book.h3.a["title"]

        # Extract the price (e.g., "£51.77") and clean it to just the number
        price = book.select_one(".price_color").text.strip().replace("£", "")

        # Extract star rating from the class list (e.g., ['star-rating', 'Three'])
        rating_class = book.select_one(".star-rating")["class"]

        # Convert the rating class name to a number using a helper
        rating = convert_rating(rating_class)

        # Extract availability text (e.g., "In stock")
        availability = book.select_one(".availability").text.strip()

        # Append extracted info to our results list
        extracted_data.append({
            "title": title,
            "price_gbp": float(price),
            "rating": rating,
            "availability": availability,
        })

    return extracted_data

def convert_rating(class_list: list) -> int:
    """
    Converts star rating class (e.g., 'Three') to an integer value (e.g., 3).
    
    Args:
        class_list (list): A list of class names from the rating element.
    
    Returns:
        int: Numerical rating from 1 to 5. Returns 0 if not found.
    """
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    # Loop through all classes (usually ['star-rating', 'Three']) and match the rating name
    for cls in class_list:
        if cls in rating_map:
            return rating_map[cls]

    # Fallback if rating not found (shouldn't happen on this site)
    return 0
