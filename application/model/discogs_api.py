import requests

def get_vinyl(query: str, discogs_token: str) -> dict:
    headers = {
        "Authorization": f"Discogs token={discogs_token}",
        "Content-Type": "application/json"
    }

    url = f"https://api.discogs.com/database/search?query={query}&format=lp&type=release"
    response = requests.get(url, headers=headers)

    return response.json()


def get_cd(barcode: str, discogs_token: str) -> dict:
    headers = {
        "Authorization": f"Discogs token={discogs_token}",
        "Content-Type": "application/json"
    }

    url = f"https://api.discogs.com/database/search?barcode={barcode}&format=cd&type=release"
    response = requests.get(url, headers=headers)

    return response.json()
