# BookScraper

A Python web scraper that extracts book data (title, price, rating, availability) from [BooksToScrape.com](http://books.toscrape.com). The output is saved as a clean, structured CSV file containing over 400 book records.

---

##  Features

- Scrapes **all pages** from the BooksToScrape site
- Extracts:
  - Title 
  - Price in GBP
  - Star rating 
  - Availability
- Saves results to `output/books.csv`
- Minimal dependencies, fast execution

---

## 🛠️ Setup Instructions (Terminal)

### 1. Clone the Repository
git clone https://github.com/stevenpyae/BookScraper.git
cd BookScraper

### 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Python script
python scraper.py

### 5. Check output 
Successful Extraction : [INFO] Saved 400 records to output/books.csv
Check output/books.csv

### 6. Review
Current set for 20 pages, Modify the below data to your desired outcome
--scraper.py Line 74: book_data = scrape_books(max_pages=20)  # Scrape up to 20 pages (400 books max)