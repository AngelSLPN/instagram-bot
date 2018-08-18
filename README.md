# instagram-bot
# A FUCKING BIG-ASS DISCLAIMER: THIS IS STILL IN BETA AND I DON'T KNOW IF IT'S GONNA WORK

_intended function: steals memes from reddit, crops them and publishes to IG_
_Also can: just scrape images/vids from reddit, just make images square by adding white borders and batch posting images from a designated directory on instagram_

...

okay so I suppose not many people who came here know hnow to do this shit so I'm gonna write down a step-by-step tutorial which will hopefully help


# 1: INSTALL PYTHON!

_the scripts are running on python 3.x_
_that is a very important information because the most of the errors you'll get are because of running it on python 2.x_

(go here)[https://www.python.org/downloads/release/python-370/] , scroll down and choose your preferred version 

blah blah blah take steps according to the installer or however do you want JUST INSTALL THE SHIT

okay so now you should have python 3.7 installed 

when you now download and extract the folder in your preferred directory (do it!) and try to run one of the scripts, they'll
probably give you an error - that's because you don't have the needed modules installed. Let's fix that in our next step:

# 2: install needed packages (modules)

NOW: open command line (win key+R, type in `cmd` and hit run)
supposing you've installed your python distribution in the C:\ root, just paste in this command: 
`C:\python37\Scripts`
now you gotta paste every single of these lines and wait for the commands to execute
`pip install praw` - needed just if you want to steal memes from reddit
`pip install instagramAPI` - needed for posting on ig

# 3: understanding how shit works/setting up the scripts

if you look in the folder you have downloaded (if not, download it now you stupid sheep (the `Scripts` one)),
you'll see 8 files. 6 of those are python files of which are 5 executable scripts and one for configuring the thing.
assuming you are sorting by ~~new~~ name: the top four python scripts (beginning wit 0) are the main ones which are supposed to run all the time (that's why using a raspberry pi is better)

Explaining the functions of the files:
**1: 0CLEARDIR**  - this is a small script which is deleting all the files at 23:59, making sure you always post fresh memes and you don't run out of space

**2: 0CROP**  - this script takes all the images from the basic directory where the pics are downloaded, crops them and moves (not sure if that's true, maybe just copies, it doesn't matter) to the final directory from where they're posted (we'll get to setting this up later)

**3: 0DOWNLOAD**  - this little piece of shit steals (not just) memes (did you think it makes fucking OC huh) from reddit. you can chose the subreddit from where he'll downlad them.

**4: config** - I am sure you'll have fun with this file. this is the only file you will definitely have to edit if you want this shit to work. we'll get back to this later.

**5: CROPPED.txt**   - this file is totally useless and i'll maybe remove it from function later, but this is the file where the 0CROP script stores the names of already cropped images so it doesn't crop them more times and use your precious CPU power.

**6: POSTED.txt**  -  this file is not useless - the 0POST script writes names of already posted images to instagram. if this script wasn't there, the 0POST script would post the same pic on instagram more times.

**7: x**  - all this script does is it creates the path in config, you won't really need it

okay. now when you understand the scripts, you can start configuring. now, if you want the full functionality, you'll need a reddit account and a reddit "app"
so go here: https://www.reddit.com/prefs/apps, scroll down and click on 'create another app...'

now answer all the input fields honestly (I'm fucking kidding I don't care what you'll type there but I ain't responsible for that shit)

this is my setup:
```
name: 'Reddit parser'
○  web app	A web based application
○  installed app	An app intended for installation, such as on a mobile phone
•  script	Script for personal use. Will only have access to the developers accounts
description:	'steals memes from reddit'
about url: leave empty
redirect uri: 'http://localhost:8080'
```
don't ever forgetti to check the `script` option

now ye can click on `create app`

a new block with some important things will show up

leave the window open and open **config.py** with your favourite text editor (or just rightclick and click edit with IDLE.
now fill your reddit username and password in the brackets. now get back to your browser window. there will be a bunch of characters under the `personal use script` text. copy that and paste it between the `client_id` brackets. Get back to the browser again and copy the `secret` and paste it between `client_secret` brackets
now scroll down to the `path` and write down your desired path. (NOTE: if on Windows use \\ instead of \ because python is stupid. also don't forget to add a final \\ at the end of the directory (EXAMPLE: `D:\\porn\\hentai\\actuallynothentaibutmemesyouhavebeenfuckingrickrolled\\`))
in the finalpath just paste your path name and add final\\ at the end (`D:\\porn\\hentai\\actuallynothentaibutmemesyouhavebeenfuckingrickrolled\\final\\`)

now save the file and close your browser. - you can test the download feature now:

run `x.py` to create the needed directories

run the `0DOWNLOAD` script
((open with IDLE,run → run module, a new window will appear))

now just wait a minute untill the images get downloaded.

great. you have just downloaded tentacle hentai.

after you've finished ~~fapping~~ vomiting, get back to `config.py` and change the `subreddit_name` to your desired subreddit from which will the script steal (2meirl4meirl, dankmemes, wet_pussy, tightpussy (cat pics), earthporn (not actual porn),...) and change the download limit to a normal number (I use twenty so the memes stay good)

run `0DOWNLOAD` again. I suppose you have already removed the hentai. If not, close everything and get some serious help. 

now you can run the `0CROP` script.

now get back to the config file and add your instagram credentials and the image caption. you could enhance the script and make the captions different but I don't really need it so whatever. (NOTE: if you want to have any line breaks ("""""""enters""""""") in the caption, write `\n` instead of every line break. you can also change the sleep times for downloading and posting (in seconds) default is a four hour (14400s) delay for every posted image and batch downloads are made every two hours 

now save the config and run `0POST` 

if even this works, the bot should be ready for work!

# 4: running the bot

~~what are you stupid why are you reading this???~~ the only thing you really need to do now is to run `0DOWNLOAD`, `0CROP`, `0POST` and `0CLEARDIR` and just enjoy.

## ENJOY!
