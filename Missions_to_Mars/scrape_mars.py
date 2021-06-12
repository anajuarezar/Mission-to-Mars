# Depedencies
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('div', class_='list_text')
    news_title =  news.find('div', class_= 'content_title').text
    news_p = news.find(class_= 'article_teaser_body').text
    browser.quit()

    try: 
        url = 'https://spaceimages-mars.com/'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        header = soup.find('div', class_= "header")
        relative_image_path = soup.find_all('img', class_="headerimage fade-in")[0]["src"]
        featured_image_url = url + relative_image_path
        browser.quit()
    except: 
        featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'

    # url = 'https://marshemispheres.com/'
    # browser.visit(url)
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')

    # hemisphere_image_urls = []
    # items = soup.find_all('div', class_='item')

    # for item in items:
    #     title = item.find('div', class_='description').find('a').find('h3').text
    #     url_path = item.find('a')['href']
    #     original_url = 'https://marshemispheres.com/'
    #     image_url = original_url + url_path
    #     browser.visit(image_url)
    #     html = browser.html
    #     soup = BeautifulSoup(html, 'html.parser')
    #     image_path = soup.find('div', class_='downloads').find('ul').find('li').find('a')['href']
    #     image = original_url + image_path 
    #     hemisphere_image_urls.append({'title': title, 'img_url': image})
    
    # browser.quit()


    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        #"hemisphere_image_urls": hemisphere_image_urls
        }
        
    print(mars_data)

    return mars_data
scrape()