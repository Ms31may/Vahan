import time
from click import filter_selector_2x2times, filter_selector_1x1times
from websiteOpen import openWebpage
def clickstep2(driver,df_xpath):
    while True:
        try:
            lefttray_xpath = df_xpath['absXpath']['left tray open button']
            driver.find_element("xpath", lefttray_xpath).click()
            time.sleep(1)                                             #wait 1 sec in case anything is running

            #select the correct options for y-axis=maker, x-axis=monthwise. 
            #yeartype cannot be changed when x axis is monthwise. year by default is cuurent year
            y_axis_selection = filter_selector_2x2times(driver,df_xpath['absXpath']['y-axis dropdown'],df_xpath['relXpath']['y-axis name'])
            x_axis_selection = filter_selector_2x2times(driver,df_xpath['absXpath']['x-axis dropdown'],df_xpath['relXpath']['x-axis name (monthwise)'])
            #yeartype_selection = filter_selector_2x2times(driver,df_xpath['absXpath']['year type dropdown'],df_xpath['relXpath']['year type name'])
            year_selection = filter_selector_1x1times(driver,df_xpath['relXpath']['year dropdown'],df_xpath['relXpath']['year name 2023'])
            yeartype_selection = "Calendar Year"
            topright_refresh_xpath = df_xpath['absXpath']['topright refresh button']
            driver.find_element("xpath", topright_refresh_xpath).click()
            time.sleep(4)
            print("completed step 2")

            break
        except:
            driver_open_time, driver = openWebpage(df_xpath)
            continue
    return driver






