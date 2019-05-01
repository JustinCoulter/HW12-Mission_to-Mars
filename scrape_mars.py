from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)   


def scrape():
    # get info from https://mars.nasa.gov/news/
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find('div', class_="content_title").text

    news_p = soup.find('div', class_="article_teaser_body").text

    # get featured mars image from https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    #browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    time.sleep(2)
    browser.click_link_by_partial_href('largesize')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    bod = soup.find_all("img")

    for val in bod:
        get_val = val["src"]
    featured_image_url = get_val

    time.sleep(2)

    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    tables = pd.read_html(url)
    df = tables[0]
    html_table = df.to_html()

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    ############################################
    #   mars hemispheres
    ############################################
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # first hemisphere
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    i_soup = soup.find('a',target='_blank')
    title_hem1 = soup.find('h2',class_='title').text
    i_soup = soup.find('a',target='_blank')
    for i in i_soup:
        hem_img1_link = i_soup["href"]

    browser.back()
    time.sleep(2)

    # 2nd hemisphere
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_hem2 = soup.find('h2',class_='title').text

    j_soup = soup.find('a',target='_blank')
    for j in j_soup:
        hem_img2_link = j_soup["href"]

    browser.back()
    time.sleep(2)

    # 3rd hemisphere
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_hem3 = soup.find('h2',class_='title').text

    k_soup = soup.find('a',target='_blank')
    for k in k_soup:
        hem_img3_link = k_soup["href"]

    browser.back()
    time.sleep(2)

    # 4th hemisphere
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_hem4 = soup.find('h2',class_='title').text

    l_soup = soup.find('a',target='_blank')
    for l in l_soup:
        hem_img4_link = l_soup["href"]



    mars_data ={
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "html_table": html_table,
        "hem_img1_link": hem_img1_link,
        "hem_img2_link": hem_img2_link,
        "hem_img3_link": hem_img3_link,
        "hem_img4_link": hem_img4_link
    }

       # Close the browser after scraping
    browser.quit()

    return mars_data