# BY FLOWKIRA pls dont copy
# use a vpn for security (optional)
import requests
import time
import random
import string
from rich import print

def logo():
    print("""[purple]
    """)
code_NitroFormat = string.ascii_letters + string.digits

while True:
    volume = random.choice([16, 24])
    code_NitroGenerate = "".join(random.choice(code_NitroFormat) for _ in range(volume))
    url_api = f'https://discord.com/api/v9/entitlements/gift-codes/{code_NitroGenerate}?with_application=false&with_subscription_plan=true'
    r = requests.get(url_api, timeout=3)
    print(r.status_code)
    if r.status_code == 200:
        print(f"CODE VALID [{code_NitroGenerate}]")
        break
    if r.status_code == 429:
        print("Discord block the script")
        time.sleep(620)
    if r.status_code == 404:
        print("no exist")