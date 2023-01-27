from click import filtered_selection
from driver import df_xpath
def listC(list_selections,driver):
    electric_checkbox_xpath = df_xpath['absXpath']['electric(BOV) checkbox']
    list_selections[0] = filtered_selection(df_xpath['absXpath']['Type dropdown'])
    list_selections[1] = filtered_selection(df_xpath['absXpath']['State dropdown'])
    list_selections[2] = filtered_selection(df_xpath['relXpath']['RTO dropdown'])
    list_selections[3] = filtered_selection(df_xpath['absXpath']['y-axis dropdown'])
    list_selections[4] = filtered_selection(df_xpath['absXpath']['x-axis dropdown'])
    #list_selections[5] = filtered_selection(df_xpath['absXpath']['year type dropdown'])
    list_selections[5] = "Calendar Year"
    list_selections[6] = filtered_selection(df_xpath['relXpath']['year dropdown'])
    list_selections[7] = not driver.find_element("xpath", electric_checkbox_xpath).is_selected()

    print(list_selections)

    return list_selections, driver