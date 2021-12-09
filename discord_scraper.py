import requests
import json

def retrieveMessage(channel):
    headers = {
        'authorization': 'NTQ5NjgwNzY0MjM3Nzc0ODUw.YYTFGg.uqUElYolGooNaZPKW9TGzCRqGlg'
        
        }
    url = f'https://discord.com/api/v9/channels/{channel}/messages?limit=101'
    r=requests.get(url, headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        try:
            if value['author']['username'] == 'BeanZ':
                print('Chuka:',value['content'])
        except TypeError:
            print(value)
retrieveMessage('627538418943000597')
