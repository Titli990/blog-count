import requests
import json

def fetch_posts(client_name):

    # Load clients
    with open("client.json", "r") as f:
        clients = json.load(f)

    # Get client URL
    base_url = clients[client_name]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f"{base_url}/wp-json/wp/v2/posts?per_page=100"

    response = requests.get(url, headers=headers)

    posts = response.json()

    return posts