# Zillow Scraper using Scrapy

This Scrapy project is designed to extract real estate listing data from [Zillow](https://www.zillow.com/) for the New York, NY area (or any city of your choice). It handles pagination, extracts key listing features, and supports CSV export.

## Project Structure

zilscraper/
├── zilscraper/
│ ├── spiders/
│ │ └── zilspider.py
│ ├── items.py
│ ├── middlewares.py
│ ├── pipelines.py
│ ├── settings.py
├── zillow_listings.csv
└── scrapy.cfg

markdown
Copy
Edit

## What It Does

### 1. Spider Setup
- Defines a Scrapy spider named `zilspider`
- Starts crawling from a Zillow search URL

### 2. Initiating Requests
- Uses `start_requests()` to send the initial request

### 3. Parsing JSON Data
- Extracts data from the `<script id="__NEXT_DATA__">` tag
- Parses the embedded JSON structure to locate listings

### 4. Extracted Fields Per Listing

Each listing includes:
- address
- price
- beds
- baths
- area (in sq ft)
- homeType
- statusText
- latLong
- livingArea
- yearBuilt
- lotAreaValue and lotAreaUnit
- zipcode, city, state, country
- url (link to the Zillow page)

### 5. Pagination
- Detects and follows the "Next Page" link
- Scrapes across multiple pages (Zillow currently allows around 20 pages)

## Output

- Listings are saved to `zillow_listings.csv`
- The CSV contains a header row and all the data rows for each listing

## Disclaimer

This project is intended for educational and research purposes only. Please consult Zillow's [robots.txt](https://www.zillow.com/robots.txt) and terms of use before deploying a scraper on their site.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/zillow-scraper.git
cd zillow-scraper
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install scrapy
Run the spider:

bash
Copy
Edit
scrapy crawl zilspider
Future Improvements
Store scraped data in a database

Add search filters (e.g., price range, bed/bath count)

Add Playwright or Selenium support for JS-heavy pages

Automate periodic scraping with cron or Scrapyd

Author
Bhavagna Shreya Bandaru
Email: bbandar5@asu.edu
Portfolio: https://bhavagna-shreya-portfolio.vercel.app

go
Copy
Edit
