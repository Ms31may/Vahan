import time
from click import filter_selector_2x2times, filter_selector_1x1times, filtered_selection
import os
from driver import driver as dr1
import configparser
import glob
from step2 import clickstep2

from websiteOpen import openWebpage
import pandas as pd
from listC import listC
import datetime
from step4 import transFormDf
#######################################################################################################################################################################

df_combined = pd.DataFrame(columns = ['S No', 'data_extrcn_date', 'data_extrcn_epoch', 'state', 'RTO', 'Maker',
       'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
       'NOV', 'DEC', 'TOTAL'])


#######################################################################################################################################################################
values = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
def remover(my_string = ""):
  for item in my_string:
    if item not in values:
      my_string = my_string.replace(item, "")
  return my_string


#######################################################################################################################################################################
config = configparser.ConfigParser()
config.readfp(open(r'config.ini'))
def clickstep3(driver,df_xpath,state_loop_counter, state, ty):
    global df_combined
    dummyState = filter_selector_2x2times(driver,df_xpath['absXpath']['State dropdown'],df_xpath['absXpath']['state'+str(state_loop_counter)])
    dummystate1 = remover(dummyState)
    print(dummystate1)
    if dummystate1  in state:


        time.sleep(1)
        rto_count = int(dummyState.split('(')[1].split(')')[0])
        print(dummyState," has ",rto_count," rto offices")
        ctd = 0
        for rto_loop_counter in range(1,rto_count+1):
            try:
                dummyRTO = filter_selector_1x1times(driver,df_xpath['relXpath']['RTO dropdown'],df_xpath['relXpath']['rto'+str(rto_loop_counter)])
                time.sleep(1)
                topright_refresh_xpath = df_xpath['absXpath']['topright refresh button']
                driver.find_element("xpath", topright_refresh_xpath).click()
                time.sleep(2.5)
                                                        

                lefttray_refresh_xpath = df_xpath['absXpath']['left tray refresh button']
                TWOwhIC_checkbox_xpath = df_xpath['relXpath']['2WH(IC) checkbox']
                TWOwhNT_checkbox_xpath = df_xpath['relXpath']['2WH(NT) checkbox']
                TWOwhT_checkbox_xpath = df_xpath['relXpath']['2WH(T) checkbox']
                electric_checkbox_xpath = df_xpath['absXpath']['electric(BOV) checkbox']

                
                driver.find_element("xpath", topright_refresh_xpath).click()
                time.sleep(2)
                
                                                            #wait 1.5 sec in case anything is running

                #click on Fuel: ELectric(BOV) in teh left tray
                if ty == 1:
                    time.sleep(1)
                    driver.find_element("xpath", electric_checkbox_xpath).click()
                    time.sleep(1)
                
                                                                    #wait 1 sec in case anything is running

                #click on 2wh IC, NT, T in teh left tray
                driver.find_element("xpath", TWOwhIC_checkbox_xpath).click()
                time.sleep(0.5)                                             #wait 0.3 sec in case anything is running
                driver.find_element("xpath", TWOwhNT_checkbox_xpath).click()
                time.sleep(0.5)                                             #wait 0.3 sec in case anything is running
                driver.find_element("xpath", TWOwhT_checkbox_xpath).click()
                time.sleep(0.5)    
                
                    
                                        #wait 0.3 sec in case anything is running

                #click on the left tray refresh button
                # print("refreshing left tray")
                driver.find_element("xpath", lefttray_refresh_xpath).click()
                time.sleep(2)


                # time.sleep(2) 
                finished = False
                user = os.getlogin()
                download_folder_link = "C:\\Users\\mohit\\Desktop\\TorkMotors\\Vahan\\TorkMotorsProject\\download_vahan\\"
                files_path = os.path.join(download_folder_link, '*')
                files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)           
                driver.find_element("xpath", df_xpath['absXpath']['xlsheet download button']).click()
                download_EPOCH = time.time()
                time.sleep(2)
                folder_path = download_folder_link
                file_type = r'\*xlsx'
                files = glob.glob(folder_path + file_type)
        

                oldName = max(files, key=os.path.getctime)
                newName1 = os.path.join(folder_path, dummyState+'_'+dummyRTO+'_EPOCH_'+str(round(download_EPOCH))+'.xlsx')
                os.rename(oldName, newName1)
                time.sleep(5)
                newName = newName1
            except Exception as e:
                # print(e)
                driver_open_time, driver = openWebpage(df_xpath)
                driver = clickstep2(driver,df_xpath)
                dummyState = filter_selector_2x2times(driver,df_xpath['absXpath']['State dropdown'],df_xpath['absXpath']['state'+str(state_loop_counter)])
                time.sleep(1)
                rto_loop_counter = rto_loop_counter -1
                continue
        
            df = transFormDf(newName, dummyState, dummyRTO, download_EPOCH)
            df_combined = pd.concat([df_combined, df], ignore_index=True)
            print(df_combined.tail(10))
            ctd =ctd+1
            if ctd == 10000000:
                break

                    #add state column and move it to left after maker column
        df_combined.to_csv(f'df_combined_allBike_ev_nonEV_{dummyState}.csv')

        

    else:
        pass
    
    
##############################################################################################################################################################1


##############################################################################################################################################################3

            





       


            



