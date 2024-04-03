import subprocess
import os
hinweis = '1 = KomplettReboot in Sec, 2 = Herunterfahren abbrechen, 3 = Herunterfahren in Sec, 4 = Sofortiger Neustart in die Firmware'
sd = 'shutdown '
eingabe = 99

with open('uacpromt.bat', 'r') as uac:
    uacrun = uac.read()
    uacrun += '\nshutdown -r -fw'

while eingabe != 0:

    try:
        print(hinweis)
        eingabe = int(input("Bitte Wählen: "))
    except ValueError:
        print("Eingabe fehlerhaft. Nochmal eingeben!")
        continue

    if eingabe == 1:
        timer = int(input("Eingabe der Zeit: "))
        subprocess.call(f'{sd}-g -t {timer}')
        print('Das System schaltet sich in {timer}s ab.')
        print('test1')

    elif eingabe == 2:
        try:
            subprocess.call(f'{sd}-a')
        except subprocess.CalledProcessError:
            print('Fehler oder bereits abgebrochen!')

    elif eingabe == 3:
        try:
            timer = int(input("Eingabe der Zeit: "))
            subprocess.call(f'{sd}-s -t {timer}')
        except subprocess.CalledProcessError:
            print('Fehler!')



    elif eingabe == 4:
        p = subprocess.Popen(["uacpromt.bat", pause], cwd=r"./")
        stdout, stderr = p.communicate()
        p.wait()

    else:
        print('END OR ERROR')
        eingabe = 0
