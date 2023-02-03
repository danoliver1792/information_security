from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def clear_text(text):
    text = text.split()
    text_clear = []
    text = re.sub("\n+", " ", text)
    text = re.sub(" +", " ", text)
    text = text.replace(u"\xa0", u"")
    text = re.sub("\[[0-9]*\]", "", text)
    text = text.split(" ")

    for item in text:
        item = item.strip()
        item = item.strip(string.punctuation)

        if len(item) > 1 or (item.lower() == "a" or item.lower() == "e"
                             or item.lower == "o"):
            text_clear.append(item)

    return text_clear


html = urlopen("https://pt.wikipedia.org/wiki/python")
bs_object = BeautifulSoup(html)
content = bs_object.find("div", {"id": "mw-content-text"}).get_text()
content = clear_text(content)

print(content)
