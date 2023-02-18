from UserHook import UserHook

users = [1, 123, 1337, 69, 420]

# easiest way to do it lol
for i in users:
  account = UserHook(i)
  account.start()
  account.get()
  account.createdOn()
  account.lastOnline()

  
