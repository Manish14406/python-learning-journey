import requests 


query = "Artificial intelligence"
api = "bef120bb1afe4aa38382c2b4fba8b9e0"


url = f"https://newsapi.org/v2/everything?q={query}&from=2026-01-24&to=2026-01-24&sortBy=popularity&apiKey={api}"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]

for article in articles:
    print(article["title"] ,article["url"])
    print("**********************************************************************")