'''
User Hook File

- Used as a hook for fetching ROBLOX Users informations
  - Including Last Online information
'''

import requests
import json

class UserHook:
    accountId = 0
    
    success = True
    started = False

    user_infos = {}
    createdOnHook = ''
    lastOnlineTime = ''
    lastOnlineDate = ''
    lastOnlineHook = ''
    
    def __init__(self, accountId):
        self.accountId = accountId

    def hookStart(self):
        try:
            # Last Online Informations
            x = requests.post('https://presence.roblox.com/v1/presence/last-online', json={'userIds': [self.accountId]})
            x = x.text
            x = json.loads(x)

            # User Informations
            user_infos = requests.get('https://users.roblox.com/v1/users/'+str(self.accountId))
            user_infos = user_infos.text
            self.user_infos = json.loads(user_infos)

            # Format the account creation date
            createdOn = self.user_infos['created'].split('T')[0].split('-')
            createdOn[0], createdOn[2] = createdOn[2], createdOn[0]
            self.createdOnHook = '/'.join(createdOn)

            # Format the last online timestamp
            lastOnlineTime = x['lastOnlineTimestamps'][0]['lastOnline'].split('T')[1].split('-')[0].split('.')[0].split(':')
            lastOnlineTime[0] = str(int(lastOnlineTime[0])+3)
            self.lastOnlineTime = ':'.join(lastOnlineTime)

            # Format the last online date
            lastOnlineDate = x['lastOnlineTimestamps'][0]['lastOnline'].split('T')[0].split('-')
            lastOnlineDate[0], lastOnlineDate[2] = lastOnlineDate[2], lastOnlineDate[0]
            self.lastOnlineDate = '/'.join(lastOnlineDate)

            # Last Online Formatted
            self.lastOnlineHook = self.lastOnlineTime + f" - ({self.lastOnlineDate})"

            self.success = True
            self.started = True
        except:
            print(f'[!] Could not initialize the hook. Something went wrong.')
            self.success = False
            self.started = False

    def showInfos(self):
        if self.success and self.started:
            print(f"{self.user_infos['name']}'s Infos:\n- Display Name: {self.user_infos['displayName']}\n- Last Online: {self.lastOnlineHook}\n- Created: {self.createdOnHook}\n- ID: {self.accountId}")
        elif not self.started:
            print('>>> Initialize the hook before executing this command')

    def createdOn(self):
        if self.success and self.started:
            print(f"{self.user_infos['name']}'s Account were created on {self.createdOnHook}")
        elif not self.started:
            print('>>> Initialize the hook before executing this command')

    def lastOnline(self):
        if self.success and self.started:
            print(f"{self.user_infos['name']}'s Account were last seen online on {self.lastOnlineHook}")
        elif not self.started:
            print('>>> Initialize the hook before executing this command')

    def getHookMessage(self):
        if self.started:
            print('Hook started')
        if self.success:
            print('Hook got success')
        else:
            print('Hook did not got success')
