import requests as re
import json
import time
import datetime

def send_notice(event_name, key, text):
    url = "https://maker.ifttt.com/trigger/"+event_name+"/with/key/"+key+""
    payload = "{\n    \"value1\": \""+text+"\"\n}"
    response = re.request("POST", url, data=payload.encode('utf-8'))
    print(response)

while True:
    url = 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/(getAppsNear)?readform&cat=All&sbcat=All&typ=New&k=93F34F8445C14708BA82D6D13D3FCBD0&p=16688FC3EE841CE04BD1051D9075C70B&_=1632654390280'
    result = re.get(url)
    print(result.text)
    ans = json.loads(result.text)
    print(ans["empty"])
    key = ""
    if(ans["empty"] != "TRUE"):
        event_name = "notice_phone"
        text = result.text
        # response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
        # print(response.text)
        send_notice(event_name, key, text)
    else :
        now = datetime.datetime.now()
        if(now.hour == 0 and now.minute == 0 and now.second == 0):
            print('Done\n')
            text = '惨'
            send_notice('no_place', key, text)
        print('No place\n')
    time.sleep(60)