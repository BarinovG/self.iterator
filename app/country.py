import json

uri = "https://en.wikipedia.org/wiki/"   

class Country_Wiki:
  
  def __init__(self, countries):
    self.countries = countries
    self.cursor = 0
    self.limit = len(countries)

  def __iter__(self):
    return self

  def __next__(self):

    if self.cursor >= self.limit:
      raise StopIteration

    name = self.countries[self.cursor]['name']['official']
    name_url = uri + name
    self.cursor += 1

    return name, name_url

def get_links(countries_list): 
  with open("country_with_wikilink.json", 'w', encoding='utf-8' ) as f: 
    for country in Country_Wiki(countries_list):
      print(country)
      json.dump(country, f, indent=1, ensure_ascii=False)
  print(f'country_with_wikilink.json is created.')

