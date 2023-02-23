import re
from model.discogs_api import get_vinyl
from model.discogs_scraper import Scraper

def search_data(data):
    output_data = []

    punctuation = "<"'"'"'@:^`!#$%&*();?'\'[]{}=+,>"
    remove_punctuation = r"^[a-zA-Z {}]*$".format(re.escape(punctuation))

    for x in data.split(" "):
        if 5<len(x)<25:
            if not re.search(r'[^\u0000-\u007F]', x):
                if not re.match(remove_punctuation, x):
                    discogs_data = get_vinyl(x, "PhGScwKlhpPNIdWyuoTrVkzlZQZoXzAleAlrOrYW")

                    for disc_data in discogs_data['results']:
                        for barcode in disc_data['barcode']:
                            if barcode == x:
                                output_data.append(disc_data)
    
    return output_data

def preprocess_data(data: str, url: str, with_price: bool = False, condition: str = "-M"):
    if with_price:
        scraper = Scraper('https://www.discogs.com/' , 'onetrust-accept-btn-handler')

    results = search_data(data)

    label = '-'
    country = '-'
    year = '-'
    uri = '-'
    genre = '-'
    title = '-'
    price = 0
    
    output = {"url": url, "data": []}
    information = {"label": "", "country": "", "year": "", "uri": "", "genre": "", "title": "", "price": 0}

    for result in results:
        uri = result['uri']
        genre = result['genre'][0]
        title = result['title']

        try: 
            country = result['country']
        except:
            pass
        try:
            year = result['year']
        except:
            pass
        try:
            label = result['label'][0] + " " + result['catno']
        except:
            pass
        
        title = title.replace("*", "")
        title = title.replace("•", "")
        title = title.replace("†", " ")
        title = title.replace("º", " ")
        title = title.replace("—", " ")

        if with_price:
            scraper.url(f"https://www.discogs.com{uri}")
            price = scraper.get_price(condition)

        information["label"] = label 
        information["country"] = country
        information["year"] = year 
        information["uri"] = f"https://www.discogs.com{uri}"
        information["genre"] =  genre
        information["title"] = title
        information["price"] = price

        output['data'].append(information)

    return output


