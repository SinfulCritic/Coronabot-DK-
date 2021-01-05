import re
import slack
import urllib.request
from bs4 import BeautifulSoup
from datetime import date

date = date.today()

content = urllib.request.urlopen('https://www.sst.dk/da/corona/status-for-epidemien/tal-og-overvaagning')

read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')

tdAll = soup.find_all('td')

raw_dnum = tdAll[21]

raw_tnum = tdAll[17]

str_tnum = raw_tnum.find('span').text

str_dnum = raw_dnum.find('span').text

tnum = float(str_tnum)

dnum = float(str_dnum)

pnum = float((dnum / tnum) * 100).__round__(2)

def slackmesseage():
    client = slack.WebClient(token='INSERT YOUR TOKEN HERE')
    client.chat_postMessage(channel='corona-bot', text=f"I dag er {dnum} personer testet positiv ud af {tnum} testede i alt. Det svarer til en positiv procent på {pnum} pct.")

def db_write():
    db = open("db.txt", "a+")
    db.write(f'DATE: {date}        Positive personer: {dnum}        Testede personer: {tnum}        Positiv procent {pnum} pct. \n')

db_write()

slackmesseage()
