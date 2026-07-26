import subprocess

def start_hotspot():
    interface = 'wlan0'
    hotspot_name = 'MyHotspot'

    subprocess.run([
        'sudo', 'nmcli', 'connection', 'add',
        'type', 'wifi',
        'ifname', interface, 'con-name', hotspot_name,
        'ssid', hotspot_name
    ])

    subprocess.run([
        'sudo', 'nmcli', 'connection', 'modify', hotspot_name,
        '802-11-wireless.mode', 'ap',
        '802-11-wireless.band', 'bg',
        '802-11-wireless-security.key-mgmt', ''
    ])

    subprocess.run(['sudo', 'nmcli', 'connection', 'up', hotspot_name])