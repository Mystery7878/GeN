import os, platform

os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/F3IhtLI7duf4pMkhhXJSfd?mode=hq2tcla')

try:
    import gen
except ImportError:
    print("\033[91;1m[•] gen module not found")