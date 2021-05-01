import folium
import pandas as pd
import xlrd


map = folium.Map(location=[41,29],tiles="CartoDB positron")

veri = pd.read_excel("cities-in-Turkey.xlsx")


ilceler = list(veri["City"])
enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])

print(enlemler)