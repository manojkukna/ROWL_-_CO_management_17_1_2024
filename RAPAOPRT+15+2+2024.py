

# import talib  # TA-Lib






import os


#
#
#
# try:
#     import xlwings
# except ImportError:
#     os.system('python -m pip install --upgrade pip')
#
#
# try:
#     import openpyxl
# except ImportError:
#     os.system('python -m pip install openpyxl')
#
#
# try:
#     import xlwings
# except ImportError:
#     os.system('python -m pip install xlwings==0.30.12')
# try:
#     import pandas
# except ImportError:
#     os.system('python -m pip install pandas')
#
#
# try:
#     import yfinance
# except ImportError:
#     os.system('python -m pip install yfinance==0.2.28')
# try:
#     import tabulate
# except ImportError:
#     os.system('python -m pip install tabulate')
#
#
# try:
#     import pyotp
# except ImportError:
#     os.system('python -m pip install pyotp')
#
#
# try:
#     import streamlit
# except ImportError:
#     os.system('python -m pip install streamlit')
#
#
#
# try:
#     import plotly
# except ImportError:
#     os.system('python -m pip install plotly==5.18.0')
# try:
#     import treamlit_option_menu
# except ImportError:
#     os.system('python -m pip install streamlit-option-menu')
# try:
#     import streamlit_extras
# except ImportError:
#     os.system('python -m pip install streamlit_extras')
#
#
# try:
#     import  numpy
# except ImportError:
#     os.system('python -m pip install  numpy ')
#


# try:
#     import  streamlit
# except ImportError:
#     os.system('python -m pip install  streamlit ')
#
# try:
#     import  plotly
# except ImportError:
#     os.system('python -m pip install  plotly ')
#
# try:
#     import streamlit_option_menu
# except ImportError:
#     os.system('python -m pip install  streamlit-option-menu ')
#
# try:
#     import  streamlit_extras
# except ImportError:
#     os.system('python -m pip install   streamlit_extras')
#













import streamlit as st  #  pip install streamlit
import pandas as pd
import plotly.express as px       #                             pip install plotly
import copy
from streamlit_option_menu import option_menu     # pip install streamlit-option-menu
# import streamlit_multiple_pages_17_12_2023 as z
from streamlit_extras.metric_cards import style_metric_cards
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

st.set_page_config(page_title="STOCK MARKET JANRAL TO ZERODHA",page_icon="📊",layout="wide",initial_sidebar_state="expanded",)  # "auto" or "expanded" or "collapsed"
# Set dark theme using custom CSS
st.markdown(
    """
    <style>
        body {
            color: #FFFFFF;  /* Text color */
            background-color: 'black';  /* Background color */
        }
        /* Add more custom styles as needed */
    </style>
    """,
    unsafe_allow_html=True)

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

kapan = "89"

import pandas as pd
import glob

# Get a list1 of all CSV files in a directory

# manoj = glob.glob(r"Z:\wifi driver\manoj\*.csv")
# piush = glob.glob(r"Z:\wifi driver\PIUSH\*.csv")
# rohit = glob.glob(r"Z:\wifi driver\ROHIT\*.csv")
# rajesh = glob.glob(r"Z:\wifi driver\RAJESH\*.csv")
# mahesh = glob.glob(r"Z:\wifi driver\MAHESH\*.csv")
#
# manoj = glob.glob(r"manoj\*.csv")
# piush = glob.glob(r"PIUSH\*.csv")
# rohit = glob.glob(r"ROHIT\*.csv")
# rajesh = glob.glob(r"RAJESH\*.csv")
# mahesh = glob.glob(r"MAHESH\*.csv")
# all_panini_fileh = glob.glob(r"all_panini_file\*.csv")




# dis = []
# # Initialize an empty list1 to store individual DataFrames

# csv_files = manoj
# name ={"mahesh": mahesh,"manoj": manoj, "rohit":rohit, "piush": piush,"rajesh":rajesh,"all_panini_fileh":all_panini_fileh}  #"rajesh":rajesh
#
# name1 ={"manoj": manoj}



# print((list(name1.keys())))

# print(name["manoj"])RAPAOPRT.csv
# breakpoint()
import shutil
import os
import filecmp
import glob





import os

def clear_folder(folder_path):
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)

# Specify the folder you want to clear
folder_to_clear = r"all_panini_file"

# Call the function to clear the folder
clear_folder(folder_to_clear)

#
# breakpoint()




def add_files_and_remove_duplicates(source_folders, destination_folder,filtered):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Flatten the list of lists
    files = [file for folder in source_folders for file in folder]

    filtered_list = [file_path for file_path in files if filtered in file_path]
    # print(filtered_list)

    # breakpoint()
    # Iterate through files and copy them to the destination folder, removing duplicates
    for file in filtered_list:

        # print(file)
        # list = files

        # print(filtered_list)
        #
        # # breakpoint()
        source_path = file
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_folder, filename)

        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            # If it exists, check if the files are identical
            if filecmp.cmp(source_path, destination_path):
                # If they are identical, remove the duplicate
                os.remove(source_path)
            else:
                # If they are not identical, copy the file to the destination folder
                shutil.copy(source_path, destination_path)
        else:
            # If the file does not exist in the destination folder, copy it
            shutil.copy(source_path, destination_path)


        # print(   filename)
        # breakpoint()
# Example usag e


# breakpoint()
def RAPAOPRT_RED(CHANI):
    # RAPAOPRT_RED(tradebook='RAPAOPRT.csv', file_extension=pd.read_csv, CHANI="-4")
    red_padas = pd.read_csv('RAPAOPRT.csv')
    # print(pd.DataFrame(red_padas))

    entry_dictRAPAOPRT = {'Color': None, "IF": None, 'VVS': None, 'VS1': None, "VS2": 0,
                 "S1": 0.00, "S2": 0.00,"SI3": None, "I1": None,"I2": None,"I3": None}
    entry_listRAPAOPRT = []
    entry_buy_df = red_padas.fillna(value=0.00)
    # print(entry_buy_df)
    # breakpoint()
    index_lisRAPAOPRT = red_padas.index.tolist()
    count = 1
    for index in index_lisRAPAOPRT:
        cadican = entry_buy_df.iloc[index, 1]
        # print(type(cadican),cadican)
        # print("-2", CHANI, cadican == CHANI)
        if cadican == CHANI:

           # print("-2",CHANI, cadican == CHANI)

           for index_2 in index_lisRAPAOPRT[index:]:
             cadican = entry_buy_df.iloc[index_2, 1]
             # print(index_2,cadican,'index_2=',entry_buy_df.iloc[index_2, 1], count )
             # breakpoint()

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

                       # print(entry_dictRAPAOPRT)
                       if entry_dictRAPAOPRT['VS2']:
                          entry_listRAPAOPRT.append(copy.deepcopy((entry_dictRAPAOPRT)))
                          #
                          # print(entry_dictRAPAOPRT)

                       if entry_dictRAPAOPRT['Color'] == "N":
                          count = 0
                          break

    return entry_listRAPAOPRT



RAPAOPRT_RED(CHANI="3")
RAPAOPRT_RED(CHANI="7")
RAPAOPRT_RED(CHANI="14")
RAPAOPRT_RED(CHANI="17")
RAPAOPRT_RED(CHANI="22")

dataframes = []
def DataFrames(name,sainar,kapan):
    csv_files = name
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        dataframes.append(df)
        # print(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df = combined_df.loc[combined_df['WT'] > 0]
    # print(pd.DataFrame(combined_df).head(50))
    #
    # breakpoint()
    combined_df_filtar= pd.DataFrame(combined_df,
      columns=['Stone Name','RoughWeight','WT','Pw','Cut','Color','Clarity',
               'Fls','Price','Dolar','Sieve','Saw','Part','W','L'])
    combined_df_filtar['sainar'] = sainar
    # index_raf_pidishan =  raf_pidishan_df.index.tolist()

    combined_df_filtar['kapan'] = combined_df_filtar['Stone Name'].str.split('-').str.get(0)
    combined_df_filtar = combined_df_filtar.loc[combined_df_filtar['kapan'] == kapan]


    combined_df_filtar.reset_index(inplace=True, drop=True)

    # print(combined_df_filtar)
    # print(combined_df_filtar.loc[combined_df_filtar['kapan'] == kapan])


    return combined_df_filtar



# appd(name=name) name ={"mahesh": mahesh,"manoj": manoj, "rohit":rohit, "piush": piush,}  #"rajesh":rajesh
#
# mahesh = DataFrames(name=name["mahesh"], sainar="mahesh", kapan="89")
#
# breakpoint()



def DataFrames_tabal(W):
    chani = " "
    if W <= 2.14:
        chani ="3"
    if W >= 2.15 and W <= 2.74:
        chani = "7"
    if W >= 2.75 and W <= 3.34:
        chani = "14"
    if W >= 3.35 and W <= 3.56:
        chani = "17"
    if W >= 3.57 and W <= 5.57:
        chani = "22"
    # print(chani)
    return chani
DataFrames_tabal(W=1.28)
# breakpoint()


def Price(df, Color, Clarity):
    Price = pd.DataFrame(df)
    # print(Price )
    # breakpoint()
    Price.reset_index(inplace=True, drop=True)
    row_index = Price[Price['Color'] == Color].index[0]
    Price = Price.iloc[row_index, Price.columns.get_loc(Clarity)]
    # print(type(Price))
    # breakpoint()
    return float(Price)

entry_pidishan_list = []

def raf_pidishan(df3,Discount,Labor_Cost):
    raf_pidishan = {'kapan': None, 'Stone Name': None, "RoughWeight": None, 'WT': None, 'Pw': None, 'Cut': 0,
                    'Color': 0.00, 'Clarity': 0.00, 'Fls': None, 'Price': None, 'par_caret': None, 'Discount': None,
                    'Labor Cost': None,'CHANI': None, 'Saw': None, 'Part': None, 'W': None, 'L': None}
    chani_list = {'3': '-4', '7':'+4', '14': '+8','17': None, '22': '+14'}

    raf_pidishan_df = df3.fillna(value=0.00)
    raf_pidishan_df.replace(to_replace="WH", value="G", inplace=True)
    raf_pidishan_df.replace(to_replace='VS', value="VS2", inplace=True)
    raf_pidishan_df.replace(to_replace='SI', value="S1", inplace=True)
    # print( raf_pidishan_df)
    # breakpoint()
    index_raf_pidishan =  raf_pidishan_df.index.tolist()

    for index in index_raf_pidishan:

        # print(len(pd.DataFrame( index_raf_pidishan )),pd.DataFrame( index_raf_pidishan ))
        # breakpoint()

        raf_pidishan['Stone Name'] = raf_pidishan_df.iloc[index, 0]
        raf_pidishan["RoughWeight"] = raf_pidishan_df.iloc[index, 1]
        raf_pidishan['WT'] = raf_pidishan_df.iloc[index, 2]
        raf_pidishan['Pw'] = raf_pidishan_df.iloc[index, 3]
        raf_pidishan['Cut'] = raf_pidishan_df.iloc[index, 4]
        raf_pidishan['Color'] = raf_pidishan_df.iloc[index,5]
        raf_pidishan['Clarity'] = raf_pidishan_df.iloc[index, 6]
        raf_pidishan['Fls'] = raf_pidishan_df.iloc[index, 7]
        raf_pidishan['W'] = raf_pidishan_df.iloc[index, 13]
        raf_pidishan['L'] = raf_pidishan_df.iloc[index, 14]
        CHANI_filtar = DataFrames_tabal(W=raf_pidishan['W'])


        # df =DataFrames_tabal(W=1.28)
        # print(raf_pidishan['Color'])
        # print(raf_pidishan['Clarity'])
        # print(CHANI_filtar)
        # print(raf_pidishan['W'])
        # print(df)
        # print(RAPAOPRT_RED(CHANI=CHANI_filtar))

        # breakpoint()  #Price(df=RAPAOPRT_RED(CHANI=CHANI_filtar)
        # print(Price(df=RAPAOPRT_RED(CHANI=CHANI_filtar), Color=raf_pidishan['Color'],Clarity=raf_pidishan['Clarity']))

        # breakpoint()
        raf_pidishan['par_caret'] = ((Price(df=RAPAOPRT_RED(CHANI=CHANI_filtar), Color=raf_pidishan['Color'],Clarity=raf_pidishan['Clarity'])) * 82.98) * 100
        raf_pidishan['par_caret'] = raf_pidishan['par_caret'] - (raf_pidishan['par_caret'] * Discount / 100)
        raf_pidishan['Discount'] = f"{Discount} %"
        raf_pidishan['Labor Cost'] = Labor_Cost
        raf_pidishan['Price'] = raf_pidishan['par_caret'] * raf_pidishan['Pw']
        raf_pidishan['CHANI'] = chani_list[CHANI_filtar]
        raf_pidishan['Saw'] = str(raf_pidishan_df.iloc[index, 11])
        raf_pidishan['Part'] = raf_pidishan_df.iloc[index, 12]
        raf_pidishan['sainar'] = raf_pidishan_df.iloc[index, 15]
        raf_pidishan['kapan'] = raf_pidishan_df.iloc[index, 16]
        entry_pidishan_list.append(copy.deepcopy(raf_pidishan))

        # print(entry_pidishan_list)

        # breakpoint()

    print(pd.DataFrame(entry_pidishan_list))
    return entry_pidishan_list


# df = raf_pidishan(df3=df4,Discount=50,Labor_Cost=80)





def metric_label(risk_dict,PROFIT,Labor_Cost):
    box_height = "50PX"
    background_color = "#0000CD"
    label_size = "30px"
    value_size = "35px"
    font_color = "#FFFFFF"
    risk_dict = pd.DataFrame(risk_dict)

    # breakpoint()
    RoughWeight = risk_dict.drop_duplicates(subset=['Stone Name'])

    print(RoughWeight)

    # print(  risk_dict)

    # breakpoint()
    # RoughWeight = risk_dict['RoughWeight'].drop_duplicates().sum()
    #
    # print(risk_dict["RoughWeight"].drop_duplicates().sum())
    # print(risk_dict["Pw"].sum())
    # print(risk_dict["Pw"].sum() /risk_dict["RoughWeight"].drop_duplicates().sum() * 100)
    # breakpoint()

    PAR_CARET_RAF_AVREJ_Cost = int((risk_dict["Price"].sum() / risk_dict["Pw"].sum() - int(float(len(risk_dict)) / RoughWeight["RoughWeight"].sum()) * Labor_Cost) *
                  risk_dict["Pw"].sum() / RoughWeight["RoughWeight"].sum())


    total8, total9, total10, = st.columns(3, gap="small")
    with total8:
        st.metric(label="PAR CARET RAF AVREJ Cost", value= int(PAR_CARET_RAF_AVREJ_Cost-PAR_CARET_RAF_AVREJ_Cost * PROFIT / 100))
    with total9:
        st.metric(label="NET PROFIT", value=int(PAR_CARET_RAF_AVREJ_Cost * PROFIT / 100))
    with total10:
        st.metric(label="%NET PROFIT%", value=f'% {PROFIT} %')




    total01, total02, total03, = st.columns(3, gap="small")
    with total01:
        st.metric(label='PAR CARET avrej Cost', value= int(risk_dict["Price"].sum() / risk_dict["Pw"].sum() - int(float(len(risk_dict)) / RoughWeight["RoughWeight"].sum()) * Labor_Cost))
    with total02:
        st.metric(label="PAR CARET SELL PRICE", value=int(risk_dict["Price"].sum() / risk_dict["Pw"].sum()) )
    with total03:
        st.metric(label='PAR CARET Labor Cost', value=int(float(len(risk_dict)) / RoughWeight["RoughWeight"].sum()) * Labor_Cost)








    total2, total3, total4 = st.columns(3, gap="small")  # "small"  'large'
    # with total1:
    # Group by 'Stone Name' and sum 'RoughWeight', 'WT', and 'Price'
    # print(risk_dict.drop_duplicates(subset=['Stone Name']))


    # print("RoughWeight",risk_dict["Stone Name"].unique())
    # breakpoint()
    with total2:
        st.metric(label="RoughWeight", value=round(RoughWeight["RoughWeight"].sum(), 2))
    with total3:
        st.metric(label="polish Weight", value=round(risk_dict["Pw"].sum(), 2))
    with total4:
        st.metric(label="parsent", value=f'{risk_dict["Pw"].sum() / RoughWeight["RoughWeight"].sum() * 100 :,.0f} %')



    total5, total6, total7, = st.columns(3, gap="small")
    with total5:
        st.metric(label='total peket', value=len(risk_dict["RoughWeight"].drop_duplicates()))
    with total6:
        st.metric(label="total pc", value=len(risk_dict))
    with total7:
        st.metric(label='size', value= f'{float(len(risk_dict)) / RoughWeight["RoughWeight"].sum():,.0f}')

    # total8, total9, total10, = st.columns(3, gap="small")
    # with total8:
    #     st.metric(label="Wins", value=f'{risk_dict["Wins"]:,.0f}')
    # with total9:
    #     st.metric(label="%Win",
    #               value=f'{risk_dict["Wins"] / risk_dict["Nb_of_trade"] * 100 if risk_dict["Wins"] != 0 else 0:,.0f}%')
    # with total10:
    #     st.metric(label="Profit", value=f'{risk_dict["Profit"]:,.0f}')
    #
    #
    # total11, total12, total13, = st.columns(3, gap="small")
    # with total11:
    #     st.metric(label="Losser", value=f'{risk_dict["Losser"]:,.0f}')
    # with total12:
    #      st.metric(label="%Losser", value=f'{risk_dict["Losser"] / risk_dict["Nb_of_trade"] * 100 if risk_dict["Losser"] != 0 else 0:,.0f}%')
    # with total13:
    #     st.metric(label="Loss", value=f'{risk_dict["Loss"]:,.0f}')
    #
    # total14, total15, total16, = st.columns(3, gap="small")
    #
    # with total14:
    #     st.metric(label="Avg_Return", value=f'{risk_dict["Avg_Return"]:,.0f}')
    # with total15:
    #     st.metric(label="Avg_Winner", value=f'{ risk_dict["Avg_Winner"]:,.0f}')
    # with total16:
    #     st.metric(label="Avg_Loser", value=f'{ risk_dict["Avg_Loser"]:,.0f}')

    style_metric_cards(background_color="#02ab21", border_left_color="#f20045", box_shadow="30px")  # color="white"


def line_chart(data, title):
    st.line_chart(data)
    st.title(title)
    # print("line_chart 82",time_())

def convert_df(df, file_name):
    csv1 = df.to_csv().encode("utf-8")
    st.download_button(
        label="Download data as CSV",
        data=csv1,
        file_name=file_name,
        mime="text/csv", key=f"{csv1}")
    return


def Clarity_pie(pie_df,width,height):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = (pie_df_data['Pw'].sum())
    fig = px.pie(pie_df_data, values='Pw',names='Clarity',title=f"Clarity piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Clarity', legend_y=0.9, paper_bgcolor='#80aaff', width=width,height=height)
    fig.update_traces(textinfo='label+percent+value', textposition='inside',textfont=dict(size=14, color="white", family="Arial Black"))
    return fig

def chani_pie(pie_df,width,height):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = (pie_df_data['Pw'].sum())
    fig = px.pie(pie_df_data, values='Pw',names='CHANI',title=f"CHANI piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='CHANI', legend_y=0.9, paper_bgcolor='#80aaff', width=width,height=height)
    fig.update_traces(textinfo='label+percent+value', textposition='inside',textfont=dict(size=14, color="white", family="Arial Black"))
    return fig



width = 2000
height = 625



def run():

        #
        # st.sidebar.image("IMG_20190423_172859.png",
        #                 caption="Developed and   application problem solving   by: KUKAN MANOJ    : helpline   number -> 9106963281")
        # print("all_qttar_dict_list lin 173 ", time_())
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Home', 'selected_sainar'],
                #,'rohit', 'piush', 'mahesh', 'rajesh','Charges','Charges Debits and Credits','Dividends', 'Settings', 'about'],
                #           https: // icons.getbootstrap.com /  # icons     'person-circle'

                icons=['house-fill','journal-arrow-up'],#,'journal-arrow-up', 'trophy-fill', 'apple', 'play-btn-fill','caret-right-square-fill','caret-right-square-fill','caret-right-square-fill','gear','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={"container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "30px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                       "nav-link-selected": {"background-color": "#02ab21"}, })

            # print("option_menu lin 189 ", time_())   df = df.loc[df['kapan'] == kapan]
        if app == "Home":
            # manoj = DataFrames(name=name["manoj"], sainar="manoj", kapan="89")

            # mahesh = DataFrames(name=name["mahesh"], sainar="mahesh",kapan="89")
            # rohit = DataFrames(name=name["rohit"], sainar="rohit",kapan="89")
            # piush = DataFrames(name=name["piush"], sainar="piush",kapan="89")
            # rajesh = DataFrames(name=name["rajesh"], sainar="rajesh",kapan="89")

            raf_Cost = st.sidebar.number_input("raf Cost", value=650, key='raf Cost')
            kapan = st.sidebar.number_input("kapan", value =89, key ='kapan')
            Discount = st.sidebar.number_input("%Discount%", value=50, key='Discount')
            PROFIT = st.sidebar.number_input("% PROFIT %", value=20, key='PROFIT')

            Labor_Cost = st.sidebar.number_input("Labor_Cost", value=80, key='Labor_Cost')

            piush = glob.glob(r"G:\R.RAWAL.CO\PIUSH\*.csv")
            rohit = glob.glob(r"G:\R.RAWAL.CO\ROHIT\*.csv")
            manoj = glob.glob(r"G:\R.RAWAL.CO\manoj\*.csv")
            rajesh = glob.glob(r"G:\R.RAWAL.CO\RAJESH\*.csv")
            mahesh = glob.glob(r"G:\R.RAWAL.CO\MAHESH\*.csv")


            source_folders = [piush, rohit, manoj, rajesh, mahesh]
            all_panini_file_folder = r"all_panini_file"
            filtered = f'\\{kapan}-'
            add_files_and_remove_duplicates(source_folders, all_panini_file_folder, filtered)

            # print(name["all_panini_fileh"])


            # breakpoint()

            fig, fig2, = st.columns(2, gap='large')

            with fig:
                 all_panini_fileh = DataFrames(name=glob.glob(r"all_panini_file\*.csv"), sainar="MAHESH", kapan=str(kapan))
                 all_qttar_dict = raf_pidishan(df3=all_panini_fileh, Discount=Discount, Labor_Cost=Labor_Cost)
                 fig = chani_pie(pd.DataFrame(all_qttar_dict), width, height)
                 st.plotly_chart(fig, use_container_width=True, theme=None)

            with fig2:
                  fig1 = Clarity_pie(pd.DataFrame(all_qttar_dict), width, height)
                  st.plotly_chart(fig1, use_container_width=True, theme=None)

            metric_label(risk_dict=all_qttar_dict, PROFIT=PROFIT,Labor_Cost=Labor_Cost)
            st.dataframe(pd.DataFrame(all_qttar_dict), use_container_width=False, width=1500, height=300)
            convert_df(df=pd.DataFrame(all_qttar_dict), file_name="MANOJ KUKNA.csv")

        if app == "selected_sainar":
            # manoj = DataFrames(name=name["manoj"], sainar="manoj", kapan="89")
            #
            # mahesh = DataFrames(name=name["mahesh"], sainar="mahesh",kapan="89")
            # rohit = DataFrames(name=name["rohit"], sainar="rohit",kapan="89")
            # piush = DataFrames(name=name["piush"], sainar="piush",kapan="89")
            # rajesh = DataFrames(name=name["rajesh"], sainar="rajesh",kapan="89")

            selected_sainar = st.sidebar.selectbox('selected sainar', ["manoj", "rohit", "piush", "rajesh", "mahesh"])

            kapan = st.sidebar.number_input("kapan", value=89, key=selected_sainar)
            Discount = st.sidebar.number_input("Discount", value=50, key=f'Discount{selected_sainar}')
            Labor_Cost = st.sidebar.number_input("Labor_Cost", value=80, key=f'Labor_Cost{ selected_sainar}')



            all_panini_fileh = DataFrames(name=name[selected_sainar], sainar=selected_sainar, kapan=str(kapan))
            all_qttar_dict = raf_pidishan(df3=all_panini_fileh,Discount=Discount, Labor_Cost=Labor_Cost)
            fig = chani_pie(pd.DataFrame(all_qttar_dict), width, height)
            st.plotly_chart(fig, use_container_width=True, theme=None)

            fig1 = Clarity_pie(pd.DataFrame(all_qttar_dict), width, height)
            st.plotly_chart(fig1, use_container_width=True, theme=None)

            metric_label(risk_dict=all_qttar_dict)
            st.dataframe(pd.DataFrame(all_qttar_dict), use_container_width=False, width=1200, height=300)
            convert_df(df=pd.DataFrame(all_qttar_dict), file_name="MANOJ KUKNA.csv")




        # if app == "rohit":
        #
        #
        #     rohit = DataFrames(name=name["rohit"], sainar="rohit", kapan="89")
        #
        #     kapan = st.sidebar.number_input("kapan", value=89, key='kapan')
        #     Discount = st.sidebar.number_input("Discount", value=50, key='Discount')
        #     Labor_Cost = st.sidebar.number_input("Labor_Cost", value=80, key='Labor_Cost')
        #
        #     all_panini_fileh = DataFrames(name=name["rohit"], sainar="rohit", kapan=str(kapan))
        #
        #
        #
        #
        #     all_panini_fileh = DataFrames(name=name["manoj"], sainar="manoj", kapan=str(kapan))
        #     all_qttar_dict = raf_pidishan(df3=all_panini_fileh, Discount=Discount, Labor_Cost=Labor_Cost)
        #     fig = chani_pie(pd.DataFrame(all_qttar_dict), width, height)
        #     st.plotly_chart(fig, use_container_width=True, theme=None)
        #
        #     fig1 = Clarity_pie(pd.DataFrame(all_qttar_dict), width, height)
        #     st.plotly_chart(fig1, use_container_width=True, theme=None)
        #
        #     metric_label(risk_dict=all_qttar_dict)
        #     st.dataframe(pd.DataFrame(all_qttar_dict), use_container_width=False, width=1200, height=300)
        #     convert_df(df=pd.DataFrame(all_qttar_dict), file_name="MANOJ KUKNA.csv")


run()




# streamlit run RAPAOPRT+14+2+2024+++.py
