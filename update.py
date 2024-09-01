

import requests, zipfile, io, time,os

def updat_addonse():
    print("LEFT 4 DEAD UPDATER @ACZONTONGAO")
    print("ALL CODES IN THIS SCRIPT IS UNDER LICENSE OF MIT LICENSE @ACZONTONGAO")
    print("USING FOR EDUCATIONAL PURPOSES ONLY UNDER PRIVATE USE \n")
    print("UPDATING ADDONS MODS \n")
    get_file = 'https://raw.githubusercontent.com/ragej4x/text-db/main/downloader-db.txt'
    print(f"Requesting form Database : {get_file} \n")
    get = requests.get(get_file)

    url = []
    url.append(get.text)
    convert = str(url)
    clean = convert.replace("'", "").replace(",", "").replace("\\n", "").replace("[", "").replace("]", "")

    print(f'Downloading from: {clean} \n')
    try:
        file = requests.get(clean)
        print(f"Response status code: {file.status_code}")
        print(f"Content Size: {len(file.content)} \n")
        extract = zipfile.ZipFile(io.BytesIO(file.content))
        print("Extracting file \n")
        extract.extractall('game/left4dead2/addons')
        
        print("Installation Successfull\n \n ")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(3)


def update_game():
    print("UPDATING GAMEFILES")
    get_file = 'https://raw.githubusercontent.com/ragej4x/text-db/main/game-update-db.txt'
    print(f"Requesting form Database : {get_file} \n")
    get = requests.get(get_file)

    url = []
    url.append(get.text)
    convert = str(url)
    clean = convert.replace("'", "").replace(",", "").replace("\\n", "").replace("[", "").replace("]", "")

    print(f'Downloading from: {clean} \n')
    try:
        file = requests.get(clean)
        print(f"Response status code: {file.status_code}")
        print(f"Content Size: {len(file.content)} \n")
        extract = zipfile.ZipFile(io.BytesIO(file.content))
        print("Extracting file \n")
        extract.extractall('')
        
        print("Installation Successfull\n \n ")
    except Exception as e:
        print(f"Error: {e}")

    print("Closing in 5 seconds")
    time.sleep(5)
    os.startfile('Launcher.exe')

    exit()



def run():
    try:
        requests.get("http://www.google.com/", timeout=5)
        return 1
    except requests.ConnectionError:
        return 0
    

if run():
    updat_addonse()
    update_game()
else:
    print("Connection error please check your internet connection")
    print("If the error still persist contact me on Facebook or Emai")
    print("Facebook : Jimboy Aczon")
    print("Email : aczontongao@gmail.com")
