

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



def DataFrames(name,sainar):
    csv_files = name
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df = combined_df.loc[combined_df['WT'] > 0]

    combined_df_filtar= pd.DataFrame(  combined_df,
      columns=['Stone Name','RoughWeight','WT','Pw','Cut','Color','Clarity','Cut',
               'Fls','Price','Dolar','Sieve','Saw','Part'])


    combined_df_filtar['sainar'] = sainar

     # Print the combined DataFrame
    # print(combined_df_filtar)
    # breakpoint()
    return combined_df

# df= DataFrames(name=name["manoj"],sainar="manoj")
#

def RAPAOPRT_RED(tradebook,file_extension):
    red_padas = file_extension(tradebook)


    entry_dict_Holding = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00,"Holding_day": None, "cumsum": None}
    entry_list_Holding = []
    entry_buy_df = red_padas.fillna(value=0.00)
    # print(entry_buy_df)
    # breakpoint()

    entry_list_Holding.append(copy.deepcopy((entry_dict_Holding)))
    index_lis_Holding = red_padas.index.tolist()
    # print(entry_buy_df.iloc[0, 1])
    count = 1
    for index in index_lis_Holding:
        cadican = entry_buy_df.iloc[index, 1]
        # print(type(cadican),cadican)
        if cadican ==  "-2" :
           print(cadican)
           # breakpoint()
           for index_2 in index_lis_Holding[index:]:
             cadican = entry_buy_df.iloc[index_2, 1]
             # print(index_2,cadican,'Quantity=',entry_buy_df.iloc[index_2, 5], count )
             if cadican == "IF" and entry_buy_df.iloc[index_2, 5] and count:
                print(index_2, cadican, 'Quantity=', entry_buy_df.iloc[index_2, 5], count)
                breakpoint()
                for index_3 in index_lis_Holding[index_2:]:
                  if not entry_buy_df.iloc[index_3, 5] == 'Quantity' and entry_buy_df.iloc[index_3, 9] > 0:
                     if not entry_buy_df.iloc[index_3, 4] == 'Quantity':
                       entry_dict_Holding["symbol"] = entry_buy_df.iloc[index_3, 1]
                       entry_dict_Holding["Entry_Date"] = entry_buy_df.iloc[index_3, 3]
                       entry_dict_Holding["Exit_Date"] = entry_buy_df.iloc[index_3, 4]
                       entry_dict_Holding["Qtt"] = entry_buy_df.iloc[index_3, 5]
                       entry_dict_Holding["Buy_Value"] = entry_buy_df.iloc[index_3, 6]
                       entry_dict_Holding["Sell_Value"] = entry_buy_df.iloc[index_3, 7]
                       entry_dict_Holding["Profit"] = entry_buy_df.iloc[index_3, 8]
                       entry_dict_Holding["Holding_day"] = entry_buy_df.iloc[index_3, 9]
                       # print(entry_buy)
                       if entry_dict_Holding["Qtt"]:
                          entry_list_Holding.append(copy.deepcopy((entry_dict_Holding)))
                       if not entry_dict_Holding["Qtt"]:
                          count = 0
                          break
    # print(pd.DataFrame(entry_list_Holding).head(10))


RAPAOPRT_RED(tradebook='RAPAOPRT.csv', file_extension= pd.read_csv)

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
