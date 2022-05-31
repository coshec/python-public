"""
Take name of market and search in google - first 25 search results
"""
"""
- check position of MnM and local competition
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from urllib.parse import urlparse  # python 3.x
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import re


USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
    return search_term, response.text

def parse_results(html, keyword):
 soup = BeautifulSoup(html, 'html.parser')
 found_results = []
 rank = 1
 result_block = soup.find_all('div', attrs={'class': 'rc'})
 for result in result_block:
  link = result.find('a', href=True)
  title = result.find('h3', attrs={'class': 'LC20lb'})
  description = result.find('span', attrs={'class': 'st'})
  if link and title:
   link = link['href']
   title = title.get_text()
#print(link)
#print(title)
  if description:
   description = description.get_text()
   if link != '#':
    found_results.append({'keyword': keyword, 'rank': rank, 'title': title, 'description': description, 'link': link})
    rank += 1
 return found_results



def scrape_google(search_term, number_results, language_code):
    try:
        keyword, html = fetch_results(search_term, number_results, language_code)
        results = parse_results(html, keyword)
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")


myinfile0= open(r"E:\\kaushik kochhar\\d\\pyfiles\\Local_Competition_Master.txt","r")
competition_list = myinfile0.read()
myinfile0.close()


# df=pd.read_excel(r'‪‪E:\Kaushik Kochhar\US trip - activities\HS - Misc\Revamp - Compare with competition\20190902\Input100.xlsx',encoding='Latin-1')
‪df=pd.read_excel('E:\\Kaushik Kochhar\\US trip - activities\\Report ARR - Leads - Ranking\\CRM Exports\\2019Q2-4.xlsx',encoding='Latin-1')

df[' Title']=df['reportname'].apply(lambda x: re.findall('[\w\-\(\)\/ &]+Market',x)[0])
# df['Short Title']=df['Report Name']
gresults_list=[]
gresults_row=[]
gresults_cols=df.columns.tolist()
gresults_cols_addnl=['Rank','Link','Title','Description','Link Type','Publisher']
gresults_cols.extend(gresults_cols_addnl)
for i,rec in enumerate(range(len(df))):
# for i,rec in enumerate(range(2)):
  search_string=df.iloc[rec]['Short Title']
  gresults_row_common=df.iloc[rec].tolist()
  sleep(randint(30,60))
  results=scrape_google(search_string,25,"en")
  MnM_found=0
  competition_found=0
  competition_found_total=0
  MnM_flag="No"
  for result in results:
      #out=results[i]['keyword']+' ' +results[0]['title']+' '+results[0]['link']
      link=result['link']
      parsed_uri = urlparse(link)  # returns six components
      domain = '{uri.netloc}'.format(uri=parsed_uri)
      pure_domain=domain.split('.')
      if len(pure_domain)==3:
        linkdotcom=str(pure_domain[1])+'.'+str(pure_domain[2])
      else:
        linkdotcom=str(pure_domain[0])+'.'+str(pure_domain[1])
    #print(linkdotcom)
      competition_flag="No"
    #   print("Market: ",line.strip())
    #   print("linkdotcom: ",linkdotcom)
      Link_type="Other"
      if linkdotcom in competition_list:
    #if MnM link already found, no need to count competition; else count them till we find MnM link
          Link_type="Competition"
      elif linkdotcom == 'marketsandmarkets.com':
          Link_type="MnM"
      gresults_row_result=[result['rank'],result['link'],result['title'],result['description'],Link_type,linkdotcom]
      gresults_row=gresults_row_common+gresults_row_result
      gresults_list.append(gresults_row)
  print(i,"# ","Record processed: ",search_string)

dfo=pd.DataFrame(gresults_list,columns=gresults_cols)
dfo.to_excel(r'‪E:\Kaushik Kochhar\US trip - activities\HS - Misc\Revamp - Compare with competition\Small Domains\V4+ - Duck or orange - past version Green-Dark Green-O.xlsx',index=False)

    
