from bs4 import BeautifulSoup
import requests

website = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/271/curitiba-pr").content
soup = BeautifulSoup(website, "html.parser")

temperature_min = soup.find("span", class_="-gray-light")

print(f"minimum temperature: {temperature_min.string}")
