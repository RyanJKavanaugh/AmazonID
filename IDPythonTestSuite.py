import unittest
import HTMLTestRunner
import os
from VerifyMenuOptions import Verify_Idaho_Menu_Options
from VerifyHeaderLinks import Verify_Idaho_Links
from VerifyCreateAndDeleteRoute import Verify_Login_And_Saving_Routes
from IDVerifyFDandTextSizes import Verify_Future_Dates_And_Text_Sizes
from VerifyUserLogin import Verify_Login
from VerifyMapLayers import Verify_Map_Layers
import xlrd
import sys

# /Users/ryankavanaugh/Desktop/AmazonLA/

workbook = xlrd.open_workbook('DataID.xlsx')
worksheet = workbook.sheet_by_index(0)
Jenkins = worksheet.cell(1, 4).value

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
#   1
left_hand_menu = unittest.TestLoader().loadTestsFromTestCase(Verify_Idaho_Menu_Options)
#   2
header_links = unittest.TestLoader().loadTestsFromTestCase(Verify_Idaho_Links)
#   3
future_dates_and_text_sizes = unittest.TestLoader().loadTestsFromTestCase(Verify_Future_Dates_And_Text_Sizes)
#   4
user_login = unittest.TestLoader().loadTestsFromTestCase(Verify_Login)
#   5
map_layers = unittest.TestLoader().loadTestsFromTestCase(Verify_Map_Layers)

#   6
create_and_delete_route = unittest.TestLoader().loadTestsFromTestCase(Verify_Login_And_Saving_Routes)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([left_hand_menu, header_links, future_dates_and_text_sizes, user_login, map_layers])

if Jenkins == True:
    # run the suite
    test_runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)
    result = test_runner.run(test_suite)
    sys.exit(not result.wasSuccessful())
else:
    # open the report file
    outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")


    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

    # run the suite using HTMLTestRunner
    runner.run(test_suite)