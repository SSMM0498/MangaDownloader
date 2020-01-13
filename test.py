######################################################################################################################################################################################################################
#########################################                       ###########################################
#########################################   Download a file     ###########################################
#########################################                       ###########################################
######################################################################################################################################################################################################################
# Import requests, shutil python module.
import requests
import shutil
# This is the image url.
image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"
# Open the url image, set stream to True, this will return the stream content.
resp = requests.get(image_url, stream=True)
# Open a local file with wb ( write binary ) permission.
local_file = open('local_image.jpg', 'wb')
# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
resp.raw.decode_content = True
# Copy the response stream raw data to local image file.
shutil.copyfileobj(resp.raw, local_file)
# Remove the image url response object.


from urllib.request import Request, urlopen

url = "https://i4.mangapanda.com/naruto/1/naruto-1564774.jpg"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

file_name = url.split('/')[-1]
u = urlopen(req)

f = open(file_name, 'wb')
# meta = u.info()
file_size = int(u.getheader("Content-Length")[0])
# print "Downloading: %s Bytes: %d" % (file_name, file_size)
print("Downloading: " , file_name , " Bytes: " , file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break
    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%3d  [%3.0f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print(status),

f.close()

###########################################################################################################
###########################################################################################################
#########################################                       ###########################################
#########################################   Validity of a url   ###########################################
#########################################                       ###########################################
###########################################################################################################
###########################################################################################################
import requests
request = requests.get('http://www.example.com')
if request.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist')

###########################################################################################################
###########################################################################################################
#########################################                       ###########################################
#########################################      Command line     ###########################################
#########################################                       ###########################################
###########################################################################################################
###########################################################################################################
#!/usr/bin/env python
import sys

for arg in sys.argv:
    print(arg)

###########################################################################################################
###########################################################################################################
##########################################                     ############################################
##########################################    Web Scrapping    ############################################
##########################################                     ############################################
###########################################################################################################
###########################################################################################################
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

# I hope you guys enjoyed this article on “Web Scraping with Python”. I hope this blog was informative and has added value to your knowledge. Now go ahead and try Web Scraping. Experiment with different modules and applications of Python. 