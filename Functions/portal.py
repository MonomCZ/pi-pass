from flask import Flask, redirect, render_template, request
import subprocess
import time
import os
import random
import uuid
from werkzeug.utils import secure_filename

def create_portal():
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB

    @app.route('/')
    def index():

        image_folder='Functions/static/cool_images'
        
        images = [
        f for f in os.listdir(image_folder)
        if f.lower().endswith((
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.webp'
        ))
    ]
        random_image = None
        if images:
            random_image = random.choice(images)

        return render_template('index.html',random_image=random_image)
    
    @app.route('/uploaded', methods=['POST'])
    def upload():
        if 'image' not in request.files:
            return "No file"

        file = request.files['image']

        if file.filename == '':
            return redirect('/')

        
        extension = os.path.splitext(secure_filename(file.filename))[1].lower()

        # generates like random nonsense filename with the same extension as the original file
        new_filename = f"{uuid.uuid4().hex}{extension}"

        file.save(os.path.join(
            "Functions/static/cool_images",
            new_filename
        ))

        return "Uploaded!"

    @app.route('/upload')
    def upload_page():

        image_folder='Functions/static/cool_images'
        
        images = [
        f for f in os.listdir(image_folder)
        if f.lower().endswith((
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.webp'
        ))
    ]
        random_image = None
        if images:
            random_image = random.choice(images)

        return render_template('upload.html',random_image=random_image)

    @app.errorhandler(413)
    def too_large(e):
        return "Obrázek je příliš velký. Maximální velikost je 50 MB.", 413

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

def setup_portal(gateway_ip='10.42.0.1', portal_port=8080):
    #subprocess.run(['sudo', 'systemctl', 'restart', 'dnsmasq'], check=True)
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
    time.sleep(5)
    subprocess.run(['sudo', 'systemctl', 'restart', 'dnsmasq'], check=True)