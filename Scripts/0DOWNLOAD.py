import praw
import config
import time
import os
import prawcore.exceptions
from urllib.error import URLError, HTTPError
import urllib.request as web
import shutil # shell utilities


path = config.path
subreddit_name = config.subreddit_name
download_limit = config.download_limit
sleeptime = config.sleeptime_download

def main(subreddit_name, current_dir = os.getcwd()):
    reddit = praw.Reddit(
        client_id = config.client_id, 
        client_secret = config.client_secret,
        username = config.username, 
        password = config.password, 
        user_agent = 'subreddit crawler')

    if not os.path.exists(path):
        os.mkdir(path)

    subreddit = reddit.subreddit(subreddit_name).hot(limit= int(download_limit))

    print("Downloading files...")

    for submissions in subreddit:
        if not submissions.stickied and submissions.score > 50:
            fullfilename = os.path.join(path, "{}.jpg".format(submissions))
            request = web.Request(submissions.url, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
            with web.urlopen(request) as response, open(fullfilename, 'wb') as out_file:                
                try:
                    shutil.copyfileobj(response, out_file)
                except HTTPError as e:
                    print("{}{}{}".format(Fore.RED, e.code, Style.RESET_ALL))
                except URLError as e:
                    print("{}{}{}".format(Fore.RED, e.reason, Style.RESET_ALL))                 

            # delete corrupted files smaller than 55 KB
            filesize = os.path.getsize(fullfilename)
            if filesize < 55000:
                os.remove(fullfilename)
            #else:
                # this is for debugging purposes only
                #temp = "{}[{:07d}KB]{}".format(Fore.GREEN, filesize, Style.RESET_ALL)
                #print("{} ID: {} URL: {}".format(temp, submissions, submissions.url))

    dir_count = len(os.listdir(path))
    print("Download succeeded. {} files saved in '{}'.".format(dir_count, path))
	print("sleeping for " + sleeptime + " seconds")
    time.sleep(int(sleeptime)
	

if __name__ == '__main__':
    main(subreddit_name)

while True:
        main(subreddit_name, current_dir = os.getcwd())

