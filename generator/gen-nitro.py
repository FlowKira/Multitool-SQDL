# BY FLOWKIRA pls dont copy
# use a vpn for security (optional)
import requests
import time
import random
import string
from rich import print

def Logo():
    print("""[purple]
        ▄▄▄▄████████▄▄▄▄
      ▄████████████████████▄
    ▄████████  ████  ████████▄
   ██████████  ▀▀▀▀  ██████████
   ██████████𓁹SQDL𓁹 ██████████
    ▀████████████████████████▀
      ▀▀████████████████▀▀
          ░░░░  ░░░░  ░░

    [/purple]""")
Logo()
time.sleep(2)
code_NitroFormat = string.ascii_letters + string.digits
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Edg/122.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Edg/121.0.0.0",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Edg/122.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.3; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/122.0.6261.89 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/121.0.6167.138 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/123.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OnePlus 10 Pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2529) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Linux; Android 13; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Chromebook; Android 11; BRAVIA 4K VH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Tizen 7.0; TV) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.205 Safari/537.36"]
while True:
    volume = random.choice([16, 24])
    random_agent = random.choice(USER_AGENT)
    code_NitroGenerate = "".join(random.choice(code_NitroFormat) for _ in range(volume))
    url_api = f'https://discord.com/api/v9/entitlements/gift-codes/{code_NitroGenerate}?with_application=false&with_subscription_plan=true'
    headers = {
        "User-Agent": random_agent,
        "Accept": "application/json"
    }
    r = requests.get(url_api, timeout=3, headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        print(f"[green]CODE VALID [{code_NitroGenerate}][/green]")
        break
    if r.status_code == 429:
        print("[pink]Discord block the script wait 10minutes[/pink]")
        time.sleep(620)
    if r.status_code == 404:
        print("[red]no exist[/red]")