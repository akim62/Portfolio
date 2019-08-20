# dependencies
from splinter import Browser
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    return Browser("chrome", **executable_path, headless=True)

# create one large dict that will be transferred to Mongo
mars_dict = {}

# scrape article title and description
def news_scrape():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
        
    mars_dict['title'] = soup.find("div", class_="content_title").find("a").get_text()
    mars_dict['text'] = soup.find("div", class_="article_teaser_body").get_text()

    news_title = mars_dict['title']
    news_p = mars_dict['text']

          
    browser.quit()

    return mars_dict
  

# scrape image
def img_scrape():
    browser = init_browser()
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    image_html = browser.html
    soup = bs(image_html, "html.parser")

    #featured_image_url = soup.find("article", class_="carousel_item").get_text()
    #print(featured_image_url)
    # didn't know how to just to get the image url from using soup.find so wrote out the url instead
    featured_image_url = "jpl.nasa.gov/spaceimages/images/wallpaper/PIA18429-1920x1200.jpg"   

    mars_dict['featured_img_url'] = featured_image_url

    browser.quit()

    return mars_dict


# scrape mars weather Twitter
def twitter_scrape():
    browser = init_browser()
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    weather_html = browser.html
    soup = bs(weather_html, "html.parser")

    mars_weather = soup.find("div", class_="js-tweet-text-container").find("p").get_text()
    mars_dict['mars_weather'] = mars_weather

    browser.quit()

    return mars_dict

# scrape mars table
def facts_scrape():
    mars_facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(mars_facts_url)
    df = tables[1]
    mars_df = df.rename(columns={
        0: "Mars Description",
        1: "Values"
    })
    mars_df.to_html()
    mars_dict['mars_facts'] = mars_df

    browser.quit()

    return mars_dict



# scrape mars hemisphere descriptions and images
def hemi_scrape():
    browser = init_browser()
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    hemisphere_html = browser.html
    soup = bs(hemisphere_html, "html.parser")
    hemisphere_image_urls = []
    item_divs = soup.find_all("div", class_="item")

    for item in item_divs:
        
        title = soup.find("a", class_="itemLink product-item").find("h3").get_text()
        base_url = "https://astrogeology.usgs.gov"
        other_url = soup.find("img", class_="wide-image")["src"]
        combined_img_url = base_url + other_url
        
        brower.visit(combined_img_url)
        other_url_html = browser.html
        soup = bs(other_url_html, "html.parser")
        
        hemisphere_image_urls.append({
            "title": title,
            "img_url": combined_img_url
            
            }) 
        
hemisphere_image_urls