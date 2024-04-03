import subprocess
import os
import tempfile
from rich.console import Console
from rich.table import Table
import tkinter as tk

console = Console()
console.print('Hallo Kunde:thumbs_up:')

hinweis = ['1. Reboot in Sec', '2. Herunterfahren abbrechen', '3. Herunterfahren in Sec', '4. Sofortiger Reboot ins BIOS']
table = Table(title="Hinweise")
table.add_column('Nr', style='blue')
table.add_column('Aufgaben', style='bold blue')
table.add_row('1', 'Reboot in Sec')
table.add_row('2', 'Herunterfahren abbrechen')
table.add_row('3', 'Herunterfahren in Sec')
table.add_row('4', 'Sofortiger Reboot ins BIOS')

eingabe = 99

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

while eingabe != 0:

    try:
        console.print(table)
        eingabe = int(input("Bitte Wählen: "))
    except ValueError:
        print("Eingabe fehlerhaft. Nochmal eingeben!")
        continue

    if eingabe == 1:
        timer = int(input("Eingabe der Zeit: "))
        subprocess.call(f'shutdown -g -t {timer}')
        print('Das System schaltet sich in {timer}s ab.')
        print('test1')

    elif eingabe == 2:
        try:
            subprocess.call(f'shutdown -a')
        except subprocess.CalledProcessError:
            print('Fehler oder bereits abgebrochen!')

    elif eingabe == 3:
        try:
            timer = int(input("Eingabe der Zeit: "))
            subprocess.call(f'shutdown -s -t {timer}')
        except subprocess.CalledProcessError:
            print('Fehler!')

    elif eingabe == 4:

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.bat') as temp_file:
            for line in batch_script_lines:
                temp_file.write(line + '\n')
                temp_file.flush()
        try:
            subprocess.run(temp_file.name, shell=True)
        except:
            print('Fehler: BIOS Reboot!')
        finally:
            break

    else:
        print('END OR ERROR')
        eingabe = 0
