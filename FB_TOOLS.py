import os,time
print('give star to our repo')
os.system('git pull && clear')
os.system('xdg-open https://github.com/Ahmed-XD/FB_TOOLS')
time.sleep(1)
print('Join Our Facebook Group and support us')
os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
os.system('clear')
print('-'*54)
users_choice = input("FB_TOOLS MADE BY AHMED ALI\n[1] CHECK CLONED ACCOUNTS LIVE OR DEAD\n[2] CHECk CLONED ACCOUNTS TOTAL FRIEND\n\nChoose : ")
if users_choice == "1":
  os.system("clear")
  os.system("chmod +x ID_CHK")
  os.system("./ID_CHK")
elif users_choice == "2":
  os.system("clear")
  os.system("chmod +x FRIEND_CHECKER")
  os.system("./FRIEND_CHECKER")
else:
  exit("Choose the right option")
