import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(url):
    """Hàm này làm nhiệm vụ đi cào dữ liệu"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    data = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        data.append({"Title": title, "Price": price})
    return data

def save_to_csv(data, filename):
    """Hàm này làm nhiệm vụ lưu file"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved {len(data)} books to {filename}")

if __name__ == "__main__":
    target_url = "https://books.toscrape.com/"
    book_list = scrape_books(target_url)
    
    if book_list:
        save_to_csv(book_list, "travel_books.csv")