import schedule
import time
import config
import os
import shutil

path = config.path
finalpath = config.finalpath

def job():
    print("deleting...")
    shutil.rmtree(path)
    os.makedirs(finalpath)
    

schedule.every().day.at("23:59").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)



def job():
    print("deleting...")

schedule.every().day.at("23:59").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
