'''
Users Hook

- Used as a hook for fetching ROBLOX Users informations
  - Including Last Online information
'''

import requests
import json

def getFromId(userId: int):
    # Last Online Informations
    x = requests.post('https://presence.roblox.com/v1/presence/last-online', json={'userIds': [userId]})
    x = x.text
    x = json.loads(x)

    # User Informations
    user_infos = requests.get('https://users.roblox.com/v1/users/'+str(userId))
    user_infos = user_infos.text
    user_infos = json.loads(user_infos)

    # Format the account creation date
    createdOn = user_infos['created'].split('T')[0].split('-')
    createdOn[0], createdOn[2] = createdOn[2], createdOn[0]
    createdOn = '/'.join(createdOn)

    # Format the last online timestamp
    lastOnlineTime = x['lastOnlineTimestamps'][0]['lastOnline'].split('T')[1].split('-')[0].split('.')[0].split(':')
    lastOnlineTime[0] = str(int(lastOnlineTime[0])+3)
    lastOnlineTime = ':'.join(lastOnlineTime)

    # Format the last online date
    lastOnlineDate = x['lastOnlineTimestamps'][0]['lastOnline'].split('T')[0].split('-')
    lastOnlineDate[0], lastOnlineDate[2] = lastOnlineDate[2], lastOnlineDate[0]
    lastOnlineDate = '/'.join(lastOnlineDate)

    # Last Online Formatted
    lastOnline = lastOnlineTime + f" - ({lastOnlineDate})"
    
    print(f"{user_infos['name']}'s Infos:\n- Display Name: {user_infos['displayName']}\n- Last Online: {lastOnline}\n- Created: {createdOn}\n- ID: {userId}")
