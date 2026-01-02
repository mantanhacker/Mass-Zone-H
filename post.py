import requests
import sys
import time
from colorama import Fore, init

init()
red = Fore.RED
reset = Fore.RESET
green = Fore.GREEN

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

sess = requests.Session()

def zone_h(defacer, url, team=None):
    payload = {
        'defacer': defacer,
        'domain1': url,
        'hackmode': '1',
        'reason': '1'
    }

    if team:
        payload['team'] = team

    try:
        sess.get('http://www.zone-h.org/notify/single', headers=headers, timeout=10)
        response = sess.post('http://www.zone-h.org/notify/single', data=payload, headers=headers, timeout=10)
        if 'OK' in response.text:
            print(f'[ZONE-H] {url} => {green}Success{reset}')
        else:
            print(f'[ZONE-H] {url} => {red}Failed{reset}')
    except requests.exceptions.Timeout:
        print(f'[ZONE-H] {url} => {red}Timeout{reset}')
    except requests.exceptions.RequestException as e:
        print(f'[ZONE-H] {url} => {red}Error: {str(e)}{reset}')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(f"Usage : python3 {sys.argv[0]} your_nickname your_team list.txt\nNote : write None if there is no team")
        sys.exit()

    defacer = sys.argv[1]
    team_input = sys.argv[2]
    domain_file = sys.argv[3]

    team = team_input if team_input.lower() != "none" else None

    try:
        with open(domain_file, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: File Not Found.")
        sys.exit(1)

    print(f"Total URLs to process: {len(urls)}")

    try:
        for i, url in enumerate(urls, start=1):
            print(f"[{i}/{len(urls)}] Processing: {url}")
            zone_h(defacer, url, team)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user.")
        sys.exit(0)

    print("\nHello Hacker!.\nCoded by L4663r666h05t")
