
from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def check_school(url):
 #url="https://www.apartments.com/the-legends-at-willow-creek-folsom-ca/5943frp"
 html = requests.get(url,headers=headers, timeout=5, allow_redirects = True )
 soup=BeautifulSoup(html.text)
 try:
  schools=soup.find('div',attrs={'class':'profilev2SchoolCard'}). \
             find_all('div',attrs={'class':'card'})
  for school in schools:
   if 'Elementary' in school.text:
    school_name=school.find('div',attrs={'class':'title'}).text
    school_rating=school.find('div',attrs={'class':'schoolScore'}).text
    if school.find('i',attrs={"class":"attendanceZoneIcon"}):
       az=True
    else:
       az=False
    if int(school.find('div',attrs={'class':'schoolScore'}).text)>6:
      return True,school_name,school_rating, az
 except:
  pass 
 return False,'','',False



response=requests.get(url,headers=headers, timeout=5, allow_redirects = True )
soup=BeautifulSoup(response.text,'html.parser')

soup=BeautifulSoup(pyperclip.paste(),'html.parser')
links=[s['href'] for s in soup.find_all('a',attrs={'class':"property-link"})]
links=list(np.unique(np.array(links)))
shortlist=[]
rec={}
for i,link in enumerate(links):
  sleep(3)
  good_school,school_name,school_rating,az=check_school(link)
  if good_school:
    rec['link']=link
    rec['school_name']=school_name
    rec['school_rating']=school_rating
    rec['attendance_zone']=az
    shortlist.append(rec)
    rec={}
  print(f'{i} of {len(links)}. {link}')

df=pd.DataFrame(shortlist)
df.to_clipboard()
    