import os
import random
import subprocess
import uuid
import shutil
import winreg
import time
import string



os.system("Taskkill /im gfclient.exe /f /t")
os.system("Taskkill /im gfService.exe /f /t")

def generate_hex(length):
    return ''.join(random.choice('abcdef' + string.digits) for _ in range(length))

def generate_hex2(length):
    return ''.join(random.choice('ABCDEF' + string.digits) for _ in range(length))



registry1 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography"
registry2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SQMClient"
registry3 = r"HKEY_CURRENT_USER\SOFTWARE\Gameforge4d\GameforgeClient\MainApp"
value_name = "MachineGuid"
value_name2 = "MachineId"
value_name3 = "InstallationId"
value_name4= "MachineId"


random_string = (
    generate_hex(8) + '-' +
    '-'.join(generate_hex(4) for _ in range(3)) + '-' +
    generate_hex(12)
)

random_string2 = (
    '{' + generate_hex2(8) + '-' +
    '-'.join(generate_hex2(4) for _ in range(3)) + '-' +
    generate_hex2(12) + '}'
)

print(f"Changing MachineGuid in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography hex to {random_string}")
time.sleep(0.1)
print(f"Changing MachineId in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SQMClient hex to {random_string2}")
time.sleep(0.1)
print(f"Deleting InstallationId in HKEY_CURRENT_USER\SOFTWARE\Gameforge4d\GameforgeClient\MainApp hex to {random_string2}")
time.sleep(0.1)
print(f"Changing MachineId in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography hex to {random_string2}")
time.sleep(0.1)


def changinguuidandguid():
    operation_completed=True
    key1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_SET_VALUE)
    try:
        winreg.SetValueEx(key1, value_name, 0, winreg.REG_SZ, random_string)

    except Exception as e:
        print(f"Error updating registry1:{e}")
        operation_completed=False
    finally:       
        winreg.CloseKey(key1)

    key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\SQMClient", 0, winreg.KEY_SET_VALUE)
    try:
        winreg.SetValueEx(key2, value_name2, 0, winreg.REG_SZ, random_string2)
    except Exception as e:
        print(f"Error updating registry2:{e}")
        operation_completed=False
    finally:
        winreg.CloseKey(key2)

    key4 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_SET_VALUE)
    try:
        winreg.SetValueEx(key4, value_name4, 0, winreg.REG_SZ, random_string2)
    except Exception as e:
        print(f"Error updating registry4:{e}")
        operation_completed=False
    finally:
        winreg.CloseKey(key4)

    time.sleep(1)
    if operation_completed:
        print("Operation completed for all registries ")

operation_completed=True
def delete_registry_value(key_path, value_name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, value_name)
        print(f"Registry value '{value_name}' deleted successfully.")

    except FileNotFoundError:
        print(f"Registry of {value_name} not found")      

    finally:
        try:
            winreg.CloseKey(key)
        except UnboundLocalError:
            pass

    if operation_completed:
        print("Registry has been deleted")


registry_key_path = r"SOFTWARE\Gameforge4d\GameforgeClient\MainApp"
registry_value_name = "InstallationId"

directories=[r'C:\Windows\Prefetch',
             r"C:\Windows\Temp",
             r"C:\Windows\TEMP",
             r"C:\Windows\Prefetch",]


def hexgenerator(length):
    combination = 'ABCDEF123456789'
    hexidecimal = ''.join(random.choice(combination) for _ in range(length))
    return hexidecimal

def generate_random_mac(length):
    combination = 'ABCDEF123456789'
    mac_address = ''.join(random.choice(combination) for _ in range(length)) 
    
    return mac_address

def DeleteGameforge(path1,path2):
    for path in (path1,path2):
        try:
            shutil.rmtree(path)
            print(f"Path {path} removed from directory")

        except FileNotFoundError:
            print(f"Path {path} does not exist or it is deleted completely")

directory = r'C:\Windows\Temp\Gameforge4d'
directory2 = r'C:\Users\Administrator\AppData\Local\Gameforge4d'






while True:
    part1 = hexgenerator(4)
    part2 = hexgenerator(4)

    hexadecimalgen = part1 + "-" + part2

    num_alphabets_part1 = sum(1 for char in part1 if char.isalpha())
    num_numbers_part1 = sum(1 for char in part1 if char.isdigit())
    num_alphabets_part2 = sum(1 for char in part2 if char.isalpha())
    num_numbers_part2 = sum(1 for char in part2 if char.isdigit())

    if num_alphabets_part1 == 4 or num_numbers_part1 == 4 or (num_numbers_part1 == 3 and num_alphabets_part1 == 1):
        part1 = hexgenerator(4)
    elif num_alphabets_part2 == 4 or num_numbers_part2 == 4 or (num_numbers_part2 == 3 and num_alphabets_part2 == 1):
        part2 = hexgenerator(4)
    else:
        break

RandomMacAddressgen = generate_random_mac(2)+"-"+generate_random_mac(2)+"-"+generate_random_mac(2)+"-"+generate_random_mac(2)+"-"+generate_random_mac(2)+"-"+generate_random_mac(2)
DeleteGameforge(directory,directory2)
changinguuidandguid()
delete_registry_value(registry_key_path, registry_value_name)
os.chdir(r'C:\Volume')
os.system(f'Volumeid.exe C:\ {hexadecimalgen}')
print(f"Your hardware serial number has succesfully changed to {hexadecimalgen}")
command=['PowerShell','-Command','Set-NetAdapter','-Name','"Ethernet 2"','-MacAddress',f'{RandomMacAddressgen}','-Confirm:$false']
subprocess.run(command,shell=True)
print(f"Your mac address succesfully has changed to {RandomMacAddressgen}")
os.system("shutdown /r /t 3")

