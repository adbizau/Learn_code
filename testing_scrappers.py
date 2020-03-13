from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import requests
import re
import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import time


SiteAuthorisation = ['antillephone.com',
                     'authorisation.mga']  # mga and
authorisation_cur = []
authorisation_mga = []
mga_urls = []
urls = []
licType = []
dataDic = {}

domain = 'https://www.luckylouis.com/'
page = requests.get(domain)
soup = BeautifulSoup(page.content, 'html.parser')
for url in soup.find_all('a'):  # gasit toate linlk-urile din site
    urls.append(url.get('href'))

for url in urls:     # facem liste separate pentru fiecare licenta sa le accesam separat
    try:
        if len(url) > 11:
            if SiteAuthorisation[0] in url:
                authorisation_cur.append(url)
            elif SiteAuthorisation[1] in url:
                authorisation_mga.append(url)
    except:
        continue

print(authorisation_mga, '   ', authorisation_cur)
if len(authorisation_cur) > 0:
    for auth in authorisation_cur:  # scrapperul pentru Curacao
        print(auth)
        try:
            # col si flex row sunt locatiile retranse
            page = requests.get(auth)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find('div', class_='col-md-9')
            detalii = results.find_all('div', class_='flex-row')
            # print(len(validator)) #vezi daca primeste 2 raspunsuri
            company = detalii[0].text.strip().split('\n')[1]
            address = detalii[2].text.strip().split('\n')[1]
            email = re.findall('[\w\.-]+@[\w\.-]+', soup.text)[0]
            websites = re.findall('www.[\w\.-]+', soup.text)
            dataDic[email] = [company, '  '*20, address, websites]
        except:
            continue
if len(authorisation_mga) > 0:
    for auth in authorisation_mga:
        # print(auth)
        page = requests.get(auth)
        soup = BeautifulSoup(page.content, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
        #email = re.findall('[\w\.-]+@[\w\.-]+', soup.text)


# print(mga_urls)
