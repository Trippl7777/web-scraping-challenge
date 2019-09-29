

import pandas as pd 
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


data_collection = {}

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'



# response = requests.get(url)
#
# soup = bs(response.text, 'lxml')
#
# type(soup)
#
#
# title_data = soup.find_all('div', class_='content_title')
# info_data = soup.find_all('div', class_='image_and_description_container')
# info_data
#
#
# title = []
# for i in title_data:
#     # Error handling
#     try:
#
#         news_title = i.find('a').text
#         title.append(news_title)
#
#
#         if (news_title):
#             # Print results
#             print('-------------')
#             print(news_title)
#
#
#     except Exception as e:
#         print(e)
#
#
# desc = []
# for x in info_data:
#     try:
#
#         info_p = x.find('div').text
#
#         desc.append(info_p)
#
#         if (info_p):
#             # Print results
#             print('-------------')
#             print(info_p)
#
#
#     except Exception as e:
#         print(e)
#
#
# type(soup)
#
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
#
#
# #Use splinter to navigate the site and find the image url for the current
# #Featured Mars Image and assign the url string to a variable called featured_image_url.
#
# new_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# browser.visit(new_url)
#
#
# response2 = requests.get(new_url)
#
# soup2 = bs(response2.text, 'lxml')
#
# type(soup2)
#
# import time
#
#
#
# html = browser.html
# soup = bs(html, 'html.parser')
# time.sleep(2)
# f_img = soup.find_all('a', class_='button fancybox')
#
#
#
# browser.click_link_by_partial_text('FULL IMAGE')
#
#
# # Don't actually need to save it -____- *sigh*
# # url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA03519_ip.jpg"
# # uopen = urllib.request(url)
# # stream = uopen.read()
# # file = open('filename','w')
# # file.write(stream)
# # file.close()
#
#
# # In[119]:
#
#
# time.sleep(2)
#
# browser.click_link_by_partial_text('more info')
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
# main_image_url = soup.find('img', class_='main_image')
# stock_pg_url = "https://www.jpl.nasa.gov"
#
#
# # ------------------
#
#
# main_image_url_clean = main_image_url['src']
#
#
# # ------------
#
#
# pic_url = stock_pg_url + main_image_url_clean
# featured_image_url = pic_url
#
#
# #------------------
#
#
#
# #Twitter URL
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
#
# twitter_url = 'https://twitter.com/marswxreport?lang=en'
# browser.visit(twitter_url)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
#
# # ----------------
#
# #mars weather info from tweet minus extra link
#
# mars_weather_raw = soup.find('p', class_='tweet-text').text
# mars_weather1 = mars_weather_raw.split("pic")
#
# mars_weather = mars_weather1[0]
#
# print(mars_weather)
#
#
# pandas_url = 'https://space-facts.com/mars/'
#
#
# # ---------------
#
#
# mars_table = pd.read_html(pandas_url)
#
#
# # ------------------
#
#
# #Scraping for Diameter, Mass, etc
#
# print(mars_table)
#
#
# # -------------
#
#
# mars_table2 = mars_table[0]
# print(mars_table2)
#
# mars_table2.columns = ['Info', 'Mars', 'Earth']
#
#
# mars_df = mars_table2.drop(['Earth'], axis=1)
#
# print(mars_df)
#
# mars_html = mars_df.to_html()
#
# print(mars_html)
#
# #Get Mars hemisphere info --
#
# OG_URL = 'https://astrogeology.usgs.gov'
#
# hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
#
# browser.visit(hemisphere_url)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
#
# #Clicky boi 1
#
# browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
#
# time.sleep(2)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
# image1 = soup.find('img', class_='wide-image')
# title1 = soup.find('h2', class_='title').text
#
#
# img1_url = OG_URL + image1['src']
# img1_url
#
#
# # ----------------------------
#
# #Clicky boi 2
#
#
#
#
# hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
#
# browser.visit(hemisphere_url)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
# browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
#
# time.sleep(2)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
# image2 = soup.find('img', class_='wide-image')
# title2 = soup.find('h2', class_='title').text
# image2
#
#
# # -----------------------------------
#
# img2_url = OG_URL + image2['src']
# img2_url
#
# #Clicky boi 3
#
# hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
#
# browser.visit(hemisphere_url)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
#
# # -----------------------
#
# browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
#
# time.sleep(2)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
# image3 = soup.find('img', class_='wide-image')
# title3 = soup.find('h2', class_='title').text
#
#
#
# img3_url = OG_URL + image3['src']
# img3_url
#
# #Clicky boi 4
#
#
# hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
#
# browser.visit(hemisphere_url)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
#
# browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
#
# time.sleep(2)
#
# html = browser.html
# soup = bs(html, 'html.parser')
#
# image4 = soup.find('img', class_='wide-image')
# title4 = soup.find('h2', class_='title').text
#
#
# # -------------------------
#
#
# img4_url = OG_URL + image4['src']
# img4_url
#
# #-------------------------
# #Dictionary
#
# hemisphere_image_urls = [
#     {'title': title1, 'img_url': img1_url},
#     {'title': title2, 'img_url': img2_url},
#     {'title': title3, 'img_url': img3_url},
#     {'title': title4, 'img_url': img4_url}
# ]
#
#
# print(hemisphere_image_urls)
# browser.quit()

# New Code

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():



    browser=init_browser()

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)

    soup = bs(response.text, 'lxml')

    type(soup)

    title_data = soup.find_all('div', class_='content_title')
    info_data = soup.find_all('div', class_='image_and_description_container')


    title = []
    for i in title_data:
        # Error handling
        try:

            news_title = i.find('a').text
            title.append(news_title)

            if (news_title):
                # Print results
                print('-------------')
                print(news_title)


        except Exception as e:
            print(e)

    desc = []
    for x in info_data:
        try:

            info_p = x.find('div').text

            desc.append(info_p)

            if (info_p):
                # Print results
                print('-------------')
                print(info_p)


        except Exception as e:
            print(e)

    type(soup)

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Use splinter to navigate the site and find the image url for the current
    # Featured Mars Image and assign the url string to a variable called featured_image_url.

    new_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(new_url)

    response2 = requests.get(new_url)

    soup2 = bs(response2.text, 'lxml')

    type(soup2)

    import time

    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(2)
    f_img = soup.find_all('a', class_='button fancybox')

    browser.click_link_by_partial_text('FULL IMAGE')

    # Don't actually need to save it -____- *sigh*
    # url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA03519_ip.jpg"
    # uopen = urllib.request(url)
    # stream = uopen.read()
    # file = open('filename','w')
    # file.write(stream)
    # file.close()

    # In[119]:

    time.sleep(2)

    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = bs(html, 'html.parser')

    main_image_url = soup.find('img', class_='main_image')
    stock_pg_url = "https://www.jpl.nasa.gov"

    # ------------------

    main_image_url_clean = main_image_url['src']

    # ------------

    pic_url = stock_pg_url + main_image_url_clean
    featured_image_url = pic_url

    # ------------------

    # Twitter URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # ----------------

    # mars weather info from tweet minus extra link

    mars_weather_raw = soup.find('p', class_='tweet-text').text
    mars_weather1 = mars_weather_raw.split("pic")

    mars_weather = mars_weather1[0]

    print(mars_weather)

    pandas_url = 'https://space-facts.com/mars/'

    # ---------------

    mars_table = pd.read_html(pandas_url)

    # ------------------

    # Scraping for Diameter, Mass, etc

    print(mars_table)

    # -------------

    mars_table2 = mars_table[0]
    print(mars_table2)

    mars_table2.columns = ['Info', 'Mars', 'Earth']

    mars_df = mars_table2.drop(['Earth'], axis=1)

    print(mars_df)

    mars_html = mars_df.to_html()

    print(mars_html)

    # Get Mars hemisphere info --

    OG_URL = 'https://astrogeology.usgs.gov'

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(hemisphere_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # Clicky boi 1

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    image1 = soup.find('img', class_='wide-image')
    title1 = soup.find('h2', class_='title').text

    img1_url = OG_URL + image1['src']
    img1_url

    # ----------------------------

    # Clicky boi 2

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(hemisphere_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    image2 = soup.find('img', class_='wide-image')
    title2 = soup.find('h2', class_='title').text
    image2

    # -----------------------------------

    img2_url = OG_URL + image2['src']
    img2_url

    # Clicky boi 3

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(hemisphere_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # -----------------------

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    image3 = soup.find('img', class_='wide-image')
    title3 = soup.find('h2', class_='title').text

    img3_url = OG_URL + image3['src']
    img3_url

    # Clicky boi 4

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(hemisphere_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')

    image4 = soup.find('img', class_='wide-image')
    title4 = soup.find('h2', class_='title').text

    # -------------------------

    img4_url = OG_URL + image4['src']
    img4_url

    # -------------------------
    # Dictionary

    hemisphere_image_urls = [
        {'title': title1, 'img_url': img1_url},
        {'title': title2, 'img_url': img2_url},
        {'title': title3, 'img_url': img3_url},
        {'title': title4, 'img_url': img4_url}
    ]

    data_collection = {
        'title1': title1, 'img_url1': img1_url,
        'title2': title2, 'img_url2': img2_url,
        'title3': title3, 'img_url3': img3_url,
        'title4': title4, 'img_url4': img4_url,
        "news_title1": news_title, 'info1': info_p,
        "main_image_URL": pic_url,
        "facts": mars_html,
        "weather": mars_weather
    }
    # news_title and info_p

    browser.quit()
    return data_collection

# scrape()









