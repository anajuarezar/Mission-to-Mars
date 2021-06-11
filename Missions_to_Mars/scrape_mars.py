# Depedencies
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('div', class_='list_text')
    news_title =  news.find('div', class_= 'content_title').text
    news_p = news.find(class_= 'article_teaser_body').text
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    header = soup.find('div', class_= "header")
    relative_image_path = soup.find_all('img', class_="headerimage fade-in")[0]["src"]
    featured_image_url = url + relative_image_path
    browser.quit()

    return news_title, news_p, featured_image_url