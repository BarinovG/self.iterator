from app.country import get_links
from app.md5_create import md5_create
import json

with open("countries.json") as f:
    countries = json.load(f)

if __name__ == "__main__":
    get_links(countries)
    md5_create("country_with_wikilink.json")
