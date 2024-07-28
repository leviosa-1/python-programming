import pyautogui as pg
import time
limit=input("Enter no. messages ")
msg=input("Enter your message ")
i=0
print("starting in 5 sec....")
time.sleep(5)

while i<int(limit):
   
    pg.typewrite(msg)
    pg.press("Enter")
    i+=1
    
    
