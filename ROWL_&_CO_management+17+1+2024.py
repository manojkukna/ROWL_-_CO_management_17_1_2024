

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

kapan = "227"

import pandas as pd
import glob

# Get a list of all CSV files in a directory
manoj = glob.glob(r"Z:\wifi driver\manoj\*.csv")
piush = glob.glob(r"Z:\wifi driver\PIUSH\*.csv")
rohit = glob.glob(r"Z:\wifi driver\ROHIT\*.csv")
rajesh = glob.glob(r"Z:\wifi driver\RAJESH\*.csv")
mahesh = glob.glob(r"Z:\wifi driver\MAHESH\*.csv")
dis = []
# Initialize an empty list to store individual DataFrames
dataframes = []
csv_files = manoj
name ={"mahesh": mahesh,"manoj":manoj,"rohit":rohit,"piush":piush,}  #"rajesh":rajesh

name1 ={"manoj":manoj,}

# Loop through the list of CSV files and read them into DataFrames
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
       # Concatenate the list of DataFrames into a single DataFrame
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




    list = {'name':None,'size':None,'total peket':None,'total pc':None ,'total wat':None , 'total polis':None ,'pasent%':None }

      #rank_zoro = df_LAST_sell.loc[(df_LAST_sell["RoughWeight"] == h)]
    duplicates = df_LAST_sell.drop_duplicates(subset=['Stone Name'], keep='last')
    duplicates.sort_values("Stone Name", inplace=True)
    list['name'] = i[0]
    list['total peket'] = len(duplicates)
    list['total pc'] = len(df_LAST_sell)

    list["total wat"] = duplicates['RoughWeight'].sum()
    list['total polis'] = df_LAST_sell['Pw'].sum()
    list['pasent%'] = list['total polis'] / list["total wat"] * 100
    list['size'] = int(float(list['total pc']) / float(list['total wat']))


    dis.append(list)

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
