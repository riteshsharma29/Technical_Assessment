#!/usr/bin/python

'''
API to search string on Google and scrape the results
'''

#importing required modules 
from urllib.parse import urlparse
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
import re

class Search_Api():

    #method to search string on Google 
    def get_results(self,string):

        ua = UserAgent()

        base_url = "https://www.google.com/search?q=" + string 
        response = requests.get(base_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")

        result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})		

        #defining empty lists		
        links = []
        titles = []	
        descriptions = []		

        for r in result_div:
        # Error handling
            try:
                link = r.find('a', href = True)
                title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
                description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
        
            # Appending results 
                if link != '' and title != '' and description != '': 
                   links.append(link['href'])
                   titles.append(title)
                   descriptions.append(description)
            except Exception as e: 
                print(e)
				
        to_remove = []
        clean_links = []
        for i, l in enumerate(links):
            clean = re.search('\/url\?q\=(.*)\&sa',l)

        # Anything that doesn't fit the above pattern will be removed
            if clean is None:
                to_remove.append(i)
                continue
            clean_links.append(clean.group(1))

        # Remove the corresponding titles & descriptions
        for x in to_remove:
            del titles[x]
            del descriptions[x]				
				
        odf = pd.DataFrame({"Titles":titles,"Descriptions":descriptions,"Links":clean_links})	
        #creating DataFrame object and scraping for Top five results		
        df = odf.head()		
			
        return df      			
		
    #method to parse each results 		
    def parse_results(self,link):	

        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        page_links = []	
        clean_page_links = []		
        for link in soup.findAll('a'):
            if link is not None:	
                page_links.append(link.get('href'))
        for l in page_links:
            try:
                if l.startswith('http'):
                    clean_page_links.append(l)
            except:
                continue	
        #remove Duplicates				
        clean_page_links = list(set(clean_page_links))				
        pagedf = pd.DataFrame({"Information on the result Page - Links":clean_page_links})			
			
        return pagedf
		