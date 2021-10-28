from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

lastmsgid=""
sendedmsgid=""
umsg,rmsg=[],[]
with open('msg.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')           
    for row in csv_reader:
        umsg.append(row[0])
        rmsg.append(row[1])

def sendmsg(replaymsg):
    actions = ActionChains(driver)
    actions.send_keys(replaymsg)
    actions.perform()
    sendbutton=driver.find_element_by_class_name("send")
    sendbutton.click()


driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://web.telegram.org/z/")

login=input("are you logged in  and is group selected: ")
while True:
    msgs=driver.find_elements_by_class_name("Message")
    msgsfromuser=driver.find_elements_by_class_name("text-content")
    msgstime=driver.find_elements_by_class_name("message-time")
    #index=0
    #for i in msgs:
    #    msgtime=msgstime[index].text
    #    msg=str(i.text).replace("\n"+msgtime,"")
    #    print(msg)
    #    index=index+1
    msgslength=len(msgs)
    lastmsg=msgs[msgslength-1]
    if lastmsgid==None:
        lastmsgid=lastmsg.get_attribute("data-message-id")
    if lastmsgid!=lastmsg.get_attribute("data-message-id"):
        msgtime=msgstime[msgslength-1].text
        cmsg=str(msgsfromuser[len(msgsfromuser)-1].text).replace("\n"+msgtime,"")
        index=0
        for i in umsg:
            if str(i).lower()==cmsg.lower():
                if sendedmsgid !=lastmsg.get_attribute("data-message-id"):
                    sendmsg(rmsg[index])
                    sendedmsgid=lastmsg.get_attribute("data-message-id")
            index=index+1
    
