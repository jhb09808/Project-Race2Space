# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer

# def fetch_space_news():
#     url = 'https://www.space.com/news'
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         articles = soup.find_all('article')  # Example selector, update based on inspection

#         news = []
#         for article in articles:
#             title_element = article.find('h3')
#             if not title_element:
#                 continue  # Skip articles without a title

#             title = title_element.text.strip()
#             link_element = article.find('a')
#             if not link_element:
#                 continue  # Skip articles without a link

#             link = link_element['href']
#             summary_element = article.find('p')
#             summary = summary_element.text.strip() if summary_element else 'No summary available'
#             news.append({'title': title, 'link': link, 'summary': summary, 'published_date': datetime.now()})

#         return news
#     else:
#         print(f"Failed to fetch the page. Status code: {response.status_code}")
#         return []

# def summarize_text(text, sentences_count=2):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, sentences_count)
#     return " ".join(str(sentence) for sentence in summary)
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def fetch_space_news():
    news_sources = [
        {'url': 'https://www.space.com/news', 'parser': parse_space_com},
        {'url': 'https://www.nasa.gov/news', 'parser': parse_nasa_news},
        {'url': 'https://philsa.gov.ph/articles/', 'parser': parse_philsa_news},
        {'url': 'https://scitechdaily.com/news/space/', 'parser': parse_scitech_news},
        # Add more sources here
    ]

    news = []
    for source in news_sources:
        url = source['url']
        parser = source['parser']
        news.extend(parser(url))

    return news

def parse_space_com(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        news = []
        for article in articles:
            title_element = article.find('h3')
            if not title_element:
                continue

            title = title_element.text.strip()
            link_element = article.find('a')
            if not link_element:
                continue

            link = link_element['href']
            summary_element = article.find('p')
            summary = summary_element.text.strip() if summary_element else 'No summary available'
            news.append({'title': title, 'link': link, 'summary': summary, 'published_date': datetime.now()})

        return news
    else:
        print(f"Failed to fetch the page from {url}. Status code: {response.status_code}")
        return []

def parse_nasa_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='content_title')

        news = []
        for article in articles:
            title_element = article.find('a')
            if not title_element:
                continue

            title = title_element.text.strip()
            link = "https://www.nasa.gov" + title_element['href']
            summary = "No summary available"
            news.append({'title': title, 'link': link, 'summary': summary, 'published_date': datetime.now()})

        return news
    else:
        print(f"Failed to fetch the page from {url}. Status code: {response.status_code}")
        return []

def parse_philsa_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='article__body')  # Update based on actual HTML structure

        news = []
        for article in articles:
            title_element = article.find('h2')
            if not title_element:
                continue

            title = title_element.text.strip()
            link_element = article.find('a')
            if not link_element:
                continue

            link = link_element['href']
            summary_element = article.find('p')
            summary = summary_element.text.strip() if summary_element else 'No summary available'
            news.append({'title': title, 'link': link, 'summary': summary, 'published_date': datetime.now()})

        return news
    else:
        print(f"Failed to fetch the page from {url}. Status code: {response.status_code}")
        return []

def parse_scitech_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='td_module_10')  # Update based on actual HTML structure

        news = []
        for article in articles:
            title_element = article.find('h3')
            if not title_element:
                continue

            title = title_element.text.strip()
            link_element = article.find('a')
            if not link_element:
                continue

            link = link_element['href']
            summary_element = article.find('p')
            summary = summary_element.text.strip() if summary_element else 'No summary available'
            news.append({'title': title, 'link': link, 'summary': summary, 'published_date': datetime.now()})

        return news
    else:
        print(f"Failed to fetch the page from {url}. Status code: {response.status_code}")
        return []

def summarize_text(text, sentences_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)
