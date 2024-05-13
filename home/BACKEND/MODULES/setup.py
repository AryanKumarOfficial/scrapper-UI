# # this file will first run the parser file first then only after the completion of the parser file it will run the extractor file and after that the setup file will delete all the contents of the data folder.

# # also create a database in mongodb and create a collection in it for storing the data unique words count, total words count, title, total reviews for each url.

# from extractor import readFolder
# from fetcher import saveToFolder
# import os


# folder = "../data"


# def setup(url):
#     try:
#         if not os.path.exists(folder):
#             os.makedirs(folder)
#         saveToFolder("https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&page=1", folder)
#         readFolder(folder, "your_db_name", "your_collection_name")
#         for root, _, files in os.walk(folder):
#             for file in files:
#                 os.remove(os.path.join(root, file))
#     except Exception as e:
#         print("Error in setup")
#         print(e)
#         return


# if __name__ == "__main__":

#     setup("https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOAGTAPNVFZZY&marketplace=FLIPKART&page=1")
# # This block runs only when this script is executed directly, not when imported as a module
