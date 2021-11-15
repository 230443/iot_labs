import requests
import time
import os
import psutil

api_key = "RTYD4EPD074BDJAS"  # Put your API Key here


def send(payload):
    payload['api_key'] = api_key
    r = requests.get("https://api.thingspeak.com/update", params=payload)


def main():
    while True:
        payload = {'field1': get_temp(),
                   'field2': is_domain_active('www.ftims.p.lodz.pl'),
                   'field3': get_cpu_percent(),
                   'field4': get_ram_usage()}
        send(payload)
        time.sleep(5)


def get_temp():
    # Calculate CPU temperature of Raspberry Pi in Degrees C
    # Get Raspberry Pi CPU temp
    return int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3


def is_domain_active(domain):
    ping_exit = os.system("ping -c 1 " + domain)
    f2 = 0
    if ping_exit == 0:
        f2 = 1

    return f2


def get_cpu_percent():
    return psutil.cpu_percent()


def get_ram_usage():
    return psutil.virtual_memory().percent


if __name__ == "__main__":
    while True:
        main()
