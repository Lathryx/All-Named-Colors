import requests # import requests library to get Wikipedia pages 
from bs4 import BeautifulSoup # import BeatifulSoup to scrape webpages 
import json # import JSON to convert results to a JSON file 

A2F_URL = "https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F" # All colors A-F URL 
G2M_URL = "https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M" # All colors G-M URL 
N2Z_URL = "https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z" # All colors N-Z URL 

A2F_page = requests.get(A2F_URL) # Get A-F page contents 
G2M_page = requests.get(G2M_URL) # Get G-M page contents 
N2Z_page = requests.get(N2Z_URL) # Get N-Z page contents 

A2F_soup = BeautifulSoup(A2F_page.content, "html.parser") # Parse A-F contents using BeatifulSoup 
G2M_soup = BeautifulSoup(G2M_page.content, "html.parser") # Parse G-M contents using BeautifulSoup 
N2Z_soup = BeautifulSoup(N2Z_page.content, "html.parser") # Parse N-Z contents using BeatifulSoup 

A2F_table = A2F_soup.find("table") # Scrape A-F colors table 
G2M_table = G2M_soup.find("table") # Scrape G-M colors table 
N2Z_table = N2Z_soup.find("table") # Scrape N-Z colors table 

A2F_rows = A2F_table.find_all("tr") # Scrape A-F colors table's rows (holds hex value) 
G2M_rows = G2M_table.find_all("tr") # Scrape G-M colors table's rows (holds hex value) 
N2Z_rows = N2Z_table.find_all("tr") # Scrape N-Z colors table's rows (holds hex value) 

A2F_hexVals = [] # Initialize array for A-F hex values 
G2M_hexVals = [] # Initialize array for G-M hex values 
N2Z_hexVals = [] # Initialize array for N-Z hex values 

A2F_colorNames = A2F_table.find_all("th") # Scrape A-F colors table's heads (holds name value) 
G2M_colorNames = G2M_table.find_all("th") # Scrape G-M colors table's heads (holds name value) 
N2Z_colorNames = N2Z_table.find_all("th") # Scrape N-Z colors table's heads (holds name value) 

colorNamesTxt = [] # Initialize array for all colors' names 
for item in A2F_colorNames[10:]: # Loop through A-F page elements to get name text 
    colorNamesTxt.append(item.find("a").text) # Add item to colorNamesTxt array 
for item in G2M_colorNames[10:]: # Loop through G-M page elements to get name text 
    colorNamesTxt.append(item.find("a").text) # Add item to colorNamesTxt array 
for item in N2Z_colorNames[10:]: # Loop through N-Z page elements to get name text 
    colorNamesTxt.append(item.find("a").text) # Add item to colorNamesTxt array 

colorHexVals = [] # Initialize array for all colors' hex values 
for item in A2F_rows[1:]: # Loop through A-F page elements to get hex values 
    colorHexVals.append(item.find("td").text.strip()) # Add item to colorHexVals array 
for item in G2M_rows[1:]: # Loop through A-F page elements to get hex values 
    colorHexVals.append(item.find("td").text.strip()) # Add item to colorHexVals array 
for item in N2Z_rows[1:]: # Loop through A-F page elements to get hex values 
    colorHexVals.append(item.find("td").text.strip()) # Add item to colorHexVals array 


class Color: # Create class to store color details in order to convert to JSON object array 
    def __init__(self, name, hexVal): 
        self.name = name
        self.hexVal = hexVal

all_colors_obj_array = [] # Initialize array for color objects 
all_colors_objDict_array = [] # Initialize array for color object dictionaries (compatable with JSON conversion function(s)) 
all_colors_dict = {} # Initialize dictionary to hold key-value pairs of corresponding color names and hex values 
iterator = 0 # integer that increases with each loop of the colorsNamesTxt array (below) 
for name in colorNamesTxt: # loop through each name in the colorNamesTxt array 
    all_colors_dict[name] = colorHexVals[iterator] # add new values to the all_colors_dict dictionary 
    all_colors_obj_array.append(Color(name, colorHexVals[iterator])) # add new values to the all_colors_obj_array array 
    iterator += 1 # iterator increases to match index in the colorHexVals array with the index in the colorNamesTxt array 
    
for item in all_colors_obj_array: # loop through each object in the all_colors_object_array array 
    all_colors_objDict_array.append(item.__dict__) # append current item in all_colors_obj_array to all_colors_objDict_array (converting to array of dictionaries to use as JSON 

# Neither of the two code blocks below need to be ran more than once locally in order to get an updated version 
# The code below writes all the colors' names to a text file 
# all_named_colors_text_file = open("all_named_colors.txt", "w") 
# for color in colorNamesTxt: 
#     all_named_colors_text_file.write(f"{color} \n")
#     print(f"{color} \n")
# all_named_colors_text_file.close() 

# The code below writes all the color objects to a JSON file 
# all_named_colors_json_file = open("all_named_colors.json", "w") 
# all_named_colors_json_file.write(json.dumps(all_colors_objDict_array)) 
# all_named_colors_json_file.close() 

# if len(colorNamesTxt) == len(colorHexVals): 
#     print(f"Yes. \nNames: {len(colorNamesTxt)} Hex Vals: {len(colorHexVals)}")
# else: 
#     print(f"No. \nNames: {len(colorNamesTxt)} Hex Vals: {len(colorHexVals)}")

# print(all_colors_dict) 

# =============================================| 
# This script's main results:                  | 
# - colorNamesTxt                              | 
# - colorHexVals                               | 
# - all_colors_dict                            | 
# - all_colors_obj_array                       | 
# - all_named_colors.txt                       | 
# - all_named_colors.json                      | 
# ---------------------------------------------- 
