from flask import Flask, redirect
import subprocess
import time

def create_portal():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return """
        hello
        """

    @app.route('/generate_204')
    @app.route('/gen_204')
    def android():
        return redirect('/')

    @app.route('/hotspot-detect.html')
    @app.route('/library/test/success.html')
    def apple():
        return redirect('/')

    @app.route('/ncsi.txt')
    @app.route('/connecttest.txt')
    @app.route('/redirect')
    def windows():
        return redirect('/')

    @app.route('/success.txt')
    def linux():
        return redirect('/')

    @app.route('/<path:path>')
    def catch(path):
        return redirect('/')

    app.run(host='0.0.0.0', port=8080, debug=False,use_reloader=False)

def setup_portal():
    subprocess.run(['sudo', 'systemctl', 'restart', 'dnsmasq'], check=True)
    subprocess.run(
        ['sudo', 'iptables', '-t', 'nat', '-D', 'PREROUTING',
         '-i', 'wlan0', '-p', 'tcp', '--dport', '80',
         '-j', 'DNAT', '--to-destination', f'{gateway_ip}:{portal_port}'],
        stderr=subprocess.DEVNULL
    )
    subprocess.run(
        ['sudo', 'iptables', '-t', 'nat', '-A', 'PREROUTING',
         '-i', 'wlan0', '-p', 'tcp', '--dport', '80',
         '-j', 'DNAT', '--to-destination', f'{gateway_ip}:{portal_port}'],
        check=True
    )

def restart_dnsmasq():
    subprocess.run(['sudo', 'systemctl', 'restart', 'dnsmasq'], check=True)