from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": f"{title}", "$options": "i"}}
    result = search_news(query)
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    try:
        format_date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError('Data inválida')

    result = search_news({"timestamp": format_date})
    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
