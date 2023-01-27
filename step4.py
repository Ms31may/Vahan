import pandas as pd
import numpy as np
from emptyDf import df_combined
from datetime import datetime
import time
def transFormDf(newName, dummyState, dummyRTO, download_EPOCH):
    
    df = pd.read_excel(newName,engine="openpyxl")
    time.sleep(1)
    df.iloc[[2],[0]] = df.iloc[[0],[0]].copy()
    df.iloc[[2],[1]] = df.iloc[[0],[1]].copy()
    df.iloc[[2],[-1]] = df.iloc[[0],[-1]].copy()
    df = df.drop(index = [0,1])
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header

        #add state column and move it to left after maker column
    df['state'] = dummyState
    df['RTO'] = dummyRTO
    df['data_extrcn_date'] = datetime.today().strftime('%Y-%m-%d')
    df['data_extrcn_epoch'] = round(download_EPOCH,0)
    df.rename(columns = {'\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Maker \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0':'Maker'}, inplace = True)
    df.rename(columns = {'\xa0\xa0\xa0\xa0\xa0TOTAL\xa0\xa0\xa0\xa0\xa0':'TOTAL'}, inplace = True)
    time.sleep(1)

    return df

