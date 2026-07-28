sudo apt update
sudo apt upgrade -y

sudo apt install -y dnsmasq python3-flask iptables network-manager python3-pip python3-pil python3-smbus i2c-tools
pip3 install --break-system-packages adafruit-blinka adafruit-circuitpython-ssd1306

#i2c this is needed for the oled display
sudo raspi-config nonint do_i2c 0

#setup dnsmasq
echo "interface=wlan0

dhcp-range=10.42.0.10,10.42.0.100,12h

address=/#/10.42.0.1

dhcp-option=3,10.42.0.1
dhcp-option=6,10.42.0.1" | sudo tee /etc/dnsmasq.d/captive.conf

sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/99-pipass.conf