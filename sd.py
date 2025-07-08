import threading
from queue import Queue
import requests
import random
import string
import json
import hashlib
from faker import Faker
import time

print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
> › Tool     :- Facebook Auto Creator     
> › Email    :- @mail.gw domain used ✅
> › Author   :- AJMAL x GPT
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
print('\x1b[38;5;208m⇼'*60)

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_mail_account(proxy=None):
    fake = Faker("en_US")
    username = generate_random_string(10)
    password = fake.password()
    email = f"{username}@mail.gw"  # 🔥 USING mail.gw domain here
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
    first_name = fake.first_name()
    last_name = fake.last_name()

    # No actual mail creation API call — fake email assumed
    return email, password, first_name, last_name, birthday

def register_facebook_account(email, password, first_name, last_name, birthday, proxy=None):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }

    sig = ''.join(f'{k}={v}' for k, v in sorted(req.items()))
    req['sig'] = hashlib.md5((sig + secret).encode()).hexdigest()

    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBDV/Nexus 7;FBSV/4.1.1;]'
    }

    try:
        res = requests.post('https://b-api.facebook.com/method/user.register', data=req, headers=headers, proxies=proxy)
        data = res.json()

        if 'new_user_id' in data:
            print(f'''
----------- GENERATED ACCOUNT -----------
EMAIL     : {email}
PASSWORD  : {password}
ID        : {data['new_user_id']}
NAME      : {first_name} {last_name}
BIRTHDAY  : {birthday}
GENDER    : {gender}
TOKEN     : {data['session_info']['access_token']}
----------- ACCOUNT SAVED -----------
''')
            with open("/sdcard/Download/username.txt", "a") as f:
                f.write(f"{email} | {password} | {first_name} {last_name} | {data['new_user_id']}\n")
        else:
            print(f"[×] FB Error: {data.get('error_msg', 'Unknown')}")

    except Exception as e:
        print(f"[×] Facebook API Error: {e}")

def load_proxies():
    try:
        with open("proxies.txt") as f:
            proxies = [line.strip() for line in f if line.strip()]
        return [{'http': f'http://{p}'} for p in proxies]
    except:
        return []

def test_proxy(proxy):
    try:
        r = requests.get("https://api.mail.gw", proxies=proxy, timeout=5)
        return r.status_code == 200
    except:
        return False

def get_working_proxies():
    raw = load_proxies()
    valid = []
    q = Queue()

    def worker():
        while True:
            proxy = q.get()
            if test_proxy(proxy):
                print(f"Pass: {proxy}")
                valid.append(proxy)
            else:
                print(f"Fail: {proxy}")
            q.task_done()

    for proxy in raw:
        q.put(proxy)

    for _ in range(10):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    q.join()
    return valid

# MAIN RUN
working_proxies = get_working_proxies()
if not working_proxies:
    print("[×] No valid proxies found.")
else:
    try:
        count = int(input("[+] How Many Accounts You Want: "))
    except:
        count = 1

    for _ in range(count):
        proxy = random.choice(working_proxies)
        email, pw, fn, ln, bday = create_mail_account(proxy)
        if all([email, pw, fn, ln, bday]):
            register_facebook_account(email, pw, fn, ln, bday, proxy)
        time.sleep(15)  # ✅ delay added
