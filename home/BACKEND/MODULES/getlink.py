import requests
from bs4 import BeautifulSoup as bs


def GetReviewsLink(link):
    if "flipkart" not in link:
        return "Invalid Link"

    elif "product-reviews" in link:
        return link
    else:
        pass
    url = requests.get(link)

    soup = bs(url.content, 'html.parser')
    review_link = None

    for link in soup.find_all('a'):
        if "product-reviews" in link.get('href'):
            review_link = "https://www.flipkart.com" + \
                link.get('href') + "?page=1"
            break
        else:
            pass

    link = review_link.split("&")[0]
    print(link)
    return link


if __name__ == "__main__":
    GetReviewsLink("https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&ssid=jfd2ppy3ww0000001715900793035")
