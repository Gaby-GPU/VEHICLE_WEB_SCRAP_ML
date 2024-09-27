import requests
from bs4 import BeautifulSoup
import time
from utils.constants import URL_BASE, ITEMS_PER_PAGE
from utils.helpers import parse_html_to_data

def get_page_url(page_number):

    """
    Generates the URL for a specific page of search results.

    Args:
        page_number (int): The page number to generate the URL for.

    Returns:
        str: The URL corresponding to the specified page number.
    """

    initial_range = 1 + ITEMS_PER_PAGE * (page_number - 1)
    page_url = f'{URL_BASE}_Desde_{initial_range}_ITEM*CONDITION_2230581_NoIndex_True'
    return page_url

def scrape_page(page_number):

    """
    Fetches and parses the HTML content of a specific page.

    Args:
        page_number (int): The page number to scrape.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the page.

    Raises:
        Exception: If the request to fetch the page fails, an exception is raised with the error code.
    """

    url = get_page_url(page_number)
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        raise Exception(f'Error al obtener la página {page_number}: {response.status_code}')

def scrape_all_pages(max_pages=10):

    """
    Scrapes data from multiple pages and compiles it into a single list.

    Args:
        max_pages (int): The maximum number of pages to scrape. Default is 5.

    Returns:
        list: A list of dictionaries containing data scraped from the pages.

    Notes:
        - The function includes a delay (`time.sleep(2)`) between requests to avoid being blocked by the server.
    """

    all_data = []
    for page in range(1, max_pages + 1):
        print(f'Scraping page {page}...')
        soup = scrape_page(page)
        page_data = parse_html_to_data(soup)
        all_data.extend(page_data)
        time.sleep(2)  
    return all_data
