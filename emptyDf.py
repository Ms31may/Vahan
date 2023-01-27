import pandas as pd
###################################################################################################################
#                                            DEFINE EMPTY DATA FRAMES
###################################################################################################################

df_combined = pd.DataFrame(columns = ['S No', 'data_extrcn_date', 'data_extrcn_epoch', 'state', 'RTO', 'Maker',
       'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
       'NOV', 'DEC', 'TOTAL'])

#define the columns for a df_diagnostics which will get appended with the filters selected during each file download
df_diagnostics = pd.DataFrame(columns = ['StateLoopNum','Type','State','RTO','Y-axis','X-axis','Year Type', 'Year',
                                        'tickbox-selected','RowsNum','ColsNum','DownloadStatus','DownloadTimestamp',
                                         'DownloadCheckItrnCount','TimeTaken(mins)','driverNum','column_mismatch_error'])

#define a temp df to append current df summary data to the df_diagnostics
df_temp = pd.DataFrame({'StateLoopNum':[], 'Type':[], 'State':[], 'RTO':[], 'Y-axis':[], 'X-axis':[], 'Year Type':[],
       'Year':[], 'tickbox-selected':[],'RowsNum':[], 'ColsNum':[], 'DownloadStatus':[],'DownloadTimestamp':[],
       'DownloadCheckItrnCount':[],'TimeTaken(mins)':[],'driverNum':[],'column_mismatch_error':[]})


