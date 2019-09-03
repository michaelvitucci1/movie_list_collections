import gspread
from oauth2client.service_account import ServiceAccountCredentials
from plexapi.server import PlexServer
from plexapi.exceptions import NotFound
import math

# the name of your movie library and spreadshee
LIBRARY = <YOUR MOVIES LIBRARY> # Ex: 'Movies'
GSPREAD_NAME = <SPREADSHEET NAME> # Ex: 'Movie Collections'

# use creds to create a client to interact with your local Plex server
PLEXURL = <PLEX URL> # Ex: 'http://xxx.xxx.x.x:32400'
TOKEN = <PLEX TOKEN> # Plex Token


# create an instance of PlexServer
plex = PlexServer(PLEXURL, TOKEN)

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open(GSPREAD_NAME).sheet1
sheet = sheet.get_all_records()

def record_missing():
  f= open("missing.txt","a+", encoding='utf8')
  f.write(str(row['Movies']) + '\n')
  f.close

# open and clear a file to record missing movies
f= open("missing.txt","w").close()

# iterate through the sheet adding collection tags to the movies or record they are missing
for row in sheet:
  if len(str(row['Collection Name'])) > 1:
    collection_name = str(row['Collection Name'])
  if len(str(row['Movies'])):
    if isinstance(row['Year'], str):
      record_missing()
    else:
      try:
        plex.library.section(LIBRARY).search(str(row['Movies']), year=row['Year'])[0].addCollection(collection_name)
        print("Adding {} to {}".format(row['Movies'], collection_name))
      except (NotFound, IndexError):
        record_missing()
