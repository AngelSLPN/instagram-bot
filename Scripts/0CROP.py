import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from PIL import Image, ImageOps
import sys
import config

path = config.path
finalpath = config.finalpath


def run_bot(CROPPED):
    checkCROPPED(CROPPED)
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for i in range(len(files)):
        for name in files:
            try:
                if name not in CROPPED:
                    photo = path+name
                    image = Image.open(path + name)
                    img = name
                    width = image.size[0]
                    height = image.size[1]
                    try:
                        
                        if width > height:
                            size = (width, width)
                            image.thumbnail(size, Image.ANTIALIAS)
                            background = Image.new('RGB', size, (255, 255, 255))
                            background.paste(
                                image, (int((size[0] - image.size[0]) / 2), int((size[1] - image.size[1]) / 2))
                            )
                            background.save(finalpath + img + "new.jpg" , 'JPEG')
                            os.remove(path + img)
                                
                        elif width < height:
                            size = (height, height)
                            image.thumbnail(size, Image.ANTIALIAS)
                            background = Image.new('RGB', size, (255, 255, 255))
                            background.paste(
                                image, (int((size[0] - image.size[0]) / 2), int((size[1] - image.size[1]) / 2))
                            )
                            background.save(finalpath + img + "new.jpg" , 'JPEG')
                            os.remove(path + img)
                                
                        else:
                            image.save(finalpath + img + "new.jpg" , 'JPEG')
                            os.remove(path + img)
                                
                        checkCROPPED(CROPPED)
                        if name not in CROPPED:
                            print("NEW ENTRY " + name)
                            with open ("CROPPED.txt", "a") as f:
                                f.write(name + "\n")
                            print("new entry added")
                                                   
                            
                    except IOError:
                        print("ERROR")
                        time.sleep(6)
                        if os.path.exists(path + img):
                            print('exists?')
                            os.remove(path + img)
                        
                        else:
                            print("FILE FOR DELETION DOESN'T EXIST, FOLDER IS PROBABLY EMPTY")
                            print("WAITING FOR 10min UNTIL NEXT SCAN...")
                        time.sleep(600)
                        
            except IOError:
                time.sleep(6)
                if os.path.exists(path + name):
                    os.remove(path + name)
                    print('corrupt file deleted')
                else:
                    print("no more images to crop, waiting...")
                    time.sleep(1800)
                
                        
def checkCROPPED(self):
    if not os.path.isfile("CROPPED.txt"):
                CROPPED = []
    else:
                with open("CROPPED.txt", "r") as f:
                        CROPPED= f.read()
                        CROPPED = CROPPED.split("\n")
                        CROPPED = list(filter(None, CROPPED))

    return list(CROPPED)


            
       
    
def get_already_cropped():
	if not os.path.isfile("CROPPED.txt"):
		CROPPED = []
	else:
		with open("CROPPED.txt", "r") as f:
			CROPPED= f.read()
			CROPPED = CROPPED.split("\n")
			CROPPED = list(filter(None, CROPPED))

	return list(CROPPED)


CROPPED = get_already_cropped()
print(CROPPED)

while True:
	run_bot(CROPPED)
