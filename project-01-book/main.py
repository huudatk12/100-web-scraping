import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # DEBUG: Print the title of the page to ensure we are in the right place
        print(f"Connected to: {soup.title.string}")

        # Find all books - Let's try to be very specific
        books = soup.find_all("article", class_="product_pod")

        if not books:
            print("Target not found. Let's try searching for <h3> tags instead...")
            # Alternative search: find all h3 tags which contain the book links
            books_alt = soup.find_all("h3")
            print(f"Found {len(books_alt)} <h3> tags.")
        else:
            print(f"Success! Found {len(books)} books.\n")
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text
                print(f"Book: {title} | Price: {price}")
    else:
        print(f"Failed. Status: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")