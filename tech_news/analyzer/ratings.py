from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    categories = []
    news_in_db = find_news()

    for news in news_in_db:
        categories.append(news["category"])

    result = Counter(sorted(categories))
    return sorted(result, key=result.get, reverse=True)[0:5]
