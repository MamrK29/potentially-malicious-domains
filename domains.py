import requests, zipfile, re
from bs4 import BeautifulSoup
domain_webpage = requests.get("https://www.whoisds.com/newly-registered-domains")
page_content = BeautifulSoup(domain_webpage, 'html.parser')
# find all the instances of the td 
# For the free domains, the latest few days are listed under a table 
table = soup.find_all('td')
# latest date is the third entry
lastest_link = table[3]
link_tag = lastest_link.find(href=True)
# get the link without tags
link = link_tag['href']

# Download the zip file that it occurs in
r = requests.get(link, allow_redirects=True)

# write the downloaded content to the file 
open('date.zip', 'wb').write(r.content)

# unzip the file 
with zipfile.Zipfile('date.zip', 'r') as zip_ref:
    zip_ref.extractall()

## read the file 
fileO =  open("domain-names.txt", "r")
contents = fileO.read()

# find all the contents relating to banks
x = re.find_all(r"\b([A-Za-z0-9]+bank.*)\b", text)

# print the contents
for i in range (0, len(x)):
    print(x[i)

## Connect to whois to gather registrar information
## Connect to Urlscan to get images 
