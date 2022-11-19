# -*- coding: utf-8 -*-
import pandas as pd
#Funtion to fill in missing data
def fillInVals(df, var, datatype = int):
    """Func to insert missing values. Argumens: df, name of object; var, 
    name of var as string; datatype, data type directly, no quotation marks"""
    df_copy = df[df[var].isna()]
    for rowIndex, series in df_copy.iterrows():
        print(rowIndex)
        print(series)
        insertVal = input("Insert missing val for " + var + " for\n" + str(df.iloc[rowIndex][["year", "AC"]])+":")
        if type(insertVal) is not datatype:
            if (datatype == int) | (datatype == float):
                insertVal = pd.to_numeric(insertVal)
        df.iloc[rowIndex, series.index.get_loc(var)] = insertVal
    return df