sudo apt update
sudo apt upgrade -y

sudo apt install -y dnsmasq python3-flask iptables network-manager

echo "interface=wlan0

dhcp-range=10.42.0.10,10.42.0.100,12h

address=/#/10.42.0.1

dhcp-option=3,10.42.0.1
dhcp-option=6,10.42.0.1" | sudo tee /etc/dnsmasq.d/captive.conf

sudo systemctl restart dnsmasq

sudo sysctl -w net.ipv4.ip_forward=0
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/99-pipass.conf

sudo iptables -t nat -D PREROUTING -i wlan0 -p tcp --dport 80 -j DNAT --to-destination 10.42.0.1:8080 2>/dev/null

sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j DNAT --to-destination 10.42.0.1:8080