from tkinter import *
import selenium
from selenium import webdriver
from time import sleep
root = Tk()
root.geometry('600x400')
background = '#0d1b2a'
root.config(bg=background)

def sel():
    print('1')


def startApp():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://instagram.com')
    usernameEntry = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
    usernameEntry.send_keys(username_entry.get())
    
    passwordEntry = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
    passwordEntry.send_keys(password_entry.get())
    
    loginButton = driver.find_element_by_css_selector('#loginForm > div > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button')
    loginButton.click()
    sleep(5)
    
    driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()
    sleep(5)
    driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
    
    sleep(1)
    driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(3) > a > svg > path').click()
    

##? UserName 
    ##*     Label
username_label = Label(root, text='Enter Your Username: ', bg=background, fg='white', font=('Arial', 10))
    ##*     Entry
username_entry = Entry(root, width=25, borderwidth=2, bg='#7d8597' )
    ##! Packing
username_label.place(relx=0.15, rely=0.1, anchor='c')
username_entry.place(relx=0.42, rely=0.1, anchor='c')


##? PassWord 
    ##*     Label
password_label = Label(root, text='Enter Your Password: ', bg=background, fg='white', font=('Arial', 10))
    ##*     Entry
password_entry = Entry(root, width=25, borderwidth=2, bg='#7d8597' )
    ##! Packing
password_label.place(relx=0.15, rely=0.2, anchor='c')
password_entry.place(relx=0.42, rely=0.2, anchor='c')


##? Count
    ##*  Label
count_label = Label(root, text='Follow Count: ', bg=background, fg='white', font=('Arial', 10))
    ##*  Entry
count_entry = Entry(root, width=25, borderwidth=2, bg='#7d8597' )
    ##! Packing
count_label.place(relx=0.12, rely=0.3, anchor='c')
count_entry.place(relx=0.42, rely=0.3, anchor='c')

##? SendMessage 
    ##* Radio Button
var = IntVar()
message_radiobutton = Radiobutton(root, text="Send Message When The Proccess Is Complete", variable=var, value=1,command=sel, bg=background, fg='white',highlightcolor='black')
message_radiobutton.place(relx=0.25, rely=0.4, anchor='c')

##? Confirm 
    ##* Button
confirm_btn = Button(root, text='Confirm', bg=background, fg='white', borderwidth=2,padx=110, command=startApp)
confirm_btn.place(relx=0.25, rely=0.5, anchor='c')

##? Exit 
    ##* Button
exit_btn = Button(root, text=' Exit ', bg=background, fg='white', borderwidth=2,padx=120, command=root.destroy)
exit_btn.place(relx=0.25, rely=0.6, anchor='c')
root.mainloop()
