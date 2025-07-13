import requests
import random
import string
import hashlib
from faker import Faker
import time

ANSI Colors

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[38;5;196m"
ORANGE = "\033[38;5;208m"
YELLOW = "\033[38;5;226m"
GREEN = "\033[38;5;82m"
CYAN = "\033[38;5;51m"
BLUE = "\033[38;5;27m"
MAGENTA = "\033[38;5;201m"
WHITE = "\033[38;5;15m"
PINK = "\033[38;5;213m"
GREY = "\033[38;5;245m"

Super Stylish Header

print(f"""{BOLD}{CYAN}
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃{PINK}   ╔═╗┌─┐┬ ┬┌─┐┬ ┬┌┬┐┌─┐┬ ┬┬┌─┐   {CYAN}FACEBOOK AUTO CREATOR  {MAGENTA}V2.0   {CYAN}┃
┃{RED}   ╚═╗│ ││ │├─┘│ │ │ ├─┤├┤ ├┴─┤   {YELLOW}Author: {WHITE}Shahzada Ajmal      {CYAN}┃
┃{ORANGE}   ╚═╝└─┘└─┘┴  └─┘ ┴ ┴ ┴└─┘┴ ┴┴┴ ┴   {GREEN}WhatsApp: {WHITE}+923218745502 {CYAN}┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
{RESET}""")
print(f"{BOLD}{MAGENTA}{'⇼'*60}{RESET}")

def generate_random_string(length):
return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_fake_phone():
return "+1" + random.choice("23456789") + ''.join(random.choices(string.digits, k=9))

def create_fake_profile(user_password):
fake = Faker()
phone = generate_fake_phone()
password = user_password
birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
first_name = fake.first_name()
last_name = fake.last_name()
return phone, password, first_name, last_name, birthday

def register_facebook_account(phone, password, first_name, last_name, birthday):
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
    'phone': phone,  
    'locale': 'en_US',  
    'method': 'user.register',  
    'password': password,  
    'reg_instance': generate_random_string(32),  
    'return_multiple_errors': True  
}  

sig = ''.join(f'{k}={v}' for k, v in sorted(req.items()))  
req['sig'] = hashlib.md5((sig + secret).encode()).hexdigest()  

headers = {  
    'User-Agent': random.choice([  
        '[FBAN/FB4A;FBAV/300.0.0.20.123;FBDM/{density=2.0,width=720,height=1280};FBLC=en_US;FBDV=Pixel;FBSV=9;]',  
        '[FBAN/FB4A;FBAV/420.0.0.35.99;FBDM={density=3.0,width=1080,height=1920};FBLC=en_GB;FBDV=Samsung;FBSV=10;]',  
        '[FBAN/FB4A;FBAV/360.0.0.15.120;FBDM={density=2.75,width=1080,height=2160};FBLC=en_CA;FBDV=MotoG;FBSV=8.1;]',  
        '[FBAN/FB4A;FBAV/250.0.0.18.119;FBDM={density=2.0,width=720,height=1280};FBLC=en_US;FBDV=Nexus;FBSV=6;]'  
    ])  
}  

try:  
    res = requests.post('https://b-api.facebook.com/method/user.register', data=req, headers=headers, timeout=25)  
    data = res.json()  

    if 'new_user_id' in data:  
        print(f"""

{BOLD}{GREEN}━━━━━━━━━━━━━━━  ACCOUNT CREATED SUCCESSFULLY  ━━━━━━━━━━━━━━━{RESET}
{BOLD}{CYAN}PHONE     : {YELLOW}{phone}{RESET}
{BOLD}{CYAN}PASSWORD  : {RED}{password}{RESET}
{BOLD}{CYAN}ID (UID)  : {MAGENTA}{data['new_user_id']}{RESET}
{BOLD}{CYAN}NAME      : {PINK}{first_name} {last_name}{RESET}
{BOLD}{CYAN}BIRTHDAY  : {BLUE}{birthday}{RESET}
{BOLD}{CYAN}GENDER    : {ORANGE}{gender}{RESET}
{BOLD}{CYAN}TOKEN     : {GREEN}{data['session_info']['access_token']}{RESET}
{BOLD}{GREEN}━━━━━━━━━━━━━━━  ACCOUNT SAVED  ━━━━━━━━━━━━━━━{RESET}
""")
with open("/sdcard/Download/username.txt", "a") as f:
f.write(f"{phone} | {password} | {first_name} {last_name} | {data['new_user_id']}\n")
return True
elif 'error_msg' in data and 'verify' in data['error_msg'].lower():
print(f"{BOLD}{ORANGE}[!] Manual Verify Required: {YELLOW}{phone}{RESET} — Login & Add Your Number")
else:
print(f"{BOLD}{RED}[×] FB Error: {data.get('error_msg', 'Unknown')}{RESET}")
return False

except Exception as e:  
    print(f"{BOLD}{RED}[×] Facebook API Error: {e}{RESET}")  
    return False

Main Execution

try:
count = int(input(f"{BOLD}{CYAN}[+] How Many Accounts You Want: {RESET}"))
except:
count = 1

user_password = input(f"{BOLD}{CYAN}[+] Enter Password For All Accounts: {RESET}")

for i in range(count):
success = False
for attempt in range(3):  # Retry up to 3 times per account
print(f"\n{BOLD}{GREY}[•] Creating account {i+1} (Attempt {attempt+1}){RESET}")
phone, pw, fn, ln, bday = create_fake_profile(user_password)
success = register_facebook_account(phone, pw, fn, ln, bday)
if success:
break
time.sleep(5)  # short delay between retries
time.sleep(20)  # delay between each account
