import requests, zipfile, io, time, os
from tqdm import tqdm

import speedtest

def run_update():
    
    """  
    net_speed = speedtest.Speedtest()
    net_speed.get_best_server()
    download_speed = net_speed.download() / 1000000
    print(f"CHECKING DOWNLOAD SPEED {download_speed}")
"""
    print("UPDATING GAMEFILES")
    get_file = 'https://raw.githubusercontent.com/ragej4x/text-db/main/game-update-db.txt'
    print(f"Requesting form Database : {get_file} \n")
    get = requests.get(get_file)

    url = []
    url.append(get.text)
    convert = str(url)
    clean = convert.replace("'", "").replace(",", "").replace("\\n", "").replace("[", "").replace("]", "")

    try:
        file = requests.get(clean)
        extract = zipfile.ZipFile(io.BytesIO(file.content))
        for i in tqdm(range(100), desc=f"Download Size : {len(file.content)} Bytes"):

            #time.sleep(len(file.content) // len(file.content) - download_speed // 70)
            
            extract.extractall('')  

    except Exception as e:
        print(f"Error: {e}")
        
        print("Installation not Successfull")
           

    print("Installation Successfull")

        #time.sleep(len(get.content) / download_speed)





run_update()






"""def update_game():
    
    get_file = 'https://raw.githubusercontent.com/ragej4x/text-db/main/game-update-db.txt'
    print(f"Requesting form Database : {get_file} \n")
    get = requests.get(get_file)

    url = []
    url.append(get.text)
    convert = str(url)
    clean = convert.replace("'", "").replace(",", "").replace("\\n", "").replace("[", "").replace("]", "")

    print(f'Downloading from: {clean} \n')


    print("Closing in 5 seconds")
    time.sleep(5)
    os.startfile('Launcher.exe')

    exit()"""

