#!/usr/bin/python3

import requests
import json
from argparse import ArgumentParser
from datetime import datetime

def loadCookieFile(fileName):
    try:
        with open(fileName, 'r') as f:
            try:
                return json.loads(f.read())
            except Exception as e:
                print('[Error] {} : \'{}\''.format(e, fileName))
                exit()
    except IOError as e:
        print(e)
        exit()

def fetchData(batch, startdate, cookies):
    headers = {
        'Host': 'intranet.hbtn.io',
        'User-Agent': 'MPG v01',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }

    params = (
        ('batch_id', batch),
        ('calendar_view', '1'),
        ('curriculum_id', '1'),
        ('start_date', startdate),
    )

    response = requests.get('https://intranet.hbtn.io//dashboards/master_planning_data.json', headers=headers, params=params, cookies=cookies, verify=False)

    return response.text

def checkParams():
    parser = ArgumentParser(description='Holberton Intranet - Master Plan Get v.01.')
    parser.add_argument('-b','--batch', type=int, dest='batch',required=True, help='Batch number. Required.')
    parser.add_argument('-d', '--date', dest='startdate', type=str, help='Start date to fetch data (Format Y-m-d). Default = Today.')
    parser.add_argument('-c', '--cookiefile', dest='cookiefile', type=str, required=True, help='Cookie File Name. Required.')
    args = parser.parse_args()
    return args

def main():
    args = checkParams()
    batch = args.batch
    startDate = args.startdate
    if (startDate is None):
        startDate = datetime.today().strftime('%Y-%m-%d')
    cookieFile = args.cookiefile
    cookies = loadCookieFile(cookieFile)
    result = fetchData(batch, startDate, cookies)
    print(result)

if __name__ == '__main__':
    main()