import re
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import send_email

# Define the URL
url = "https://www.pararius.com/apartments/den-haag/1000-2000"
# Send a GET request to the page
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the listings container
    listings = soup.find_all("section", class_="listing-search-item")[:8]
    # Loop through listings and extract relevant information
    titles = []
    prices = []
    areas = []

    for listing in listings:
        
        # Extract listing title (address or description)
        title = listing.find("a", class_="listing-search-item__link--title")
        title_text = title.get_text(strip=True) if title else "No title found"
        titles.append(title_text)
        
        # Extract price
        price = listing.find("div", class_="listing-search-item__price")
        price_text = price.get_text(strip=True) if price else "No price found"
        prices.append(price_text)

        # Extract m2 
        features = listing.find("div", class_="listing-search-item__features")
        area = features.find("li", class_="illustrated-features__item--surface-area").get_text(strip=True) if features else "No area found"    
        areas.append(area)

    df = pd.DataFrame({'house': titles, 'price': prices, 'area': areas})
    df_saved_name = 'houses_area_more_recent.csv'
    new_houses = False
    try:
        # read old csv and compare with new
        previuos_offer = pd.read_csv(df_saved_name)
        print('PREVIOUS OFFER CALCULATED CORRECTLY')
        if previuos_offer.equals(df):
            print('NO NEW OFFER')
            # no new listings
            new_houses = False
        else:
            print('NEW OFFERS')
            new_houses = True
            df.to_csv(df_saved_name, index=False)
    except:
        print('THERE IS AN ERROR IN COMPARING DATAFRAMES')
        # csv does not exist -> no record
        df.to_csv(df_saved_name)
    # now send me an email if new houses
    if new_houses:
        send_email.send_email(send_email.subject, send_email.body, "<INSERT YOUR EMAIL>")
    else:
        pass

else:
    print("Failed to retrieve the page")
