from home.BACKEND.MODULES.parser import fetchAndSaveToFile
import time


def saveToFolder(url, path, page_count=1):
    try:
        if "https://" in url:
            file_name = url.split("/")[3]
        else:
            file_name = url.split("/")[1]
        
        for i in range(0, page_count):
            new_url = url + f"&page={i+1}"  
            fetchAndSaveToFile(new_url, f"{path}/{file_name}_{i+1}.html")
            time.sleep(1)
    except Exception as e:
        print("Error fetching data from ", url)
        print(e)
        return
