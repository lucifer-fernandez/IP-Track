import requests
import os
import time
import sys    

os.system("pip install requests")
os.system("clear")
time.sleep(2)
print("""\033[1;32m


_________ _______     _________ _______  _______  _______  _       
\\__   __/(  ____ )    \\__   __/(  ____ )(  ___  )(  ____ \\| \\    /\\
   ) (   | (    )|       ) (   | (    )|| (   ) || (    \\/|  \\  / /
   | |   | (____)| _____ | |   | (____)|| (___) || |      |  (_/ / 
   | |   |  _____)(_____)| |   |     __)|  ___  || |      |   _ (  
   | |   | (             | |   | (\\ (   | (   ) || |      |  ( \\ \\ 
___) (___| )             | |   | ) \\ \\__| )   ( || (____/\\|  /  \\ \\
\\_______/|/              )_(   |/   \\__/|/     \\|(_______/|_/    \\/
                                                                                                         
\033[1;31m=======================================================================
    \033[1;34mTools Author: \033[1;33mMohammad Rayhan Khan 
    \033[1;34mVersion     : \033[1;33m1.0
    \033[1;34mTool Name   : \033[1;33mIP Location Tracker
    \033[1;34mFacebook    : \033[1;33mhttps://www.facebook.com/azad.farabi.2024
    \033[1;34mGithub      : \033[1;33mhttps://github.com/lucifer-fernandez/IP_to_Location.git
\033[1;31m=======================================================================
""")







ip = input("\033[1;36mEnter your target IP:\033[1;33m ")

response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()

def type():
    a = "\n\t\t\033[1;36m☯️ Fetching your IP info... \n"
    for i in a:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.09)



if data['status'] == 'success':
    os.system("clear")
    type()
    time.sleep(3)
    os.system("clear")
    print("\n\t\t\033[1;32m📍 IP Location Info:\n")
    print("\033[1;35m_"*60)
    print(f"\n\033[1;36m✅ Country     : \033[1;33m{data['country']}")
    print(f"\033[1;36m✅ CountryCode : \033[1;33m{data['countryCode']}")
    print(f"\033[1;36m✅ Region      : \033[1;33m{data['region']}")
    print(f"\033[1;36m✅ RegionName  : \033[1;33m{data['regionName']}")
    print(f"\033[1;36m✅ City        : \033[1;33m{data['city']}")
    print(f"\033[1;36m✅ ZIP         : \033[1;33m{data['zip']}")
    print(f"\033[1;36m✅ Latitude    : \033[1;33m{data['lat']}")
    print(f"\033[1;36m✅ Longitude   : \033[1;33m{data['lon']}")
    print(f"\033[1;36m✅ Timezone    : \033[1;33m{data['timezone']}")
    print(f"\033[1;36m✅ ISP         : \033[1;33m{data['isp']}")
    print(f"\033[1;36m✅ Org         : \033[1;33m{data['org']}")
    print(f"\033[1;36m✅ AS Info     : \033[1;33m{data['as']}")
    print(f"\033[1;36m✅ IP Address  : \033[1;31m{data['query']}\033[0m\n")
    print("\033[1;35m—"*60)

   
    maps_link = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
    print(f"\n\n\033[1;36m📌 Live Location Link: \033[1;32m {maps_link}\033[1;0m")
    print("\n\033[1;33mCopy this link, then paste into the Google Maps and search. You'll see the live location in Google Maps.\033[0m\n\n\n")

else:
    time.sleep(1)
    print("\033[1;31m❌ Failed to fetch IP details. Check the IP address and try again.\033[1;0m")
