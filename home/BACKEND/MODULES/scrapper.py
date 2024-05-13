# scrapper.py
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def scrapData(file):
    try:

        with open(file, "r", encoding="utf-8") as file:
            html = file.read()

        soup = BeautifulSoup(html, "html.parser")

        # Extract title
        title = soup.title.string if soup.title else "No title"

        # Extract total reviews count
        total_reviews = soup.select_one(
            "span.Wphh3N > span:last-child").string if soup.select_one("span.Wphh3N > span:last-child") else "Unknown"

        # Extract comments
        comments_section = soup.find_all("div", class_="ZmyHeo")

        all_words = []
        for comment in comments_section:
            unwanted = comment.find("span", class_="wTYmpv")
            if unwanted:
                unwanted.decompose()
            comment_text = comment.get_text(separator=' ', strip=True)
            all_words.extend(comment_text.split())

        return (all_words, title, total_reviews)
    except Exception as e:
        logger.error(f"Error processing file {file}: {e}")
        return ([], "Error", "Error")
