import gspread
from oauth2client.service_account import ServiceAccountCredentials
from plexapi.server import PlexServer
from plexapi.exceptions import NotFound

# the name of your movie library and spreadshee
LIBRARY = <YOUR MOVIES LIBRARY> # Ex: 'Movies'
GSPREAD_NAME = <YOUR SPREADSHEET NAME> # Ex: 'Movie Collections'

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# use creds to create a client to interact with your local Plex server
baseurl = <LOCAL PLEX ADDRESS> # Ex: 'http://xxx.xxx.x.x:32400'
token = <YOUR PLEX TOKE> # Plex Token
plex = PlexServer(baseurl, token)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(GSPREAD_NAME).sheet1
sheet = sheet.get_all_records()

# open a file to record missing movies
f= open("missing.txt","w").close()

# iterate through the sheet adding collection tags to the movies or record they are missing
for row in sheet:
  if len(str(row['Collection Name'])) > 1:
    collection_name = str(row['Collection Name'])

  if len(str(row['Movies'])):
    try:
      plex.library.section(LIBRARY).get(str(row['Movies'])).addCollection(collection_name)
      print("Adding {} to {}".format(row['Movies'], collection_name))
    except NotFound:
      f= open("missing.txt","a+")
      f.write(row['Movies'] + '\n')
      f.close
