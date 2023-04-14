from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock


mock_db = [
  {
    "_id": "6439579743398c896f417ced",
    "url": "https://blog.betrybe.com/tecnologia/cabos-de-rede/",
    "title": "Cabos de rede: o que são, quais os tipos e como crimpar?",
    "timestamp": "10/04/2023",
    "writer": "Dayane Arena dos Santos",
    "reading_time": 9,
    "summary": "Os cabos de rede são itens extremamente necessários",
    "category": "Tecnologia"
  },
  {
    "_id": "6439579743398c896f417cee",
    "url": "https://blog.betrybe.com/desenvolvimento-web/estruturas-de/",
    "title": "Estruturas de repetição: quais as 4 principais e quando usá-las",
    "timestamp": "05/04/2023",
    "writer": "Vinicius Martins",
    "reading_time": 5,
    "summary": "As estruturas de repetição estão muito presentes na vida",
    "category": "Desenvolvimento Web"
  },
  {
    "_id": "6439579743398c896f417cef",
    "url": "https://blog.betrybe.com/tecnologia/website-development/",
    "title": "Website development: o que é, o que faz e salário! O guia!",
    "timestamp": "31/03/2023",
    "writer": "Lucas Custódio",
    "reading_time": 13,
    "summary": "O Website development pode ser encontrado no mercado",
    "category": "Tecnologia"
  },
  {
    "_id": "6439579743398c896f417cf0",
    "url": "https://blog.betrybe.com/tecnologia/code-review/",
    "title": "Code Review: como virar um caçador de bugs com 15 dicas",
    "timestamp": "22/03/2023",
    "writer": "Cairo Noleto",
    "reading_time": 11,
    "summary": "Manter a consistência do código de um projeto e identificar",
    "category": "Tecnologia"
  }
]


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_db)

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-10)

    news = ReadingPlanService.group_news_for_available_time(10)

    assert len(news['readable']) == 2
    assert len(news['unreadable']) == 2
    assert news['readable'][0]['unfilled_time'] == 1
    assert news['readable'][1]['unfilled_time'] == 5
