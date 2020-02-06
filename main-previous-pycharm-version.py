import gspread
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

spreadsheet_old = client.open_by_url("https://docs.google.com/spreadsheets/d/1yZv9w9zRKwrGTaR-YzmAqMefw4wMlaXocejdxZaTs6w/edit#gid=638231677")
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1wQVypefm946ch4XDp37uZ-wartW4V7ILdg-qYiDXUHM/htmlview?usp=sharing&sle=true")

spreadsheet_time_series = client.open_by_url("https://docs.google.com/spreadsheets/d/1UF2pSkFTURko2OvfHWWlFpDFAr1UxCBA4JLwlSP6KFo/htmlview?usp=sharing&sle=true")

#list of columns i want to keep
const_cols = ["Province/State", "Country", "Country/Region", "Date last updated", "Last Update", "Confirmed", "Recovered", "Deaths"]
#dict of column names to change
column_names = {"Country": "Country/Region", "Date last updated": "Last Update"}
#dict of columns and values to put in NaNs
fillna_values = {'Province/State': "", "Country/Region": "", "Confirmed": 0, "Recovered": 0, "Deaths":0}

list_dates = spreadsheet.worksheets()
list_time_series = spreadsheet_time_series.worksheets()

#list to help change column names
list_of_column_names = []

def read_spreadsheets(spreadsheet, list_dates,save):
    titles = []
    df_list = []

    for df in list_dates:
        #get worksheet as df
        title = df.title
        titles.append(title)
        df = get_as_dataframe(spreadsheet.worksheet(title))
        # delete columns i don't need
        for col in df.columns:
            if not col in const_cols:
                df = df.drop(labels=col, axis=1)
        #get column names that stayed in list of dfs
        for col in df.columns:
            if not col in list_of_column_names:
                list_of_column_names.append(col)

        #drop columns and rows with only NaNs
        df = df.dropna(axis=0, how='all')
        df = df.dropna(axis=1, how='all')

        # changing column names to standarise it
        df = df.rename(columns=column_names)

        #filling NaNs
        df = df.fillna(value=fillna_values)

        #adding dfs to df_list
        df_list.append(df)

    #save multiple sheets to excel
    if save == True:
        writer = pd.ExcelWriter('multiple_sheets_2019_nCoV.xlsx', engine='xlsxwriter')

        for i, df in enumerate(df_list, 0):
            df.to_excel(writer, sheet_name=titles[i], index=False)

        writer.save()

    return df_list

def big_df(df_list):
    #make df is a first date df for a start
    main_df = df_list[len(df_list) - 1]
    #adding next dfs to main_df
    for i in range(0, len(df_list) - 1):
        main_df = pd.concat([main_df, df_list[len(df_list) - 1 - i]], axis=0, ignore_index=True)
    return main_df

def read_time_series_spreadsheets(spreadsheet_time_series,list,save):
    titles = []
    df_list = []

    for df in list:
        # get worksheet as df
        title = df.title
        titles.append(title)
        df = get_as_dataframe(spreadsheet_time_series.worksheet(title))

        df = df.dropna(axis=0, how='all')
        df = df.dropna(axis=1, how='all')

        df_text = df[df.columns[0:2]]
        df_text = df_text.fillna(value = '')
        df_val = df[df.columns[2:len(df.columns)]]
        df_val = df_val.fillna(value = 0)
        df = pd.concat([df_text,df_val],axis=1)
        df_list.append(df)

    if save == True:
        writer = pd.ExcelWriter('time_series_2019_nCoV.xlsx', engine='xlsxwriter')

        for i, df in enumerate(df_list,0):
            df.to_excel(writer,sheet_name=titles[i], index=False)

        writer.save()

    return df_list

if __name__ == "__main__":

    #df_list = read_spreadsheets(spreadsheet,list_dates,save=True)

    time_series_df_list = read_time_series_spreadsheets(spreadsheet_time_series, list_time_series, save=True)

    #main_df = big_df(df_list)

    #main_df.to_excel('2019_nCoV.xlsx', sheet_name="2019_nCoV_all_data",index=False)

    # printing all columns - not only first few and last few
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(time_series_df_list[0])


