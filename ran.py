import os
import platform

os.system('git pull --quiet 2>/dev/null')
os.system("clear")

print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/F3IhtLI7duf4pMkhhXJSfd?mode=hq2tcla')

tokyo = platform.architecture()[0]

if tokyo in ["64bit"]:
    os.system('clear')
    try:
        __import__("gen")
    except ImportError:
        print('\033[91;1m [•] Module gen not found')
else:
    print('\033[91;1m [•] Unsupported device')