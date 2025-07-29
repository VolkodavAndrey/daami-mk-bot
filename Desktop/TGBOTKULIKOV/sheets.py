import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import SPREADSHEET_NAME

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).sheet1

def save_to_sheet(data: list):
    sheet.append_row(data)