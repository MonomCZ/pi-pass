import subprocess

def start_hotspot():
    interface = 'wlan0'
    hotspot_name = 'MyHotspot'
    #deletes the previous hotspot if it exists
    subprocess.run(['sudo','nmcli', 'connection', 'delete', hotspot_name], stderr=subprocess.DEVNULL)
    #creates a new one
    subprocess.run(['sudo','nmcli', 'connection', 'add', 'type', 'wifi', 'ifname', interface, 'con-name', hotspot_name,'ssid', hotspot_name], check=True)
    #sets the ip (so it doesnt change so the captive portal thing doesnt break)
    subprocess.run(['sudo','nmcli', 'connection', 'modify', hotspot_name,'ipv4.addresses', '10.42.0.1/24'], check=True)
    subprocess.run(['sudo','nmcli', 'connection', 'modify', hotspot_name,'ipv4.gateway', '10.42.0.1','ipv4.dns', '10.42.0.1','ipv4.method', 'manual', ], check=True)
    #does *something* 
    subprocess.run(['sudo','nmcli', 'connection', 'modify', hotspot_name,'802-11-wireless.mode', 'ap','ipv6.method', 'ignore'], check=True)
    #makes it so the hotspot doesn't automatically start on boot
    subprocess.run(['sudo', 'nmcli', 'connection', 'modify', hotspot_name,'connection.autoconnect', 'no'], check=True)
    #removes the password :3
    #subprocess.run(['sudo','nmcli', 'connection', 'modify', hotspot_name,'remove', '802-11-wireless-security'], check=True)

    #just starts it up
    subprocess.run(['sudo','nmcli', 'connection', 'up', hotspot_name], check=True)


    