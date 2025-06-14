# Scrapy settings for zilscraper project

BOT_NAME = "zilscraper"

SPIDER_MODULES = ["zilscraper.spiders"]
NEWSPIDER_MODULE = "zilscraper.spiders"

# Ignore robots.txt (set to True to obey)
ROBOTSTXT_OBEY = False

# Set number of concurrent requests
CONCURRENT_REQUESTS = 1

# Default headers for all requests
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.zillow.com/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

# Use UTF-8 encoding for CSV/JSON export
FEED_EXPORT_ENCODING = "utf-8"

# ---- Scrapy Playwright Integration ----

# Enable the async reactor needed by Playwright
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Configure Playwright download handler
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# Enable Playwright middleware
DOWNLOADER_MIDDLEWARES = {
    "scrapy_playwright.middleware.PlaywrightMiddleware": 543,
}

# Browser type: chromium / firefox / webkit
PLAYWRIGHT_BROWSER_TYPE = "chromium"

# Launch options for the browser
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,  # Set to False to see browser while debugging
}
