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

    def getHookStatus(self):
        count = 0
        # testing
        if self.started: count+=1
        if self.success: count+=1

        return count

    def hookWorking(self):
        return self.getHookStatus() == 2
        
    def showInfos(self):
        if self.hookWorking():
            print(f"{self.user_infos['name']}'s Infos:\n- Display Name: {self.user_infos['displayName']}\n- Last Online: {self.lastOnlineHook}\n- Created: {self.createdOnHook}\n- ID: {self.accountId}")

    def createdOn(self):
        if self.hookWorking():
            print(f"{self.user_infos['name']}'s Account were created on {self.createdOnHook}")

    def lastOnline(self):
        if self.hookWorking():
            print(f"{self.user_infos['name']}'s Account were last seen online on {self.lastOnlineHook}")

    # aliases
    def startHook(self): self.hookStart()
    def start(self): self.hookStart()
    def hook(self): self.hookStart()
    def fetchId(self): self.showInfos()
    def fetch(self): self.showInfos()
    def get(self): self.showInfos()
    def lastSeen(self): self.lastOnline()


#bruh = UserHook(1)
#bruh.hookStart()
#bruh.showInfos()
