from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pyhtmlreport import Report

report = Report() #Initializing report

### Getting Chrome Driver
driver = webdriver.Chrome(executable_path="G:\\chromedriver.exe")
driver.maximize_window()

report.setup(
    report_folder=r"F:\UAP\CSE 322 Project\Movie-Recommendation-System\Automated Testing Report",
    module_name="Report",
    release_name="Release 1",
    selenium_driver=driver
)

### Getting webpage
driver.get("http://localhost:8501")
time.sleep(3)
# print(driver.title)
# time.sleep(3)
## Test 1 (Landing Page)
try:
    report.write_step('Go to landing page', status=report.status.Start, test_number=1)

    assert(driver.title=="Movie Recommender System")
    report.write_step('Landing page loaded Successfully', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Landing page loading failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wring!', status=report.status.Warn, screenshot=True)

finally:
    report.generate_report()
time.sleep(3)


driver.close()
