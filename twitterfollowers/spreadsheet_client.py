import gspread

from gspread.exceptions import APIError
from oauth2client.service_account import ServiceAccountCredentials


class SpreadsheetClient:
    def __init__(self, conf_file, spreadsheet_id):
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(conf_file, scope)

        client = gspread.authorize(credentials)
        self.sheet = client.open_by_key(spreadsheet_id).sheet1
        self._init_sheet()

    def _init_sheet(self):
        """
        Google Sheets documents have by default 1000 rows. Remove excess rows if there is
        no data stored.
        """
        try:
            a2 = self.sheet.acell('A2').value
        except APIError:
            a2 = None
        if not a2:
            print("No existing data found. Initializing sheet size to 1.")
            self.sheet.resize(1)

    def append_data(self, data):
        self.sheet.append_row(data)
