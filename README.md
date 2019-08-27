# Collections Auto Tag

https://www.reddit.com/r/PleX/comments/cvgl97/im_making_a_big_list_of_movie_collections/

Using the spreadsheet linked in the above post, I wanted to try and write a script that would automatically tag movies on a Plex server with the related collections. I'm still relatively new to Python and coding in general but here's an attempt. 

I wasn't able to do a lot of testing as I was missing quite a few of the movies, but I added a feature that will create a .txt file to keep track of which movies are missing. Hopefully, someone will find it useful!

# Instructions
To get this to work, I copied a version of the spreadsheet to my Drive account and set up an API service for that. I used the following guide to achieve this. I'm sure there is a far better way to achieve this, but I wasn't sure if there were security concerns linking it to my API.

https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

From there, I create some variable that should be changed for your specific Drive and Plex credentials.
Finally to run this script make sure oauth2client, gspread, and the Plex API wrapper are all installed.
