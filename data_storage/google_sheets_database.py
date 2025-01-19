import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .base_database import DatabaseInterface

class GoogleSheetsDatabase(DatabaseInterface):
    def __init__(self):
        self.sheet = None

    def connect(self):
        creds_file = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "credentials.json")
        scope = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        client = gspread.authorize(creds)
        sheet_name = os.getenv("GOOGLE_SHEETS_NAME", "MySheet")
        self.sheet = client.open(sheet_name).sheet1
        print(f"Connected to Google Sheets: {sheet_name}")

    def insert(self, data):
        self.sheet.append_row(list(data.values()))
        print("Data inserted into Google Sheets.")

    def query(self, query_params):
        rows = self.sheet.get_all_records()
        return [row for row in rows if row.get("col1") == query_params.get("col1")]
