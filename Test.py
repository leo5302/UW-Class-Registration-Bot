import requests
import time
from selenium import webdriver

usr = 
pw =


def run():
    global usr, psw
    driver = webdriver.Chrome('/Users/leo5302/Downloads/chromedriver')   #要改
    login(driver, usr, pw)

    while getStatus(driver):
        print("Rechecking...")
        print()
        time.sleep(1)                                                    ＃延遲


def login(driver, id, pw):
    driver.get("https://sdb.admin.uw.edu/students/uwnetid/register.asp")
    username = driver.find_element_by_id("weblogin_netid")
    password = driver.find_element_by_id("weblogin_password")
    username.clear()
    password.clear()
    username.send_keys(id)
    password.send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()

def getStatus(driver):
    sln = ["15306", "15307", "15308", "15309", "15310", "15311", "15312", "15313"]   #sln codes最多支持8組
    #sln = ["13758"]   #Test
    driver.get(getUrl())
    current = driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[1]/tt").text
    limit = driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[2]/tt").text
    status = driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[2]/td[5]/tt/b").text
    
    if int(current) < int(limit):
        if status == 'Open':
            print("Found empty spot! Now trying to register class for you.")
            print()
            return register(driver, sln)
        else:
            print("Class has empty spot but " + status)
            print("Please manually check the class stats.")
            print("")
            check = pause()
            if check == '1':
                return True
            else:
                exit()
    elif current == limit:
        print("The class is full!")
        print()
        driver.refresh();
        return True

def register(driver, sln):
    driver.get("https://sdb.admin.uw.edu/students/uwnetid/register.asp")
    max = getMax(driver)
    for i in range(8):
        form = driver.find_element_by_name("sln" + str(max + 1 + i))
        form.clear()
        if i < len(sln):
            form.send_keys(sln[i])
    driver.find_element_by_xpath('//input[@value=\' Update Schedule \']').click()

    print("Checking if successfully registered...")
    check = driver.find_element_by_xpath('//*[@id="regform"]/p[2]/table/tbody/tr[2]/td[5]').text
    if check == ' ':
        print("Congradulation! Your class is registered.")
        return False
    else:
        print("Too late! The class is full again!")
        return True

def getMax(driver):
    return int(driver.find_element_by_name("maxdrops").get_attribute('value'))


def getUrl():      #Check url
    return "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=SPR+2020&SLN=15306"  #info
    #return "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=SPR+2020&SLN=16477"  #math
    #return "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=SUM+2020&SLN=12205"  #random
    #return "https://sdb.admin.uw.edu/timeschd/uwnetid/sln.asp?QTRYR=SPR+2020&SLN=13758"  #engl to test register


def pause():
    print("Enter 1 if you wish to continue checking")
    programPause = input("Enter other key if you want to exit the program: ")
    return programPause


run()
