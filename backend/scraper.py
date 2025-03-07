import requests
from bs4 import BeautifulSoup

def scrape_prices(item: str):
    return {
        "item": item,
        "price": "$5.99",
        "store": "Example Store"
    }
