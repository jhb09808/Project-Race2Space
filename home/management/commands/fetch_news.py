from django.core.management.base import BaseCommand
from home.news_fetcher import fetch_space_news, summarize_text
from home.models import NewsArticle

class Command(BaseCommand):
    help = 'Fetch latest space news and save to database'

    def handle(self, *args, **kwargs):
        articles = fetch_space_news()

        for article in articles:
            summarized_text = summarize_text(article['summary'])
            # Check if the article already exists to avoid duplicates
            if not NewsArticle.objects.filter(title=article['title']).exists():
                NewsArticle.objects.create(
                    title=article['title'],
                    summary=summarized_text,
                    link=article['link'],
                    published_date=article['published_date']
                )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved news articles'))
