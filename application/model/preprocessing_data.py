import re
from requests.exceptions import HTTPError
from discogs_api import get_vinyl, get_price

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
                    
                    try:
                        discogs_data = get_vinyl(code, discogs_token)
                    except HTTPError as http_err:
                        print(f'Preprocessing -> HTTP error occurred: {http_err}')
                        continue
                    except Exception as err:
                        print(f'Preprocessing -> Other error occurred: {err}')
                        continue

                    for disc_data in discogs_data['results']:
                        discogs_code = disc_data['catno'].replace('"', "").replace("'", "").replace("A", "").replace("B", "").replace(" ", "").replace("-", "").replace("~", "")
                        if code == discogs_code:
                            output_data.append(disc_data)
                            break
    
    return output_data

def preprocess_data(data: str, credentials: list, url: str, condition: str = "Near Mint (NM or M-)") -> dict:
    # Get the Discogs API token from the credentials list
    discogs_token = credentials[7]

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
        id = result['id']

        price = round(get_price(id, discogs_token)[condition]['value'], -1)-0.01
        uri = result['uri']
        genre = result['genre'][0]
        title = result['title']

        try: 
            country = result['country']
        except KeyError:
            pass
        try:
            year = result['year']
        except KeyError:
            pass
        try:
            label = result['label'][0] + " " + result['catno']
        except KeyError:
            pass

        title = title.replace("*", "").replace("•", "").replace("†", " ").replace("º", " ").replace("—", " ")

        information = {"label": label, "country": country, "year": year, "uri": f"https://www.discogs.com{uri}", "genre": genre, "title": title, "price": price}
        output['data'].append(information)

    return output
