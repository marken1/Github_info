from bs4 import BeautifulSoup
import requests
import re


def cont(url):
    profile = requests.get(url)
    soup = BeautifulSoup(profile.content, 'html.parser')
    find_el = soup.find('h2', class_='f4 text-normal mb-2')
    delete_string = re.findall(r'\d+', str(find_el.text))
    strings = [str(integer) for integer in delete_string]
    a_string = "".join(strings)
    con = int(a_string)
    return con



def repo(url):
    profile = requests.get(url)
    soup = BeautifulSoup(profile.content, 'html.parser')
    rep = soup.find('span', class_='Counter')
    return rep.text


def stars(url):
    profile = requests.get(url)
    soup = BeautifulSoup(profile.content, 'html.parser')
    stars = soup.find('span', class_='text-bold color-text-primary')
    return stars.text
