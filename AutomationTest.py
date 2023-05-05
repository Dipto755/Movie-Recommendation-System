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

## Test 1 (Landing Page)
try:
    report.write_step('Go to landing page', status=report.status.Start, test_number=1)

    assert(driver.title=="Movie Recommender System")
    report.write_step('Landing page loaded Successfully', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Landing page loading failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


## Test 2 (Selecting recommendation type)
try:
    report.write_step('Selecting Recommendation Type', status=report.status.Start, test_number=2)

    ### Selecting recommendation type (movie)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[4]/div/div/div/div[1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/div/div/li[2]/div/div/div").click()
    time.sleep(2)

    recom_type = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[4]/div/div/div/div[1]/div[1]").text

    assert(recom_type != "--Select--")
    report.write_step('Selection of Recommendation type Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of Recommendation type failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


## Test 3 (Selecting movie)
try:
    report.write_step('Selecting Movie with poster', status=report.status.Start, test_number=3)

    ### Selection movie (this time : "Harry Potter" with poster)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]/div/input").send_keys("Harry Potter and the Sorcerer's Stone"+Keys.ENTER)
    time.sleep(5)

    movie = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]/div[1]").text

    assert(movie == "Harry Potter and the Sorcerer's Stone")
    report.write_step('Selection of Movie (Harry Potter and the Sorcerers Stone) Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of Movie (Harry Potter and the Sorcerers Stone) failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


## Test 4 (Selecting another movie)
try:
    report.write_step('Selecting another Movie with poster', status=report.status.Start, test_number=4)

    ### Selection movie (this time : "Toy Story" with poster)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]/div/input").send_keys("Toy Story"+Keys.ENTER)
    time.sleep(2)

    movie = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]/div[1]").text

    assert(movie == "Toy Story")
    report.write_step('Selection of Movie (Toy Story) Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of Movie (Toy Story) failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


## Test 5 (Selecting poster fetch option to no)
try:
    report.write_step('Selecting poster fetch option to no' , status=report.status.Start, test_number=5)

    ### Selecting fetch poster option to 'NO'
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[6]/div/div/label[2]/div[1]').click()
    time.sleep(2)

    optn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[6]/div/div/label[2]/div[2]").text

    assert(optn == "No")
    report.write_step('Selection of poster fetch option to no Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of poster fetch option to no failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)

## Test 6 (Selecting movie)
try:
    report.write_step('Selecting Movie without poster', status=report.status.Start, test_number=6)

    ### Selection movie (this time : "Harry Potter" without poster)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]/div/input").send_keys("Harry Potter and the Sorcerer's Stone"+Keys.ENTER)
    time.sleep(5)

    movie = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div[1]/div[1]").text

    assert(movie == "Harry Potter and the Sorcerer's Stone")
    report.write_step('Selection of Movie without poster (Harry Potter and the Sorcerers Stone) Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of Movie without poster (Harry Potter and the Sorcerers Stone) failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


## Test 7 (Selecting recommendation type (Genre))
try:
    report.write_step('Selecting Recommendation Type (Genre)', status=report.status.Start, test_number=7)

    ### Selecting recommendation type (genre)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[4]/div/div/div/div[1]/div/input").send_keys("Genre based"+Keys.ENTER)
    time.sleep(2)

    recom_type = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[4]/div/div/div/div[1]/div[1]").text

    assert(recom_type == "Genre based")
    report.write_step('Selection of Recommendation type (Genre) Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of Recommendation type (Genre) failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


## Test 8 (Selecting movie genres)
try:
    report.write_step('Selecting Movie Genres without poster', status=report.status.Start, test_number=8)

    ### Selection movie genres without poster
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div/div[1]/div[2]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div/div[1]/div/input").send_keys("Crime"+Keys.ENTER)
    time.sleep(1)

    genre = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[2]/div[1]/div[1]/div/div[5]/div/div/div/div/div[1]").text

    assert(genre == "Crime")
    report.write_step('Selection of Movie genre without poster Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Selection of Movie genre without poster failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)

## Test 9 (about section)
try:
    report.write_step('Expanding about section', status=report.status.Start, test_number=9)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/button/svg").click()
    time.sleep(2)

    text = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/label/div/p").text
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)

## Test 10
try:
    report.write_step('Landing about section', status=report.status.Start, test_number=10)

    assert (driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/button/svg"))
    report.write_step('Landing about section Successful', status=report.status.Pass, screenshot=True)
except AssertionError:
    report.write_step('Landing about section failed!', status=report.status.Fail, screenshot=True)
except Exception as e:
    report.write_step('Something went Wrong!', status=report.status.Warn, screenshot=True)


finally:
    report.generate_report()


time.sleep(3)
driver.close()
