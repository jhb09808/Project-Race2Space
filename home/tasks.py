from celery import shared_task
from .models import NewsArticle
from .news_fetcher import fetch_space_news, summarize_articles

@shared_task
def update_news():
    articles = fetch_space_news()
    summarized_articles = summarize_articles(articles)
    for article in summarized_articles:
        NewsArticle.objects.create(title=article['title'], summary=article['summary'], link=article['link'])
