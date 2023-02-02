from websiteOpen import openWebpage
from driver import df_xpath
from step2 import clickstep2
from step3 import clickstep3
from step5 import clickstep5
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By

print('Andaman  Nicobar Island','Andhra Pradesh','Arunachal Pradesh',
 'Assam','Bihar','Chhattisgarh',
 'Chandigarh','UT of DNH and DD',
 'Delhi','Goa','Gujarat','Himachal Pradesh','Haryana','Jharkhand','Jammu and Kashmir',
 'Karnataka','Kerala','Ladakh','Maharashtra','Meghalaya','Manipur','Madhya Pradesh',
 'Mizoram','Nagaland','Odisha','Punjab','Puducherry','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttarakhand','Uttar Pradesh','West Bengal')


state = input("Enter the state")
# ty= int(input("1 for Ev and 2 for non-ev"))


#open the webpage
driver_open_time, driver = openWebpage(df_xpath)
driver = clickstep2(driver,df_xpath)

for state_loop_counter in range(1,35):
    r = clickstep3(driver,df_xpath,state_loop_counter, state)
    if r:
        break


for state_loop_counter in range(1,35):
    r= clickstep5(driver,df_xpath,state_loop_counter, state)
    if r:
        break


