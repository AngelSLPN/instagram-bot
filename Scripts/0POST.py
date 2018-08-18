import os
from InstagramAPI import InstagramAPI
import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI
from PIL import Image
import config

path = config.finalpath
IGCaption = config.caption
username = config.instagram_username
password = config.instagram_password
sleeptime = config.sleeptime_post

igapi = InstagramAPI(username, password)
igapi.login()  # login

def run_bot(POSTED):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for i in range(len(files)):
        for name in files:
            try:
                filesize = os.path.getsize(path + name)
                
                if filesize < 55000:
                    os.remove(path + name)
                else:
                        if name not in POSTED:
                            photo = path+name
                            print("file chosen:" + name)
                            print("Now Uploading this photo to instagram: " + photo)
                            igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
                            
                            POSTED.append(name)

                            with open ("POSTED.txt", "a") as f:
                                f.write(name + "\n")
                            print("new entry added")

                            print("pause upload for " + sleeptime + " seconds: ")
                            time.sleep(int(sleeptime))
            except RuntimeError:
                if os.path.exists(path + name):
                    os.remove(path + name)
                    print('corrupt file deleted')
            except FileNotFoundError:
                if os.path.exists(path + name):
                    os.remove(path + name)
                    print('corrupt file deleted')
            
                                
    
def get_already_posted():
	if not os.path.isfile("POSTED.txt"):
		POSTED = []
	else:
		with open("POSTED.txt", "r") as f:
			POSTED= f.read()
			POSTED = POSTED.split("\n")
			POSTED = list(filter(None, POSTED))

	return list(POSTED)


POSTED = get_already_posted()
print(POSTED)

while True:
	run_bot(POSTED)
