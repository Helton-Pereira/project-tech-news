import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_links = selector.css("h2 a::attr(href)").getall()
    if news_links is False:
        no_links = []
        return no_links
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(
        ".next.page-numbers::attr(href)").get()
    if not next_page_url:
        return None
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
