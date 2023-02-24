import re
from model.discogs_api import get_vinyl
from model.discogs_scraper import Scraper

def search_data(data: str, discogs_token: str) -> list[dict]: 
    output_data = []
    punctuation = "<"'"'"'@:^`!#$%&*();?'\'[]{}=+,>"
    remove_punctuation = r"^[a-zA-Z {}]*$".format(re.escape(punctuation))

    data = data.replace("}", "")
    data = data.replace("{", "")

    for code in data.split(","):
        if 5 < len(code) < 25:
            if not re.search(r'[^\u0000-\u007F]', code):
                if not re.match(remove_punctuation, code):
                    code = code.replace('"', "").replace("'", "").replace("A", "").replace("B", "").replace(" ", "").replace("-", "").replace("~", "")
                    
                    # Search the Discogs API for vinyl records matching the code
                    discogs_data = get_vinyl(code, discogs_token)

                    for disc_data in discogs_data['results']:
                        discogs_code = disc_data['catno'].replace('"', "").replace("'", "").replace("A", "").replace("B", "").replace(" ", "").replace("-", "").replace("~", "")
                        if code == discogs_code:
                            output_data.append(disc_data)
                            break
    
    return output_data

def preprocess_data(data: str, credentials: list, url: str, with_price: bool = False, condition: str = "-M") -> dict:
    # Get the Discogs API token from the credentials list
    discogs_token = credentials[7]
    
    if with_price:
        scraper = Scraper('https://www.discogs.com/' , 'onetrust-accept-btn-handler')

    # Search the Discogs API for vinyl records matching the input codes
    results = search_data(data, discogs_token)

    label = '-'
    country = '-'
    year = '-'
    uri = '-'
    genre = '-'
    title = '-'
    price = 0
    
    output = {"url": url, "data": []}

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
        
        title = title.replace("*", "").replace("•", "").replace("†", " ").replace("º", " ").replace("—", " ")

        # Get the record price if with_price is True
        if with_price:
            scraper.url(f"https://www.discogs.com{uri}")
            price = scraper.get_price(condition)

        information = {"label": label, "country": country, "year": year, "uri": f"https://www.discogs.com{uri}", "genre": genre, "title": title, "price": price}
        output['data'].append(information)

    return output
