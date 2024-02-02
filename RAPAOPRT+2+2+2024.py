

# import talib  # TA-Lib

import copy
import numpy as np
#
# import Zerodha_place_order as z

from math import nan
import math
import xlwings
import traceback
import datetime
import numpy as np
import csv
import time
# from kite_trade import *
import datetime, time
from datetime import datetime
import pyotp
from tabulate import tabulate

import pandas as pd
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

kapan = "181"

import pandas as pd
import glob

# Get a list1 of all CSV files in a directory
manoj = glob.glob(r"Z:\wifi driver\manoj\*.csv")
piush = glob.glob(r"Z:\wifi driver\PIUSH\*.csv")
rohit = glob.glob(r"Z:\wifi driver\ROHIT\*.csv")
rajesh = glob.glob(r"Z:\wifi driver\RAJESH\*.csv")
mahesh = glob.glob(r"Z:\wifi driver\MAHESH\*.csv")
dis = []
# Initialize an empty list1 to store individual DataFrames
dataframes = []
csv_files = manoj
name ={"mahesh": mahesh,"manoj": manoj, "rohit":rohit, "piush": piush,}  #"rajesh":rajesh

name1 ={"manoj": manoj}



print((list(name1.keys())))

# print(name["manoj"])RAPAOPRT.csv
# breakpoint()



def RAPAOPRT_RED(tradebook,file_extension,CHANI):
    red_padas = file_extension(tradebook)
    entry_dictRAPAOPRT = {'Color': None, "IF": None, 'VVS': None, 'VS1': None, "VS2": 0,
                 "S1": 0.00, "S2": 0.00,"SI3": None, "I1": None,"I2": None,"I3": None}
    entry_listRAPAOPRT = []
    entry_buy_df = red_padas.fillna(value=0.00)
    index_lisRAPAOPRT = red_padas.index.tolist()
    count = 1
    for index in index_lisRAPAOPRT:
        cadican = entry_buy_df.iloc[index, 1]
        # print(type(cadican),cadican)
        if cadican == CHANI:
           for index_2 in index_lisRAPAOPRT[index:]:
             cadican = entry_buy_df.iloc[index_2, 1]
             # print(index_2,cadican,'Quantity=',entry_buy_df.iloc[index_2, 5], count )
             if cadican == "IF" and entry_buy_df.iloc[index_2, 5] and count:
                # print(index_2, cadican, 'IF=', entry_buy_df.iloc[index_2, 1], count)

                for index_3 in index_lisRAPAOPRT[index_2:]:
                  if not entry_buy_df.iloc[index_3, 5] == 'S1': # and entry_buy_df.iloc[index_3, 5] > 0
                     if not entry_buy_df.iloc[index_3, 7] == 0.0:
                       entry_dictRAPAOPRT["Color"] = entry_buy_df.iloc[index_3, 0]
                       entry_dictRAPAOPRT["IF"] = entry_buy_df.iloc[index_3, 1]
                       entry_dictRAPAOPRT["VVS"] = entry_buy_df.iloc[index_3, 2]
                       entry_dictRAPAOPRT["VS1"] = entry_buy_df.iloc[index_3, 3]
                       entry_dictRAPAOPRT["VS2"] = entry_buy_df.iloc[index_3, 4]
                       entry_dictRAPAOPRT["S1"] = entry_buy_df.iloc[index_3, 5]
                       entry_dictRAPAOPRT["S2"] = entry_buy_df.iloc[index_3, 6]
                       entry_dictRAPAOPRT["SI3"] = entry_buy_df.iloc[index_3,7]
                       entry_dictRAPAOPRT["I1"] = entry_buy_df.iloc[index_3, 8]
                       entry_dictRAPAOPRT["I2"] = entry_buy_df.iloc[index_3, 9]
                       entry_dictRAPAOPRT["I3"] = entry_buy_df.iloc[index_3, 10]
                       if entry_dictRAPAOPRT['VS2']:
                          entry_listRAPAOPRT.append(copy.deepcopy((entry_dictRAPAOPRT)))
                       if entry_dictRAPAOPRT['Color'] == "N":
                          count = 0
                          break
    print(pd.DataFrame(entry_listRAPAOPRT))
    return

# RAPAOPRT_RED(tradebook='RAPAOPRT.csv', file_extension=pd.read_csv,CHANI="-4")
#





def DataFrames(name,sainar):
    csv_files = name
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df = combined_df.loc[combined_df['WT'] > 0]
    combined_df_filtar= pd.DataFrame(combined_df,
      columns=['Stone Name','RoughWeight','WT','Pw','Cut','Color','Clarity',
               'Fls','Price','Dolar','Sieve','Saw','Part'])
    combined_df_filtar['sainar'] = sainar
    # Print the combined DataFrame
    # print(combined_df_filtar.head(5))
    # breakpoint()
    return combined_df_filtar
#
df4= DataFrames(name=name["manoj"],sainar="manoj")
# print(df4)
# breakpoint()



def raf_pidishan(df3):
    raf_pidishan = {'Stone Name': None, "RoughWeight": None, 'WT': None, 'Pw': None,'Cut': 0,
                        'Color': 0.00, 'Clarity': 0.00,  'Fls' : None, 'Price': None, 'par_caret': None, 'Sieve': None,
                          'Saw': None, 'Part': None}
    raf_pidishan_df = df3.fillna(value=0.00)
    print(pd.DataFrame(df3).head(5))

    #
    # breakpoint()
    index_raf_pidishan =  raf_pidishan_df.index.tolist()
    count = 1
    for index in index_raf_pidishan:
        # cadican =   raf_pidishan_df.iloc[index, 2]
        # print(raf_pidishan_df.iloc[index, 2])
        raf_pidishan['Stone Name'] = raf_pidishan_df.iloc[index, 0]
        raf_pidishan[ "RoughWeight"] = raf_pidishan_df.iloc[index, 1]
        raf_pidishan['WT'] = raf_pidishan_df.iloc[index, 2]
        raf_pidishan['Pw'] = raf_pidishan_df.iloc[index, 3]
        raf_pidishan['Cut'] = raf_pidishan_df.iloc[index, 4]
        raf_pidishan['Color'] = raf_pidishan_df.iloc[index,5]
        raf_pidishan[ 'Clarity'] = raf_pidishan_df.iloc[index, 6]
        raf_pidishan['Fls'] = raf_pidishan_df.iloc[index, 7]
        raf_pidishan['Price'] = raf_pidishan_df.iloc[index, 8]
        raf_pidishan['par_caret'] = raf_pidishan_df.iloc[index, 9]
        raf_pidishan['Sieve'] = raf_pidishan_df.iloc[index, 10]
        raf_pidishan['Saw'] = raf_pidishan_df.iloc[index, 11]
        raf_pidishan['Part'] = raf_pidishan_df.iloc[index, 12]

        print(raf_pidishan)
        # breakpoint()

# print(DataFrames(name=name["manoj"],sainar="manoj"))

#
# print(df4)
# breakpoint()
raf_pidishan(df3=df4)

breakpoint()

def analist(df,sainar):

    df.loc[:, 'kapan'] = df['Stone Name'].str[:3]
    sainar = sainar
    
    df.loc[:, 'sainar'] = sainar


    df = df.loc[df['kapan'] == kapan]

    print(df)

    list1 = {'name': None, 'size': None, 'total peket': None, 'total pc': None, 'total wat': None, 'total polis': None,
            'pasent%': None}

    # rank_zoro = df_LAST_sell.loc[(df_LAST_sell["RoughWeight"] == h)]
    duplicates = df.drop_duplicates(subset=['Stone Name'], keep='last')
    duplicates = pd.DataFrame(duplicates)
    duplicates.sort_values("Stone Name", inplace=True)
    list1['name'] = sainar[0]
    list1['total peket'] = len(duplicates)
    list1['total pc'] = len(df)

    list1["total wat"] = duplicates['RoughWeight'].sum()
    list1['total polis'] = df['Pw'].sum()
    list1['pasent%'] = list1['total polis'] / list1["total wat"] * 100
    list1['size'] = int(float(list1['total pc']) / float(list1['total wat']))

    dis.append(list1)

    SUM = df['WT'].sum()

    # grouped = df_LAST_sell.groupby("Stone Name")["WT","Pw"].sum()
    grouped = df.groupby("Stone Name")[["WT", "Pw"]].sum()

    grouped["RoughWeight"] = duplicates["RoughWeight"]
    grouped['pasent%'] = grouped["Pw"] / grouped["WT"] * 100

    print(grouped)

    # sheets_NAME = "data_NSC_ALL.xlsx"
    # ws = xlwings.Book(sheets_NAME).sheets("NSE")
    # ws.clear()
    #
    # selected_columns = df_LAST_sell[['Stone Name', 'RoughWeight', 'Shape', 'WT',
    #                                  'Pw', 'Cut', 'Shape', 'Color', "Clarity", 'Price', 'sainar']]


# analist(df=df, sainar="manoj")

breakpoint()




# Loop through the list1 of CSV files and read them into DataFrames
for i in name.items():
    csv_files = i
    print(csv_files)
    # breakpoint()
    for csv_file in csv_files[1]:
        df = pd.read_csv(csv_file)
        # print(df)
        # breakpoint()
        # df [i[0]]= i[0]
        dataframes.append(df)
        # print( df)
       # Concatenate the list1 of DataFrames into a single DataFrame
       #  breakpoint()

    combined_df = pd.concat(dataframes, ignore_index=True)

     # Print the combined DataFrame
    print(combined_df)
    # breakpoint()
    df_LAST_sell = combined_df.loc[combined_df['WT'] > 0]

# df_LAST_sell['kapan'] = df_LAST_sell['Stone Name'].str[:3]
    df_LAST_sell.loc[:, 'kapan'] = df_LAST_sell['Stone Name'].str[:3]
    df_LAST_sell.loc[:, 'sainar'] = i[0]

    # print(df_LAST_sell)

    df_LAST_sell = df_LAST_sell.loc[df_LAST_sell['kapan'] == kapan]

    print(df_LAST_sell)




    list1 = {'name':None,'size':None,'total peket':None,'total pc':None ,'total wat':None , 'total polis':None ,'pasent%':None }

      #rank_zoro = df_LAST_sell.loc[(df_LAST_sell["RoughWeight"] == h)]
    duplicates = df_LAST_sell.drop_duplicates(subset=['Stone Name'], keep='last')
    duplicates.sort_values("Stone Name", inplace=True)
    list1['name'] = i[0]
    list1['total peket'] = len(duplicates)
    list1['total pc'] = len(df_LAST_sell)

    list1["total wat"] = duplicates['RoughWeight'].sum()
    list1['total polis'] = df_LAST_sell['Pw'].sum()
    list1['pasent%'] = list1['total polis'] / list1["total wat"] * 100
    list1['size'] = int(float(list1['total pc']) / float(list1['total wat']))


    dis.append(list1)

    SUM = df_LAST_sell['WT'].sum()



    # grouped = df_LAST_sell.groupby("Stone Name")["WT","Pw"].sum()
    grouped = df_LAST_sell.groupby("Stone Name")[["WT", "Pw"]].sum()


    grouped["RoughWeight"] = duplicates["RoughWeight"]
    grouped['pasent%'] = grouped["Pw"] / grouped["WT"] * 100

    print(grouped)


    sheets_NAME = "data_NSC_ALL.xlsx"
    ws = xlwings.Book(sheets_NAME).sheets("NSE")
    ws.clear()

    selected_columns = df_LAST_sell[['Stone Name', 'RoughWeight','Shape', 'WT',
                           'Pw', 'Cut','Shape', 'Color',"Clarity",'Price', 'sainar']]


    ws.range('A15').value = pd.DataFrame(selected_columns)


    # ws.range('A15').value = pd.DataFrame(grouped)
    #

    ws = xlwings.Book(sheets_NAME).sheets("NSE")
    ws.range('A1').value = pd.DataFrame.from_dict(dis)


    ws = xlwings.Book(sheets_NAME).sheets("RANIG_STOCK")
    ws.clear()
    ws.range('A5').value = pd.DataFrame.from_dict(duplicates)
