import gspread
from helpers import methods
from testcase.testcase import TestCase

# API Ex. Jira: https://sprout.atlassian.net/rest/api/latest/issue/RTB-176
# Needs auth, check into jira API library for Python

print "Google Account Login"
email_addy = raw_input("Enter Email: ")
passwd = raw_input("Enter Password: ")

print "\nDocument Info"
ss_needed = 'Copy of Regression Tests'   # raw_input("Enter Spreadsheet Name (Exact): ")
ws_needed = 'Messages'  # raw_input("Enter Worksheet Name (Exact): ")
ws_desc_col = 'D'  # raw_input("Enter Description Column (Letter): ")
ws_steps_col = 'E'  # raw_input("Enter Steps Column (Letter): ")
ws_results_col = 'F'  # raw_input("Enter Results Column (Letter): ")
ws_start_at_row = 3  # raw_input("Enter Row to Start At (Number): ")


#login to google
client = gspread.login(email=email_addy, password=passwd)

#open spreadsheet
wb = client.open(ss_needed)

#grab specific page
ws = wb.worksheet(ws_needed)

#create an index from description column
index = methods.get_col_index(ws_desc_col)

#get the list of descriptions in that column
descriptions_list = ws.col_values(index)

#iterate through the descriptions list and build each case
for each_description in descriptions_list[ws_start_at_row-1:]:

    #parse the steps list based on the current descrip cell
    steps_list = methods.get_steps_list(
        worksheet=ws,
        cell=ws_steps_col+str(ws_start_at_row)
    )

    #parse the results list based on the current descrip cell
    results_list = methods.get_results_list(
        worksheet=ws,
        cell=ws_results_col+str(ws_start_at_row)
    )

    #create instance of test cases with these
    tc = TestCase(
        d=each_description,
        s=steps_list,
        r=results_list)

    print tc

    ws_start_at_row += 1

    #format test case to Jira formatting
