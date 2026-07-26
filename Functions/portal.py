from flask import Flask, redirect

def create_portal():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return """
        hello
        """

    @app.route('/<path:path>')
    def catch(path):
        return redirect('/')

    app.run(host='0.0.0.0', port=80)