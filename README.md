# Twitter Followers

A small Python script that fetches the follower count from Twitter and pushes it to Google Sheets.


![Workflow](/img/workflow.png)

## Requirements
- Python 3

## Usage
1. Clone this repository somewhere on your machine 
1. Go to https://developer.twitter.com/ and create a Twitter developer account
1. Copy `twitter.json.example` to `twitter.json`
1. Register a new app in the Twitter developer page, go to Keys and tokens and copy all four secrets to `twitter.json`
1. Go to Google developer console https://console.developers.google.com/ and create service account keys for OAuth2.
1. Copy the JSON authentication file you got from Google inside this directory and name it `google.json`
1. Open the `google.json` file and copy the e-mail address from the `client_email` field
1. Go to Google Sheets https://docs.google.com/spreadsheets/u/0/, create a blank sheet, give it a descriptive name and share it to the service account e-mail
1. Call the `followers.sh` script, copy the spreadsheet id from the URL of your spreadsheet

```
 bash followers.sh --account <twitter_handle> --spreadsheet_id <id_from_url>
```

This will create a new Python virtualenv and install the required packages. Next, the script will try to fetch the follower count from the Twitter API and add a new entry to the spreadsheet with a timestamp.

You can run the script periodically with CRON to update the count for example once a day.
