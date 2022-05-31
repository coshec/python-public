"""
Take name of market and search in google - first 25 search results
- check position of MnM and local competition
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from urllib.parse import urlparse  # python 3.x
import csv
import pandas as pd
import numpy as np
import re
from koogle import scrape_google
from collections import Counter

def get_domain_type(link):
#   print('Parsing Link: ',link)
    parsed_uri = urlparse(link)  # returns six components
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    pure_domain=domain.split('.')
    if len(pure_domain)==3:
        linkdotcom=str(pure_domain[1])+'.'+str(pure_domain[2])
    elif len(pure_domain)==2:
        linkdotcom=str(pure_domain[0])+'.'+str(pure_domain[1])
    else:
        linkdotcom=link
    Link_type="Other"
    if linkdotcom == "marketsandmarkets.com":
        Link_type="MnM"
    elif linkdotcom in competition_list:
        Link_type="Competition"
    return Link_type,linkdotcom


with open(r"E:\\kaushik kochhar\\d\\pyfiles\\Local_Competition_Master.txt","r") as myinfile0:
    competition_list = myinfile0.read()

Mapping={}
with open(r'‪E:\Kaushik Kochhar\HS\ARR Review\Category-Domain mapping.csv') as f:
   category_dict = csv.DictReader(f)
   for category in category_dict:
       Mapping[category['Category']]=category['MnM Domain']


filename=r'‪E:\Kaushik Kochhar\US trip - activities\Report ARR - Leads - Ranking\CRM Exports\20191002.xlsx'
filename_o=filename.split('\\')[-1].split('.')[0]+'-out.xlsx'
Detailfile=filename.split('\\')[-1].split('.')[0]+'-Detail.csv'

df=pd.read_excel(filename,encoding='Latin-1')

''' Put your filter conditions here ===
'''
df.PublishDate=pd.to_datetime(df.PublishDate)
dfg=df[(df.PublishDate.dt.year.isin([2018,2019])) & (df.PublishDate<'2019-10-01') ]
dfg=dfg[dfg.AllSaleCount>0]
dfg.shape
dfg.sort_values(['ReportCode','verson'],ascending=[True,False],inplace=True)
dfg.drop_duplicates(['ReportCode'],inplace=True)
dfg.reset_index(inplace=True,drop=True)
dfg.sort_values(['AllSaleCount','Inbound'],ascending=[False,False],inplace=True)
# dfg=df[(df['Google Trend']=='Active') | (df['Google Trend']=='Positive')][['MainTitle']]
#
dfg['ShortTitle']=dfg['reportname'].map(lambda x: re.findall('[\w\-\(\)\/, &]+[Mm]arket|$',x)[0])
# dfg['ShortTitle']=dfg['MainTitle']+str(' Market')
#
print_freq=1
#
dfg.reset_index(inplace=True,drop=True)
dfg['MnMDomain']=dfg.Category.map(Mapping)
dfg['MnMRank']=""
dfg['MnMReportName']=""
dfg['CompetitorsAbove']=""
dfg['TotalCompetitors']=""
dfg['Ad-MnMRank']=""
dfg['Ad-CompetitorsAbove']=""
dfg['Ad-TotalCompetitors']=""

# Detailfile=r'E:\Kaushik Kochhar\US trip - activities\HS - Misc\ICT 2014-16 title analysis - for Balaji\2014-16reports.csv'
Detailfile=r'E:\Kaushik Kochhar\scratch\dummy.csv'
myoutfile2 = open(Detailfile, "a",encoding='utf-8')

found=0
c=Counter()
for rec in range(len(dfg)):
    # if dfg.loc[rec,'ShortTitle'] == np.nan:
    #     print('Blank Rec. Rec: ',rec," :: ",dfg.loc[rec,'ShortTitle'])
    #     continue
    search_string=dfg.loc[rec,'ShortTitle']
    results,adresults=scrape_google(search_string,25,"en")
    MnM_found, competition_found, competition_found_total=0,0,0
    MnM_flag=False
    MnM_Title=[] #if there are multiple results, capture all
    for result in results:
        Link_type,domain=get_domain_type(result['link'])
        if Link_type=="MnM":
            MnM_found=result['rank']
            MnM_Title.append(re.findall('[\w\-\(\)\/ &\,]+[Mm]arket|$',result['title'])[0]) # pull out title, handle characters{-,&,(,),/,','} and After[m]arket
            MnM_flag=True
        elif Link_type=="Competition":
            competition_found_total+=1
            if not(MnM_flag): # we found a competition but yet to see MnM link so count as competitor above
                competition_found+=1
                c.update([domain])
        out_string=dfg.loc[rec,'ShortTitle']+"`"+ str(result['rank'])+"`"+result['link']+"`"+result['title']+"`"+result['description']
        out_string=out_string+"`"+Link_type
        _=myoutfile2.write(out_string)
        _=myoutfile2.write('\n')
    #write summary record
    if MnM_found==0:
        MnM_found='25+'
    dfg.loc[rec,'MnMRank']=str(MnM_found)
    if MnM_Title:
        dfg.loc[rec,'MnMReportName']= MnM_Title[0]# capture top MnM result market
    dfg.loc[rec,'CompetitorsAbove']=str(competition_found)
    dfg.loc[rec,'TotalCompetitors']=str(competition_found_total)
#
    ad_MnM_found, ad_competition_found, ad_competition_found_total=0,0,0
    ad_MnM_flag=False
    for adresult in adresults:
        Link_type,_=get_domain_type(adresult['link'])
        if Link_type=="MnM":
            ad_MnM_found=adresult['rank']
            ad_MnM_flag=True
        elif Link_type=="Competition":
            ad_competition_found_total+=1
            if not(ad_MnM_flag): # we found a competition but yet to see MnM link so count as competitor above
                ad_competition_found+=1
        out_string=dfg.loc[rec,'ShortTitle']+"`"+ str(adresult['rank'])+"`"+adresult['link']+"`"+adresult['title']+"`"+adresult['description']
        out_string=out_string+"`"+Link_type
        _=myoutfile2.write(out_string)
        _=myoutfile2.write('\n')
    #write summary record
    if ad_MnM_found==0:
        ad_MnM_found='?'
    dfg.loc[rec,'Ad-MnMRank']=str(ad_MnM_found)
    dfg.loc[rec,'Ad-CompetitorsAbove']=str(ad_competition_found)
    dfg.loc[rec,'Ad-TotalCompetitors']=str(ad_competition_found_total)
#
    if rec%print_freq==0:
        print("Records processed: ",rec)
        print('----------------------- Last Title processed: ',dfg.loc[rec,'ShortTitle'])
        if MnM_found != 1:
            found+=1
            print('Report Found with Rank > 1; Total till now: ',found, 'This one at rank: ',MnM_found)
            if found==550:
                break
    sleep(randint(30,60))

cols=['MnMDomain','ReportCode', 'ShortTitle', 'verson', 'PublishDate',
       'LeadCount', 'AllSaleCount', 'Inbound', 'Reseller', 'other', 'pageviews', 
       'MnMRank', 'MnMReportName', 'CompetitorsAbove', 'TotalCompetitors',
       'Ad-MnMRank', 'Ad-CompetitorsAbove', 'Ad-TotalCompetitors',
        'Category', 'SubCategory']

# cols2=['Revenue', 'Revenue_per_Month', 'InboundRevenue', 'ResellerRevenue', 'otherRevenue']
# cols+=cols2

dfg.to_excel(filename_o,columns=cols,index=False)
myoutfile2.close()

