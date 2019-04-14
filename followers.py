import argparse
import datetime
import os
import sys
from twitterfollowers.twitter_client import TwitterClient
from twitterfollowers.spreadsheet_client import SpreadsheetClient

SCRIPT_DIR = sys.path[0]


def main(twitter_account, spreadsheet_id, twitter_auth, google_auth):
    twitter_client = TwitterClient(twitter_auth)
    spreadsheet_client = SpreadsheetClient(google_auth, spreadsheet_id)

    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S") 
    print("Fetch follower count for {}".format(twitter_account))
    data = [now, twitter_client.get_follower_count(twitter_account)]
    print(data)

    print("Update spreadsheet")
    spreadsheet_client.append_data(data)
    print("Finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Store Twitter follower count to Google Sheets')
    parser.add_argument('--account',
                        help="Twitter account name")
    parser.add_argument('--spreadsheet_id',
                        help='Spreadsheet ID from the Google Sheets URL')
    parser.add_argument('-g', '--google_auth',
                        help='Google authentication file, default "google.json"',
                        default=os.path.join(SCRIPT_DIR, "google.json"))
    parser.add_argument('-t', '--twitter_auth',
                        help='Twitter authentication file, default "twitter.json"',
                        default=os.path.join(SCRIPT_DIR, "twitter.json"))
    args = parser.parse_args()

    main(
            twitter_account=args.account,
            spreadsheet_id=args.spreadsheet_id,
            twitter_auth=args.twitter_auth,
            google_auth=args.google_auth
    )
