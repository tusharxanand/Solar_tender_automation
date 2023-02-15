import pandas as pd
import webbrowser
from bs4 import BeautifulSoup
import requests
import parsedatetime as pdt

# read the excel file into pandas dataframe
df=pd.read_excel("Testing_scrape.xlsx")


file_name="Testing_scrape_2.xlsx"
headline=[]
date=[]

def extract_dates(sentence):
    cal = pdt.Calendar()
    time_struct, parse_status = cal.parse(sentence)
    if parse_status == 0:
        return None
    else:
        # return time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday
        return(f'{time_struct.tm_mday}-{time_struct.tm_mon}-{time_struct.tm_year}')




# read the links
for i in range (1,3):
    for j in range (0,2):
        link=df[f"Page {i}"][j]


        # open link in brave browser
        brave_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
        # webbrowser.get("brave").open(link)

        # scraping data from the website
        tender_html_content=requests.get(link)
        html_content=tender_html_content.content

        soup_tender_html_content=BeautifulSoup(html_content,'html.parser')
        soup_tender_html_content_h1=soup_tender_html_content.find('h1')
        soup_tender_html_content_SubHeading=soup_tender_html_content.find('div', class_="page-sub-title")
        # print(soup_tender_html_content_h1.text)
        # print(soup_tender_html_content_SubHeading.text)
        headline.append(soup_tender_html_content_h1.text)
        date.append(soup_tender_html_content_SubHeading.text)


date2=[]
for i in range(len(date)):
    date2.append(extract_dates(date[i]))


       
  
df2=pd.DataFrame({'HEADLINE':headline, 'DATE':date2})

    
print(df2)
df2.to_excel(file_name,index=False)