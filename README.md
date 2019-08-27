Plex Movie Collections
=====================

Overview
--------
Most importantly, thank you /u/hotdog218 for creating this sheet and everyone who contributed. 

https://www.reddit.com/r/PleX/comments/cvgl97/im_making_a_big_list_of_movie_collections/

Using the spreadsheet linked in the above post, I wanted to try and write a script that would automatically tag movies on a Plex server with the related collections. I'm still relatively new to Python and coding in general but here's an attempt. 

I wasn't able to do a lot of testing as I was missing quite a few of the movies, but I added a feature that will create a .txt file to keep track of which movies are missing. Hopefully, someone will find it useful!

Instructions & Documentation
----------------------------
To get this to work, I copied a version of the spreadsheet to my Drive account and set up an API service for that. I used the following guide to achieve this. I'm sure there is a far better way to achieve this, but I wasn't sure if there were security concerns linking it to my API.

https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

Next, you must change the following variables in the plex_collections.py file to match your server credentials:

``` python
# the name of your movie library and spreadsheet
LIBRARY = <YOUR MOVIES LIBRARY> # Ex: 'Movies'
GSPREAD_NAME = <YOUR SPREADSHEET NAME> # Ex: 'Movie Collections'

# use creds to create a client to interact with your local Plex server
PLEXURL = <LOCAL PLEX ADDRESS> # Ex: 'http://xxx.xxx.x.x:32400'
TOKEN = <YOUR PLEX TOKE> # Plex Token
```

Finally, to run this script make sure oauth2client, gspread, and the Plex API wrapper are all installed. To do so, run the following command in the command prompt:

```
pip install plexapi oauth2client gspread
```

Usage
-----
To run the script, run the following in command prompt:

```
python3 plex_collections.py
```

While I haven't tested it, the script should hypothetically work for any Google Spreadsheet that is formatted in the same way as the one provided by /u/hotdog218 from the Reddit post.
