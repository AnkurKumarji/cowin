import requests
from os import system
from time import sleep
from datetime import datetime,timedelta
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def CheckAvalibility():
    center_id = '702330'
    # center_id = '782095'
    dates,urls,data,vaxin_data = ([] for i in range(4))
    for i in range(3):dates.append((datetime.today()+timedelta(i)).strftime('%d-%m-%Y'))
    for date in dates:urls.append(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter?center_id={center_id}&date={date}')
    for url  in urls:data.append(requests.get(url).json())

    for dta in data:
        try:
            if dta['centers']['sessions'][0]['vaccine'] == 'COVISHIELD':
                print("True",dta['centers']['sessions'][0]['date'])
                try:
                    system('termux-media-player play run.mp3')
                    sleep(20)
                    system('termux-media-player stop run.mp3')
                    exit(0)
                except: exit(0)
        except:pass
    return 0

while True:
    CheckAvalibility()
    sleep(30)