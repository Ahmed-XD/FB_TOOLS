import os,time
print('give star to our repo')
os.system('git pull && clear')
os.system('xdg-open https://github.com/Ahmed-XD/FB_TOOLS')
time.sleep(1)
print('Join Our Facebook Group and support us')
os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
os.system('clear')
print('-'*54)
users_choice = input("\033[1;33mFB_TOOLS MADE BY AHMED ALI\n[1] CHECK CLONED ACCOUNTS LIVE OR DEAD\n[2] CHECk CLONED ACCOUNTS TOTAL FRIEND\n[3] GET 2F CODE [KEY]\n[4] GET GROUP INFO [MEMBER|GROUP TYPE]\n[5] AUTO 2F \n\nChoose : ")
if users_choice == "1":
  os.system("clear")
  os.system("chmod +x ID_CHK")
  os.system("./ID_CHK")
elif users_choice == "2":
  os.system("clear")
  os.system("python FRIEND*")
elif users_choice == "3":
  os.system("python 2F*")
elif users_choice == "4":
  os.system("clear && python GROUP_FINDER.py")
elif users_choice == "5":
  os.system("clear && 2F_AUTO*")
else:
  exit("Choose the right option")
