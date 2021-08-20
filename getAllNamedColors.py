import requests 
from bs4 import BeautifulSoup 
import json 

A2F_URL = "https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F" 
G2M_URL = "https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M"
N2Z_URL = "https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z" 

A2F_page = requests.get(A2F_URL) 
G2M_page = requests.get(G2M_URL) 
N2Z_page = requests.get(N2Z_URL) 

A2F_soup = BeautifulSoup(A2F_page.content, "html.parser")
G2M_soup = BeautifulSoup(G2M_page.content, "html.parser")
N2Z_soup = BeautifulSoup(N2Z_page.content, "html.parser")

A2F_table = A2F_soup.find("table")
G2M_table = G2M_soup.find("table") 
N2Z_table = N2Z_soup.find("table") 

A2F_rows = A2F_table.find_all("tr") 
G2M_rows = G2M_table.find_all("tr") 
N2Z_rows = N2Z_table.find_all("tr") 

A2F_hexVals = [] 
G2M_hexVals = [] 
N2Z_hexVals = [] 

A2F_colorNames = A2F_table.find_all("th")
G2M_colorNames = G2M_table.find_all("th")
N2Z_colorNames = N2Z_table.find_all("th")

colorNamesTxt = []
for item in A2F_colorNames[10:]: 
    colorNamesTxt.append(item.find("a").text) 
for item in G2M_colorNames[10:]: 
    colorNamesTxt.append(item.find("a").text) 
for item in N2Z_colorNames[10:]: 
    colorNamesTxt.append(item.find("a").text) 

colorHexVals = [] 
for item in A2F_rows[1:]: 
    colorHexVals.append(item.find("td").text.strip()) 
for item in G2M_rows[1:]: 
    colorHexVals.append(item.find("td").text.strip()) 
for item in N2Z_rows[1:]: 
    colorHexVals.append(item.find("td").text.strip()) 


class Color: 
    def __init__(self, name, hexVal): 
        self.name = name
        self.hexVal = hexVal

all_colors_obj_array = [] 
all_colors_objDict_array = [] 
all_colors_dict = {} 
iterator = 0 
for name in colorNamesTxt: 
    all_colors_dict[name] = colorHexVals[iterator]
    all_colors_obj_array.append(Color(name, colorHexVals[iterator])) 
    iterator += 1 
    
for item in all_colors_obj_array: 
    all_colors_objDict_array.append(item.__dict__)

# all_named_colors_text_file = open("all_named_colors.txt", "w") 
# for color in colorNamesTxt: 
#     all_named_colors_text_file.write(f"{color} \n")
#     print(f"{color} \n")
# all_named_colors_text_file.close() 

all_named_colors_json_file = open("all_named_colors.json", "w") 
all_named_colors_json_file.write(json.dumps(all_colors_objDict_array)) 
all_named_colors_json_file.close() 

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