from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome(ChromeDriverManager().install())


def google_classroom(link):
     driver.get(link)

     #email
     email = driver.find_element_by_xpath('//*[@id="identifierId"]')
     email.send_keys("email")
   
     click = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
     click.click()
      
     time.sleep(10)

     #email
     email = driver.find_element_by_xpath('//*[@id="i0116"]')
     email.send_keys("email")

     click = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
     click.click()


     #password
     email = driver.find_element_by_xpath('//*[@id="i0118"]')
     email.send_keys("password")

     time.sleep(2)

     click = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
     click.click()


     #yes
     click = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
     click.click()

     time.sleep(3)

     #confirm
     click = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
     click.click()
          
     time.sleep(2)

#end of google_classroom function

def join_meeting_room(link):
     driver.get(link)
     time.sleep(3)
     click = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')
     click.click()

     #join the class
     click = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
     click.click()
     

#end of join_meetinf_room
    

def check_grade(link):
     driver.get(link)
     time.sleep(3)
     username = driver.find_element_by_xpath('//*[@id="ms_cph_txtUsername_txt"]')
     username.send_keys("username")
     password_c = driver.find_element_by_xpath('//*[@id="ms_cph_txtPassword_txt"]')
     password_c.send_keys("password")

     #login
     click = driver.find_element_by_xpath('//*[@id="ms_cph_btLogin_btn"]')
     click.click()   

#check_grade("https://sisportal.mpls.k12.mn.us/")
google_classroom("https://classroom.google.com/u/0/h")
join_meeting_room("https://meet.google.com/lookup/cmo6dld7jj")

 

