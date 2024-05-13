# folder_reader.py
import os
import logging
from home.BACKEND.MODULES.scrapper import scrapData

# Set up logging to print to the console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
words_collection = []


def readFolder(folder):
    try:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                words_list, title, total_reviews = scrapData(
                    file_path)
                logger.info(f"Processed file: {file_path}")
                logger.info(f"Title: {title}, Total Reviews: {
                            total_reviews}, Words Count: {len(words_list)}")
                words_collection.extend(words_list)

        logger.info(f"Total words count: {len(words_collection)}")
        logger.info(f"Unique words count: {len(set(words_collection))}")
        logger.info(f"Words Collection: {words_collection}")
        return words_collection, len(set(words_collection)), len(words_collection), title, total_reviews
    except Exception as e:
        logger.error(f"Error while reading folder {folder}: {e}")


if __name__ == "__main__":
    # This block runs only when this script is executed directly, not when imported as a module
    readFolder("../data", "your_db_name", "your_collection_name")
