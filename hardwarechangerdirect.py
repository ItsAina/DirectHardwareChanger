import os
import random
import subprocess
import uuid
import shutil
import winreg
import time
import string
import time
import threading
import psutil


def generate_hex(length):
    return ''.join(random.choice('abcdef' + string.digits) for _ in range(length))

def generate_hex2(length):
    return ''.join(random.choice('ABCDEF' + string.digits) for _ in range(length))

def generate_hex3(length):
    return ''.join(random.choice('ABCDEF' + string.digits) for _ in range(length))

def generate_hex4(length):
    return ''.join(random.choice('abcdef' + string.digits) for _ in range(length))

def generate_hex5(length):
    return ''.join(random.choice('abcdef' + string.digits) for _ in range(length))

def hardwareids():
    return ('{' + generate_hex5(8) + '-' +'-'.join(generate_hex5(4) for _ in range(3)) + '-' +generate_hex5(12) + '}\n' for _ in range(10))


def KillProcessGameforge():
    os.system("Taskkill /im gfclient.exe /f /t")
    os.system("Taskkill /im gfService.exe /f /t")



registry1 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography"
registry2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SQMClient"
registry3 = r"HKEY_CURRENT_USER\SOFTWARE\Gameforge4d\GameforgeClient\MainApp"
registry4 = r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SystemInformation"
value_name = "MachineGuid"
value_name2 = "MachineId"
value_name3 = "InstallationId"
value_name5 = "ComputerHardwareId"


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

random_string3 = (
    '{' + generate_hex3(8) + '-' +
    '-'.join(generate_hex3(4) for _ in range(3)) + '-' +
    generate_hex3(12) + '}'
)

random_string4 = (
    '{' + generate_hex4(8) + '-' +
    '-'.join(generate_hex4(4) for _ in range(3)) + '-' +
    generate_hex4(12) + '}'
)




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
        winreg.SetValueEx(key4, value_name2, 0, winreg.REG_SZ, random_string3)
    except Exception as e:
        print(f"Error updating registry4:{e}")
        operation_completed=False
    finally:
        winreg.CloseKey(key4)

    key5 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\SystemInformation", 0, winreg.KEY_SET_VALUE)
    try:
        winreg.SetValueEx(key5, value_name5, 0, winreg.REG_SZ, random_string4)
    except Exception as e:
        print(f"Error updating registry5: {e}")
        operation_completed = False
    finally:
        winreg.CloseKey(key5)

    key6 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\SystemInformation", 0, winreg.KEY_SET_VALUE)
    try:
        winreg.SetValueEx(key6, value_name6, 0, winreg.REG_SZ, hardwareids)

    except Exception as e:
        print(f"Error updating registry6: {e}")
        operation_completed = False
    finally:
        winreg.CloseKey(key6)
        operation_completed = True

    if operation_completed:
        print("Operation completed for all registries ")

operation_completed=True
def delete_registry_value():
    key_path = r"SOFTWARE\Gameforge4d\GameforgeClient\MainApp"
    value_name = "InstallationId"
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

def generate_random_mac2(length2):
    combination = 'ABCDEF123456789'
    hexidecimal = ''.join(random.choice(combination) for _ in range(length2))
    return hexidecimal

def generate_random_mac3(length3):
    combination = 'ABCDEF123456789'
    hexidecimal = ''.join(random.choice(combination) for _ in range(length3))
    return hexidecimal

def generate_random_mac4(length4):
    combination = 'ABCDEF123456789'
    hexidecimal = ''.join(random.choice(combination) for _ in range(length4))
    return hexidecimal


def generate_random_mac5(length4):
    combination = 'ABCDEF123456789'
    hexidecimal = ''.join(random.choice(combination) for _ in range(length4))
    return hexidecimal

def DeleteGameforge():
    directory = r'C:\Windows\Temp\Gameforge4d'
    directory2 = r'C:\Users\Administrator\AppData\Local\Gameforge4d'
    directory3 = r'C:\ProgramData\Gameforge4d'
    directory4 = r'C:\ProgramData\Riot Games'
    for path in (directory,directory2,directory3,directory4):
        try:
            shutil.rmtree(path)
            print(f"Path {path} removed from directory")

        except FileNotFoundError:
            print(f"Path {path} does not exist or it is deleted completely")






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
RandomMacAddressgen2 = generate_random_mac2(2)+"-"+generate_random_mac2(2)+"-"+generate_random_mac2(2)+"-"+generate_random_mac2(2)+"-"+generate_random_mac2(2)+"-"+generate_random_mac2(2)
RandomMacAddressgen3 = generate_random_mac3(2)+"-"+generate_random_mac3(2)+"-"+generate_random_mac3(2)+"-"+generate_random_mac3(2)+"-"+generate_random_mac3(2)+"-"+generate_random_mac3(2)
RandomMacAddressgen4 = generate_random_mac4(2)+"-"+generate_random_mac4(2)+"-"+generate_random_mac4(2)+"-"+generate_random_mac4(2)+"-"+generate_random_mac4(2)+"-"+generate_random_mac4(2)
RandomMacAddressgen5 = generate_random_mac5(2)+"-"+generate_random_mac5(2)+"-"+generate_random_mac5(2)+"-"+generate_random_mac5(2)+"-"+generate_random_mac5(2)+"-"+generate_random_mac5(2)

def VolumeChanger():
    os.system(f'Volumeid.exe C:\\ {hexadecimalgen}')

def MacAddressChanger():
    get_active_network_adapters_script = """
    Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -ExpandProperty Name
    """

    active_network_adapters_process = subprocess.run(['powershell', '-Command', get_active_network_adapters_script], capture_output=True, text=True)

    if active_network_adapters_process.returncode == 0 and active_network_adapters_process.stdout.strip():
        active_network_adapters = active_network_adapters_process.stdout.strip().splitlines()
        print("Active network adapters:", active_network_adapters)

        network_adapters_to_change = [
            ("Ethernet", RandomMacAddressgen),
            ("Ethernet 2", RandomMacAddressgen2),
            ("Ethernet 3", RandomMacAddressgen3),
            ("Wi-Fi", RandomMacAddressgen4),
            ("Ethernet 4",RandomMacAddressgen5)
        ]

        for adapter_name, mac_address in network_adapters_to_change:
            if adapter_name in active_network_adapters:
                powershell_script = f"""
                try {{
                    Set-NetAdapter -Name "{adapter_name}" -MacAddress "{mac_address}" -ErrorAction Stop -Confirm:$False
                    Write-Output "MAC address for '{adapter_name}' set successfully"
                }}
                catch {{
                    Write-Output "Error setting MAC address for '{adapter_name}': $_"
                }}
                finally {{
                }}
                """

                process = subprocess.run(['powershell', '-Command', powershell_script], capture_output=True, text=True)

                print(f"Output for '{adapter_name}':", process.stdout.strip())
                print(f"Errors for '{adapter_name}':", process.stderr.strip())

            else:
                print(f"Network adapter '{adapter_name}' is not active. Skipping MAC address change.")

    else:
        print("No active network adapters found. Cannot change MAC addresses.")



def main():
    program_name = 'gfclient.exe'
    if not any(proc.name().lower() == program_name for proc in psutil.process_iter()):
        pass
    else:
        KillProcessGameforge()
        time.sleep(1) 

    thread_2 = threading.Thread(target=DeleteGameforge())
    thread_2.start()
    thread_3 = threading.Thread(target=changinguuidandguid())
    thread_3.start()
    thread_4 = threading.Thread(target=delete_registry_value())
    thread_4.start()
    thread_5 = threading.Thread(target=VolumeChanger())
    thread_5.start()
    thread_6 = threading.Thread(target=MacAddressChanger())
    thread_6.start()
    time.sleep(3)
    os.system("shutdown /r /t 1")
    





if __name__ == "__main__":
    main()

