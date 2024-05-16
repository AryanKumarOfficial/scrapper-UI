import requests
from home.BACKEND.MODULES.getlink import GetReviewsLink

url = "https://api.scrapingant.com/v2/general" #proxy url


target_url  =f"https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&page=1" #product url


proxies ={
   "http" :"20.204.190.254:3129",
   "https": "20.219.178.121:3129",
}


params = {
    "url": target_url,
    "x-api-key": "00fd0fc814e44a07b06ced7aba3d331f",
    "render_js": "false",
    "proxy": proxies
}



def fetchAndSaveToFile(url,path):
    try:
        link = GetReviewsLink(url)
        print("Fetching data from ",link)
        r= requests.get(link)
        with open(path, "w",encoding="utf-8") as f:
                # print(r.text)
                f.write(r.text)
        print("Data saved to ",path)


    except Exception as e:
        print("Error fetching data from ",link)
        print(e)
        return


# fetchAndSaveToFile(url,"data/flipkart_iphone.html" )