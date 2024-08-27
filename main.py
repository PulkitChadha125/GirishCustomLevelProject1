import threading
import requests,XtsIntegration
import time
import traceback
from datetime import datetime, timedelta
import pandas as pd


def delete_file_contents(file_name):
    try:
        # Open the file in write mode, which truncates it (deletes contents)
        with open(file_name, 'w') as file:
            file.truncate(0)
        print(f"Contents of {file_name} have been deleted.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def get_user_settings():
    global result_dict
    # Symbol,lotsize,Stoploss,Target1,Target2,Target3,Target4,Target1Lotsize,Target2Lotsize,Target3Lotsize,Target4Lotsize,BreakEven,ReEntry
    try:
        csv_path = 'TradeSettings.csv'
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()
        result_dict = {}
        # Symbol,EMA1,EMA2,EMA3,EMA4,lotsize,Stoploss,Target,Tsl
        for index, row in df.iterrows():
            symbol_dict = {
                'Symbol': row['Symbol'],"Quantity":row['Quantity'],
                'EXPIERY': row['EXPIERY'],
            }
            result_dict[row['Symbol']] = symbol_dict
        print("result_dict: ", result_dict)
    except Exception as e:
        print("Error happened in fetching symbol", str(e))

get_user_settings()
def get_api_credentials():
    credentials = {}

    try:
        df = pd.read_csv('Credentials.csv')
        for index, row in df.iterrows():
            title = row['Title']
            value = row['Value']
            credentials[title] = value
    except pd.errors.EmptyDataError:
        print("The CSV file is empty or has no data.")
    except FileNotFoundError:
        print("The CSV file was not found.")
    except Exception as e:
        print("An error occurred while reading the CSV file:", str(e))

    return credentials


credentials_dict = get_api_credentials()
id=credentials_dict.get('id')
API_KEY=credentials_dict.get('API_KEY')
API_SECRET=credentials_dict.get('API_SECRET')
source=credentials_dict.get('source')
XTS_API_BASE_URL=credentials_dict.get('XTS_API_BASE_URL')
api_key_market=credentials_dict.get('api_key_market')
api_secret_market=credentials_dict.get('api_secret_market')


XtsIntegration.marketapilogin(api_key_market,api_secret_market,source)

XtsIntegration.login(API_KEY,API_SECRET,source)
XtsIntegration.ExchangeSegment()

def write_to_order_logs(message):
    with open('OrderLog.txt', 'a') as file:  # Open the file in append mode
        file.write(message + '\n')

def round_to_nearest(number, nearest):
    return round(number / nearest) * nearest



def main_strategy():
    print("main_strategy running ")
    try:
        for symbol, params in result_dict.items():
            symbol_value = params['Symbol']
            timestamp = datetime.now()
            timestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")

            if isinstance(symbol_value, str):
                pass



    except Exception as e:
        print("Error in main strategy : ", str(e))
        traceback.print_exc()


while True:
    main_strategy()
    time.sleep(2)

