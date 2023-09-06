#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import the BeautifulSoup for web scrapping

from bs4 import BeautifulSoup


# In[3]:


#importing the libraries 

import re

import requests

import pandas as pd

import numpy as np


# In[4]:


#features to take for the mobile devices
names = []
ratings =[]
prices = []
rating_number= []
review_number = []

random_m = []
display_m = []
camera_m = []
battery_m = []
processor_m=[]
    
#from page 1-10 information about the mobiles    
for i in range(1,11):
    
    #target url
    url  = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
    r = requests.get(url)
    soup =BeautifulSoup(r.text,"html.parser")
   
    #container 
    box= soup.find('div' , class_ ='_1YokD2 _3Mn1Gg')

    print(url)
   
    print(str(i))
    
    
    
    print("--------NAME---------------")
#   name of the mobile

    name = box.find_all('div',class_ = '_4rR01T')
    for n in name:
        names.append(n.text)
        
    print(names)
   



    print("--------rating---------------")

    rating=box.find_all('div',class_ ='_3LWZlK')

    for r in rating:
        ratings.append(r.text)
    print(ratings)

    
    
#   price of the mobile
    
    print("--------price---------------")
    
    price = box.find_all('div',class_ = '_30jeq3 _1_WHN1')
    for p in price:
        prices.append(p.text.replace('₹',''))
    print(prices)
    
    
#   review and rating number from the customers
    
    print("---------rev and rat--------------")
    randnum = box.find_all('span',class_ = '_2_R_DZ')
    
    for r in randnum:
    
    # Split the text by spaces and get the first part
        parts = r.text.split()
        rating_number.append(parts[0])
        review_number.append(parts[-2])
    print(rating_number)
    print(review_number)
    
    
    
    #RAM of the mobile
    print("----------ram----------------------")
    
    
    product_details = box.find_all("ul", class_="_1xgFaf")
    ram_list = []
    rom_list = []
    camera_list = []
    battery_list = []
    processor_list = []


    for product in product_details:
    # Extract the text from the first <li> element within the <ul>
        ram_info = product.find("li", class_="rgWa7D")
        if ram_info:
            ram_text = ram_info.text
        # Use regular expression to extract the numeric part before "GB"
            ram_value = re.search(r'(\d+)\s*GB', ram_text)
            if ram_value:
                ram_list.append(ram_value.group(1))

    # Print the extracted RAM information
    for ram in ram_list:
            random_m.append(ram)


#display , camera , battery ,processor
    
    # Iterate through each product details block
    for product in product_details:
        # Extract the text from each <li> element within the <ul>
        details = product.find_all("li", class_="rgWa7D")
        if len(details) >= 6:

            display, camera, battery, processor = [detail.text for detail in details[1:5]]
            rom_list.append(display)
            camera_list.append(camera)
            battery_list.append(battery)
            processor_list.append(processor)

    print(" RAM ")
    print(random_m)
    
    print ( "--------------display-------------")
    
    print ( "--------------camera-------------")
    
    print ( "--------------battery-------------")
    
    print ( "--------------processor-------------")
    for i in range(len(rom_list)):
        display_m.append(rom_list[i])
        camera_m.append(camera_list[i])
        battery_m.append(battery_list[i])
        processor_m.append(processor_list[i])
    print(random_m,display_m,camera_m,battery_m,processor_m)
    
    


# In[5]:


# Find the minimum length among the lists

# because the list are of different size so we have to 

# make the size of the list same 

#In order to make the dataframe 


min_length = min(len(names), len(ratings), len(prices), len(random_m), len(display_m), len(camera_m), len(battery_m), len(processor_m), len(rating_number), len(review_number))

# Trim the lists to the minimum length
names = names[:min_length]

ratings = ratings[:min_length]

prices = prices[:min_length]

random_m = random_m[:min_length]

display_m = display_m[:min_length]

camera_m = camera_m[:min_length]

battery_m = battery_m[:min_length]

processor_m = processor_m[:min_length]

rating_number = rating_number[:min_length]

review_number = review_number[:min_length]

# Now all lists have the same length (min_length)


#making the dataframe
df = pd.DataFrame({
    "Name": names,
    "Rating": ratings,
    "Price": prices,
    "RAM": random_m,
    "Display": display_m,
    "Camera": camera_m, 
    "Battery": battery_m,  
    "Processor": processor_m,  
    "Number of People Rated": rating_number,
    "Number of People Review": review_number
})


# In[57]:


print(df)


# In[6]:



#saving the file in csv format
df.to_csv('D:/flipkartmobiledataflipkart_mobile_data.csv')


# In[ ]:





# In[ ]:




