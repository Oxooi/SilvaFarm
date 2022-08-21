#Open website
from time import sleep
import webbrowser
import sys
from colorama import Fore
from colorama import Style

#Open website with argument
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(f'[{Fore.YELLOW}*{Fore.WHITE}] {Style.BRIGHT}Let\'s watch {Fore.LIGHTMAGENTA_EX}' + address + f'{Fore.WHITE}! and farm silvas{Style.RESET_ALL}')
    sleep(1)
    webbrowser.open('https://www.twitch.tv/' + address)
    print(f'[{Fore.YELLOW}*{Fore.WHITE}] {Style.BRIGHT}Stream launched..{Style.RESET_ALL}')

else:
    print(f'[{Fore.YELLOW}!{Fore.WHITE}] {Fore.LIGHTRED_EX}No argument given{Fore.WHITE}')
    print(f'[{Fore.YELLOW}!{Fore.WHITE}] {Fore.LIGHTRED_EX}Usage: python3 silva.py <streamer>{Fore.WHITE}')
    print(f'[{Fore.YELLOW}!{Fore.WHITE}] {Fore.LIGHTRED_EX}Example: python3 silva.py silvacraft{Fore.WHITE}')