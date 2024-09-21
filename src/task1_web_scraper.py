import requests
from bs4 import BeautifulSoup

def scrape_ndtv_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []
    
    def extract_link_info(a_tag):
        return {
            'text': a_tag.get_text(strip=True),
            'href': a_tag.get('href', '')
        }
    
    for a_tag in soup.find_all('a', class_='crd_lnk'):
        articles.append(extract_link_info(a_tag))
    
    for a_tag in soup.find_all('a', class_='crd_ttl8'):
        articles.append(extract_link_info(a_tag))
    
    for h3_tag in soup.find_all('h3', class_='crd_ttl8'):
        a_tag = h3_tag.find('a')
        if a_tag:
            articles.append(extract_link_info(a_tag))
    
    # remove duplicates
    seen = set()
    unique_articles = []
    for article in articles:
        article_tuple = (article['text'], article['href'])
        if article_tuple not in seen:
            seen.add(article_tuple)
            unique_articles.append(article)
    
    return unique_articles

if __name__ == "__main__":
    ndtv_url = "https://www.ndtv.com"
    scraped_articles = scrape_ndtv_articles(ndtv_url)
    
    print(f"Scraped {len(scraped_articles)} unique articles:")
    for index, article in enumerate(scraped_articles, 1):
        print(f"{index}. Title: {article['text']}\n")
        print(f"---->URL: {article['href']}")