from   selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from   selenium.common.exceptions import TimeoutException
import time

TARGET_SITE = 'https://  . . . . . '

browser = webdriver.Firefox(executable_path = '/home/mantis444/Python/geckodriver')#local path to geckodr. file
browser.get( TARGET_SITE )
scheight = 9.9 # global var. used for scrolling down page, 9.9->10%


def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def Check_and_scroll_id( ide2 ):
    try:
        browser.find_element_by_id(ide2)
    except NoSuchElementException:
        return False
    return True

def Scroll_and_fill ( ide, szoveg ):
    if szoveg == "tick":
        buli = True
    else:
        buli = False
    global scheight
    while scheight > 1.0:

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight -= 0.8
        time.sleep(0.2)
        if Check_and_scroll_id(ide) and not buli :
            item = browser.find_element_by_id( ide)        
            item.click()
            item.clear()
            item.send_keys( szoveg )
            time.sleep(0.1)
            return
        elif Check_and_scroll_id(ide) and buli:
            item = browser.find_element_by_id( ide )
            if not item.is_selected():
                item.click()
    
    scheight = 9.9


err = "sem"  

browser.find_element_by_id("cookie_action_close_header").click()
print ( "SUCCCESS")
time.sleep(1)
browser.execute_script("window.scrollTo(0, 120);")


alap = " target email address , @ notation omitted"

for szam in range(5,len(alap)):

    #email = browser.find_element_by_id( "input_25_2" )
    print (szam)

    inydex = len(alap)
    if szam>2:
        sztr = alap[0:szam] + "." + alap[szam:inydex] + "@gmail.com"
    else :
        sztr = alap + "@gmail.com"
    print (sztr)

    Scroll_and_fill ("input_25_32", "Teszt")
    str3 = "Selenium Webdriver testcase - " + str(szam) + " - email:" + sztr
    Scroll_and_fill ("input_25_33", str3)
    Scroll_and_fill ("input_25_2", sztr)
    Scroll_and_fill ("input_25_23", "36987654321")
    Scroll_and_fill ("input_25_4", "tesztsykpe")

    Scroll_and_fill ("choice_25_40_1", "tick")
    Scroll_and_fill ("choice_25_15_0", "tick")
    Scroll_and_fill ("choice_25_44_0", "tick")
    Scroll_and_fill ("choice_25_8_0", "tick")
    Scroll_and_fill ("choice_25_30_0", "tick")
    Scroll_and_fill ("choice_25_10_1", "tick")
    Scroll_and_fill ("choice_25_25_1", "tick")

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    gombos = browser.find_element_by_id('gform_submit_button_25')
    gombos.click()
    time.sleep(6.1)

    browser.execute_script("window.scrollTo(0, 300)")

    osveny = "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div/div/form/div[2]/ul/li[3]/div[2]"
    if check_exists_by_xpath(osveny):
        err = browser.find_element_by_xpath(osveny).text
        print (err)
    else:
        err = "nix"
    browser.execute_script("window.history.go(-1)")
    time.sleep(8.1)
    osveny = "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div/div/form/div[1]/ul/li[1]/label"
    if not check_exists_by_xpath(osveny):
        print ("sign in form not found")
        browser.execute_script("window.history.go(-1)")
        time.sleep(5.5)
time.sleep(12)
browser.quit()

