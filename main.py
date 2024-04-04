import subprocess
import os
import tempfile
from rich.console import Console
from rich.table import Table
from time import sleep
from art import *
console = Console()

table = Table(title="Hinweise")
table.add_column('Nr', style='blue')
table.add_column('Aufgaben', style='bold blue')
table.add_row('0', 'Tool schließen')
table.add_row('1', 'Reboot in Sec')
table.add_row('2', 'Herunterfahren abbrechen')
table.add_row('3', 'Herunterfahren in Sec')
table.add_row('4', 'Sofortiger Reboot ins BIOS')

batch_script_lines = [
    '@echo off',
    'if "%2" == "firstrun" exit',
    'cmd /c "%0" null firstrun',
    'if "%1" == "skipuac" goto skipuacstart',
    ':checkPrivileges',
    'NET FILE 1>NUL 2>NUL',
    'if "%errorlevel%" == "0" ( goto gotPrivileges ) else ( goto getPrivileges )',
    ':getPrivileges',
    'if "%1" == "ELEV" (shift & goto gotPrivileges)',
    'setlocal DisableDelayedExpansion',
    'set "batchPath=%~0"',
    'setlocal EnableDelayedExpansion',
    'ECHO Set UAC = CreateObject^("Shell.Application"^) > "%temp%\\OEgetPrivileges.vbs"',
    'ECHO UAC.ShellExecute "!batchPath!", "ELEV", "", "runas", 1 >> "%temp%\\OEgetPrivileges.vbs"',
    '"%temp%\\OEgetPrivileges.vbs"',
    'exit /B',
    ':gotPrivileges',
    'setlocal & pushd .',
    'cd /d %~dp0',
    'cmd /c "%0" skipuac firstrun',
    'cd /d %~dp0',
    ':skipuacstart',
    'if "%2" == "firstrun" exit',
    'shutdown -r -fw',
    'pause'
]

eingabe = 99

while True:
    os.system('cls')
    hallo = text2art('Easy Start Up Menu')
    print(hallo)

    try:
        console.print(table)
        eingabe = int(input("Bitte Wählen: "))
    except ValueError:
        console.print("Eingabe fehlerhaft. Nochmals als Int. eingeben!", style='red bold underline')
        continue
    except:
        console.print('Unbekannter Fehler in Eingabe', style='red bold underline')

    if eingabe == 1:
        try:
            timer = int(input("Eingabe der Zeit: "))
            subprocess.call(f'shutdown -g -t {timer}')
            console.print(f'Das System schaltet sich in {timer} Sekunden ab.', style='green')
            sleep(3)
            continue
        except ValueError:
            console.print('Ungültiger Eingabewert in Option 1', style='red bold underline')
            sleep(3)
        except:
            console.print('Unbekannter Fehler in Option 1', style='red bold underline')
            sleep(3)
            continue

    elif eingabe == 2:
        try:
            subprocess.call(f'shutdown -a')
            sleep(3)
            continue
        except subprocess.CalledProcessError:
            console.print('Fehler oder bereits abgebrochen!', style='red bold underline')
            sleep(3)
            continue
        except:
            console.print("Fehler", style='red bold underline')
            sleep(3)
            continue

    elif eingabe == 3:
        try:
            timer = int(input("Eingabe der Zeit: "))
            subprocess.call(f'shutdown -s -t {timer}')
            sleep(3)
            continue
        except subprocess.CalledProcessError:
            console.print('Subprozess Fehler', style='red bold underline')
            sleep(3)
            continue

    elif eingabe == 4:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.bat') as temp_file:
            for line in batch_script_lines:
                temp_file.write(line + '\n')
                temp_file.flush()
                continue
        try:
            subprocess.run(temp_file.name, shell=True)
            sleep(3)
            continue
        except:
            console.print('Fehler: BIOS Reboot!', style='red bold underline')
            sleep(3)
            continue

    elif eingabe == 0:
        console.print('Danke für Ihre Nutzung meines EasyStartUp Tools.', style='green bold underline')
        sleep(3)
        break

    else:
        console.print('END OR ERROR', style='red bold underline')

