import subprocess

def start_hotspot():
    interface = 'wlan0'
    hotspot_name = 'MyHotspot'

    subprocess.run([
        'sudo', 'nmcli', 'device', 'wifi', 'hotspot',
        'ifname', interface,
        'ssid', hotspot_name
    ])
